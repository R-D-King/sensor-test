import RPi.GPIO as GPIO  # Installation: See README.md for proper installation instructions
import time

# Configuration
RAIN_PIN = 17  # GPIO pin connected to rain sensor's digital output

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_PIN, GPIO.IN)

print(f"Rain Sensor Monitoring Started on GPIO pin {RAIN_PIN}")
print("Press CTRL+C to exit")
print("----------------------------------------")

try:
    last_state = None
    while True:
        # Read current state from sensor
        current_state = GPIO.input(RAIN_PIN)
        
        # Only print when state changes to reduce console spam
        if current_state != last_state:
            if current_state == 0:
                print("Rain detected!")
            else:
                print("No rain detected")
            last_state = current_state
            
        # Delay between readings
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Program stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("GPIO cleaned up")