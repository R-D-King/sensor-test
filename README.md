
# sensor-test
Sensors test scripts for my raspberry pi graduation project

## Project Overview
This repository contains test scripts for various sensors used with Raspberry Pi. These scripts are part of a graduation project focused on sensor integration and monitoring.

## Sensors Included
- Temperature/Humidity (DHT22)
- Barometric Pressure (BMP180)
- Soil Moisture
- Rain Detection (Digital & Analog)
- Light Detection (LDR - Digital & Analog)
- LCD Display (16x2)
- Relay Control

## Installation Instructions

### Setting up a Virtual Environment (Recommended)
```bash
# Install required system dependencies
sudo apt update
sudo apt install -y python3-pip python3-venv libgpiod2

# Create and activate a virtual environment
python3 -m venv testing-venv
source testing-venv/bin/activate

# Install from requirements.txt
pip install -r requirements.txt
```

## Usage
Each sensor has its own Python script that can be run independently:

```bash
# Example: Run the DHT22 temperature/humidity sensor test
python3 dht22.py

# Example: Run the LCD display test
python3 16x2.py
```

## Calibration
For sensor calibration instructions, see the [SENSOR_CALIBRATION_GUIDE.txt](SENSOR_CALIBRATION_GUIDE.txt) file.

## Hardware Connections
Each script contains pin configuration at the top of the file. Default connections:

- DHT22: GPIO 26
- BMP180: I2C (SDA/SCL)
- LCD 16x2: RS=25, E=24, Data=[23, 17, 18, 22]
- Rain Sensor (Digital): GPIO 17
- LDR (Digital): GPIO 4
- Relay: GPIO 21
