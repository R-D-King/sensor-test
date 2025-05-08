import spidev  # Installation: See README.md for proper installation instructions
import time

# MCP3008 SPI Configuration
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 1000000  # Set SPI speed to 1MHz

# Define the channel for the LDR sensor
LDR_CHANNEL = 1  # Default to channel 0, can be changed as needed

def read_channel(channel):
    # Read analog data from MCP3008 ADC
    # MCP3008 communication protocol requires 3 bytes:
    # 1st byte: Start bit (1)
    # 2nd byte: Single-ended mode (1) + channel selection (3 bits) + padding
    # 3rd byte: Don't care (0) - needed to clock out the data
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    
    # Extract the 10-bit ADC value from the response:
    # - adc[1] contains 2 least significant bits of the result
    # - adc[2] contains the remaining 8 bits
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convert_to_percent(value, min_val, max_val):
    # Convert raw ADC value to percentage based on calibration range
    # Formula: ((current - min) / (max - min)) * 100
    percent = ((max_val - value) / (max_val - min_val)) * 100
    return max(0, min(100, percent))  # Clamp values to 0-100% range

# Calibration values for the LDR sensor
LDR_MIN = 0      # ADC value in complete darkness (0V)
LDR_MAX = 1023   # ADC value in bright light (3.3V) - 10-bit ADC has max value of 1023

try:
    while True:
        # Read raw analog value from LDR connected to the specified channel
        ldr_raw = read_channel(LDR_CHANNEL)
        
        # Convert raw value to light percentage
        ldr_percent = convert_to_percent(ldr_raw, LDR_MIN, LDR_MAX)
        
        # Display both raw ADC value and calculated percentage
        print(f"Raw: {ldr_raw} | Percentage: {ldr_percent:.1f}% | Channel: {LDR_CHANNEL}")
        time.sleep(1)  # Wait for 1 second before next reading
        
except KeyboardInterrupt:
    # Clean shutdown on Ctrl+C
    spi.close()  # Release SPI resources
    print("\nExiting...")
