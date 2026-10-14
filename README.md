# Sensors and Applications Laboratory

Laboratory experiments, circuit simulations, hardware implementations, and digital signal processing pipelines for the **Sensors and Applications Laboratory** course.

---

## Repository Structure

```text
├── Experiment 4/
│   ├── 24f3100260_Week_4.pdf
│   ├── Figure_1.png
│   ├── Human_Activity_Recognition.py
│   ├── Static.csv
│   ├── UP stairs.csv
│   ├── Walking Down the Stairs.csv
│   └── walking.csv
├── 24f3100260_Week_3.pdf
├── Sensors_Lab_Week_1_Report.pdf
├── Sensors_Lab_Week_2_Report.pdf
└── README.md

1. Week 1: Design & Analysis of a 3-Op-Amp Instrumentation Amplifier (INA)File: Sensors_Lab_Week_1_Report.pdfObjective: Design, analyze, and test a three-op-amp instrumentation amplifier topology for precision low-level differential signal conditioning.   Key Highlights:Derivation of the closed-form transfer function: $V_{\text{out}} - V_{\text{ref}} = \frac{R_2}{R_1}\left(1 + \frac{2R_F}{R_G}\right)(V_{\text{IN-}} - V_{\text{IN+}})$.   Differential gain configuration for $A_d = 3$ ($R_G = 10\text{ k}\Omega$) and $A_d = 20$ ($R_G \approx 1\text{ k}\Omega$).   Common-Mode Rejection Ratio (CMRR) characterization ($\approx 69\text{ dB}$).   Frequency response sweep from $1\text{ kHz}$ to $5\text{ kHz}$.   Reference-voltage level shifting verification ($V_{\text{REF}} = 2.5\text{ V}$).   Hardware & Tools: MCP6004 Quad Op-Amp, ADALM1000, LTspice.   2. Week 2: Temperature Sensor Unit Using NTC ThermistorFile: Sensors_Lab_Week_2_Report.pdfObjective: Characterize an NTC thermistor and build an analog signal conditioning circuit to linearize and scale resistance variation into a usable voltage output.   Key Highlights:Two-point characterization between $33.4^\circ\text{C}$ ($6.9\text{ k}\Omega$) and $42.2^\circ\text{C}$ ($5.2\text{ k}\Omega$).   Target range analysis ($30^\circ\text{C} - 60^\circ\text{C}$) and voltage divider optimization ($R_1 = \sqrt{R_{\min} \cdot R_{\max}} \approx 3.65\text{ k}\Omega$).   Op-amp gain and offset stage implementation ($A_v \approx 2.53\text{ V/V}$).   Validation via LTspice sweeps, digital thermometer cross-checks, and ambient room temperature tracking.   Hardware & Tools: NTC Thermistor, MCP6004 / AD8648 Op-Amp, LTspice, Reference Clinical Thermometer.   3. Week 3: Electronic Compass Using Hall Effect SensorsFile: 24f3100260_Week_3.pdfObjective: Implement a 2-axis electronic compass resolving Earth's horizontal geomagnetic field into orthogonal $B_x$ and $B_y$ components for heading estimation.   Key Highlights:Two linear Hall sensors mounted orthogonally at $90^\circ$ on a non-magnetic carrier.   High-gain difference amplification ($R_1 = 500\ \Omega$, $R_2 = 695\text{ k}\Omega$) centered around a $2.5\text{ V}$ virtual mid-supply bias.   Noise suppression and bandwidth limiting using a $10\text{ nF}$ feedback capacitor.   Magnetic field locus analysis ($V_{\text{out}Y}\text{ vs. } V_{\text{out}X}$) across four headings and evaluation of channel gain/offset mismatches.   Hardware & Tools: Linear Hall-Effect Sensors (SS49-type), MCP6004, ADALM1000 / ALICE toolchain, LTspice.   4. Week 4: Human Activity Recognition (HAR) Using Smartphone AccelerometerFolder: Experiment 4/   24f3100260_Week_4.pdf: Full laboratory report detailing methodology, algorithm design, and results.   Human_Activity_Recognition.py: Python signal-processing script for data extraction, smoothing, step detection, and rule-based classification.   Figure_1.png: Waveform plot showing raw magnitude, smoothed magnitude (SMA), and detected peak steps across the first 10 seconds of all four recorded activities.   Static.csv, walking.csv, UP stairs.csv, Walking Down the Stairs.csv: Raw tri-axial linear accelerometer datasets logged at $100\text{ Hz}$.   Signal Processing Pipeline:Magnitude Calculation: Computes orientation-invariant scalar acceleration:
   $$\Vert{}a\Vert{} = \sqrt{a_x^2 + a_y^2 + a_z^2}$$Filtering: 15-sample Simple Moving Average (SMA) filter to attenuate sensor jitter while preserving step features.   Peak Detection: Uses scipy.signal.find_peaks with height and cadence lockout constraints to detect steps.   Activity Classification: Rule-based statistical thresholding (mean, standard deviation, and peak amplitude) distinguishing Static/Resting, Walking (Flat), Stairs (Up), and Stairs (Down / High Impact).  
