# HVDC System Data Analysis and Optimization

This project simulates, analyzes, and optimizes data for a High Voltage Direct Current (HVDC) power system. It generates synthetic HVDC data, performs data analysis, detects anomalies, and optimizes parameters to maximize efficiency. Visualizations and reports are automatically generated for easy reference.

## Features

- **Synthetic Data Generation**: Creates realistic HVDC data for voltage, current, and power.
- **Statistical Analysis**: Calculates averages and detects anomalies.
- **Parameter Optimization**: Finds optimal voltage and current values for efficiency using a complex loss function.
- **Data Visualization**: Generates and saves multiple visualizations as PNG files.
- **Automated Report**: Summarizes analysis and optimization results.

  ## How to Run

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**: Download the project from GitHub.
   ```bash
   git clone https://github.com/mirza019/hvdc_platform.git
   cd hvdc_platform

  ```bash
    pip install -r requirements.txt
    python data/generate_data.py
    python main.py
   ```
## Check Outputs:

Figures: Generated figures are saved in the figures/ directory.
Report: A summary report is generated in the reports/ directory, named hvdc_report.txt.

## Project Structure

```plaintext
hvdc_data_analysis/
├── config.py                    # Configuration file
├── main.py                      # Main script
├── figures/                     # Generated figures
├── data/                        # Data files and generation script
├── src/                         # Analysis, optimization, and visualization modules
└── reports/                     # Generated report

