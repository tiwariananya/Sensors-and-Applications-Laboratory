import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 1. Dataset Configuration
files = {
    'Static': 'Static.csv',
    'Walking': 'walking.csv',
    'Climbing Up Stairs': 'UP stairs.csv',
    'Climbing Down Stairs': 'Walking Down the Stairs.csv'
}

results = []
plt.figure(figsize=(12, 10))

for idx, (activity, fname) in enumerate(files.items(), 1):
    # Skip the 6 header metadata lines created by Physics Toolbox Sensor Suite
    df = pd.read_csv(fname, skiprows=6)
    df.columns = [c.strip() for c in df.columns]
    
    # 2. Compute 3-Axis Acceleration Magnitude: ||a|| = sqrt(ax^2 + ay^2 + az^2)
    df['mag'] = np.sqrt(df['ax (m/s^2)']**2 + df['ay (m/s^2)']**2 + df['az (m/s^2)']**2)
    
    # 3. Apply Simple Moving Average (SMA) filter (window = 15 samples ~ 0.15s at 100 Hz)
    window_size = 15
    df['mag_smooth'] = df['mag'].rolling(window=window_size, center=True).mean().fillna(df['mag'])
    
    # 4. Peak Detection for Step Counting
    # distance = 35 samples enforces a minimum 0.35s gap between steps (~2.8 steps/sec max)
    threshold = 1.8 if activity != 'Static' else 1.0
    peaks, _ = find_peaks(df['mag_smooth'], height=threshold, distance=35)
    
    if activity == 'Static':
        peaks = []  # Suppress false positives for static calibration
        
    duration = df['time'].iloc[-1] - df['time'].iloc[0]
    step_count = len(peaks)
    cadence = (step_count / duration) if duration > 0 else 0
    mean_val = df['mag'].mean()
    std_val = df['mag'].std()
    max_val = df['mag'].max()
    
    # 5. Rule-Based Classification Logic
    if std_val < 0.1:
        classified = "Static / Resting"
    elif mean_val < 2.2 and max_val < 8.0:
        classified = "Walking (Flat)"
    elif max_val >= 10.0 or std_val > 1.4:
        classified = "Stairs (High Impact / Down/Up)"
    else:
        classified = "Stairs (Up)"
        
    results.append({
        'Activity': activity,
        'Duration (s)': round(duration, 2),
        'Data Points': len(df),
        'Mean Mag (m/s²)': round(mean_val, 3),
        'Std Dev (m/s²)': round(std_val, 3),
        'Max Mag (m/s²)': round(max_val, 3),
        'Steps Detected': step_count,
        'Cadence (steps/s)': round(cadence, 2),
        'Classified As': classified
    })
    
    # 6. Plot the first 10 seconds of each activity
    plot_df = df[df['time'] <= 10.0]
    plot_peaks, _ = find_peaks(plot_df['mag_smooth'], height=threshold, distance=35)
    if activity == 'Static':
        plot_peaks = []
        
    plt.subplot(4, 1, idx)
    plt.plot(plot_df['time'], plot_df['mag'], label='Raw Magnitude', alpha=0.35, color='gray')
    plt.plot(plot_df['time'], plot_df['mag_smooth'], label='Smoothed (SMA)', color='blue', linewidth=1.5)
    if len(plot_peaks) > 0:
        plt.plot(plot_df['time'].iloc[plot_peaks], plot_df['mag_smooth'].iloc[plot_peaks], 'ro', label='Detected Steps')
    
    plt.title(f"{activity} (0 - 10s Window)")
    plt.xlabel("Time (s)")
    plt.ylabel("Acc ($m/s^2$)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig("activity_plots.png", dpi=200)
plt.show()

# Print Table Summary
summary_table = pd.DataFrame(results)
print("\n" + "="*80)
print("EXPERIMENTAL SUMMARY & STEP COUNT RESULTS")
print("="*80)
print(summary_table.to_string(index=False))