import smbus  # Installation: See README.md for proper installation instructions
import time
from ctypes import c_short
import signal
import sys

# Configuration
DEVICE = 0x77  # I2C address of BMP180 sensor
bus = smbus.SMBus(1)  # Use I2C bus 1 on Raspberry Pi

def getShort(data, index):
    # Combine two bytes and return signed 16-bit value
    return c_short((data[index] << 8) + data[index + 1]).value

def getUshort(data, index):
    # Combine two bytes and return unsigned 16-bit value
    return (data[index] << 8) + data[index + 1]

def readBmp180Id(addr=DEVICE):
    # Read chip ID and version from the sensor
    REG_ID = 0xD0
    (chip_id, chip_version) = bus.read_i2c_block_data(addr, REG_ID, 2)
    return (chip_id, chip_version)

def readBmp180(addr=DEVICE):
    # Register addresses
    REG_CALIB  = 0xAA
    REG_MEAS   = 0xF4
    REG_MSB    = 0xF6
    REG_LSB    = 0xF7
    CRV_TEMP   = 0x2E
    CRV_PRES   = 0x34
    OVERSAMPLE = 3  # Oversampling setting (0-3)

    # Read calibration data from the sensor
    cal = bus.read_i2c_block_data(addr, REG_CALIB, 22)

    # Convert bytes to calibration values
    AC1 = getShort(cal, 0)
    AC2 = getShort(cal, 2)
    AC3 = getShort(cal, 4)
    AC4 = getUshort(cal, 6)
    AC5 = getUshort(cal, 8)
    AC6 = getUshort(cal, 10)
    B1  = getShort(cal, 12)
    B2  = getShort(cal, 14)
    MB  = getShort(cal, 16)
    MC  = getShort(cal, 18)
    MD  = getShort(cal, 20)

    # Request temperature measurement
    bus.write_byte_data(addr, REG_MEAS, CRV_TEMP)
    time.sleep(0.005)  # Wait for measurement
    msb, lsb = bus.read_i2c_block_data(addr, REG_MSB, 2)
    UT = (msb << 8) + lsb

    # Request pressure measurement
    bus.write_byte_data(addr, REG_MEAS, CRV_PRES + (OVERSAMPLE << 6))
    time.sleep(0.04)  # Wait for measurement
    msb, lsb, xsb = bus.read_i2c_block_data(addr, REG_MSB, 3)
    UP = ((msb << 16) + (lsb << 8) + xsb) >> (8 - OVERSAMPLE)

    # Calculate true temperature
    X1 = ((UT - AC6) * AC5) >> 15
    X2 = int((MC << 11) / (X1 + MD))
    B5 = X1 + X2
    temperature = int(B5 + 8) >> 4
    temperature = temperature / 10.0

    # Calculate true pressure
    B6 = B5 - 4000
    X1 = (B2 * (B6 * B6 >> 12)) >> 11
    X2 = (AC2 * B6) >> 11
    X3 = X1 + X2
    B3 = (((AC1 * 4 + X3) << OVERSAMPLE) + 2) >> 2
    X1 = (AC3 * B6) >> 13
    X2 = (B1 * (B6 * B6 >> 12)) >> 16
    X3 = ((X1 + X2) + 2) >> 2
    B4 = (AC4 * (X3 + 32768)) >> 15
    B7 = (UP - B3) * (50000 >> OVERSAMPLE)

    if B7 < 0x80000000:
        P = (B7 * 2) // B4
    else:
        P = (B7 // B4) * 2

    X1 = (P >> 8) * (P >> 8)
    X1 = (X1 * 3038) >> 16
    X2 = (-7357 * P) >> 16
    pressure = P + ((X1 + X2 + 3791) >> 4)
    pressure = pressure / 100.0  # Convert to hPa

    # Calculate altitude using pressure
    altitude = 44330.0 * (1.0 - pow(pressure / 1013.25, 1.0 / 5.255))
    altitude = round(altitude, 2)

    return (temperature, pressure, altitude)

# Function to handle clean exit
def signal_handler(sig, frame):
    print("\nProgram terminated.")
    sys.exit(0)

# Register signal handler for clean exit
signal.signal(signal.SIGINT, signal_handler)

# Main function
def main():
    print("BMP180 Sensor Monitoring Started")
    print("Press CTRL+C to exit")
    print("----------------------------------------")
    
    try:
        # Read and display chip ID and version
        chip_id, chip_version = readBmp180Id()
        print(f"Chip ID: {chip_id}, Version: {chip_version}")
        
        # Main loop
        while True:
            try:
                temperature, pressure, altitude = readBmp180()
                print(f"Temperature: {temperature:.1f} °C")
                print(f"Pressure: {pressure:.1f} hPa")
                print(f"Altitude: {altitude:.1f} m")
                print("----------------------------------------")
            except OSError as e:
                print(f"Error reading sensor: {e}")
                
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
