import spidev  # Installation: See README.md for proper installation instructions
import time

# MCP3008 SPI Configuration
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 1000000  # Set SPI speed to 1MHz

# Define the channel for the rain sensor
RAIN_CHANNEL = 2  # Default to channel 0, can be changed as needed

# Calibration values for the rain sensor
DRY_VALUE = 980   # Value when sensor is completely dry
WET_VALUE = 300    # Value when sensor is wet (adjust based on your sensor)

def read_channel(channel):
    # Read analog data from MCP3008 ADC
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def calculate_wetness_percentage(value):
    # Convert ADC value to wetness percentage
    # Clamp value to calibration range
    value = max(min(value, DRY_VALUE), WET_VALUE)
    # Calculate percentage (reversed because higher ADC value = drier)
    return ((DRY_VALUE - value) / (DRY_VALUE - WET_VALUE)) * 100

try:
    print("Rain Sensor Analog Monitoring Started")
    print(f"Using MCP3008 channel: {RAIN_CHANNEL}")
    print("Press CTRL+C to exit")
    print("----------------------------------------")
    
    while True:
        # Read raw analog value from rain sensor
        raw_value = read_channel(RAIN_CHANNEL)
        
        # Convert raw value to wetness percentage
        wetness = calculate_wetness_percentage(raw_value)
        
        # Display both raw ADC value and calculated percentage
        print(f"Raw: {raw_value} | Wetness: {wetness:.1f}% | Channel: {RAIN_CHANNEL}")
        
        # Interpret the wetness level
        if wetness < 10:
            print("Status: DRY - No rain detected")
        elif wetness < 50:
            print("Status: DAMP - Light rain/moisture")
        else:
            print("Status: WET - Heavy rain detected")
            
        print("----------------------------------------")
        time.sleep(1)  # Wait for 1 second before next reading
        
except KeyboardInterrupt:
    print("Program stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean shutdown
    spi.close()  # Release SPI resources
    print("SPI connection closed")
