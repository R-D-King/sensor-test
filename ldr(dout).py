import RPi.GPIO as GPIO  # Installation: See README.md for proper installation instructions
import time

# Define the GPIO pin connected to D0 output of LDR sensor
LDR_PIN = 17

# Setup GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

# Continuous reading implementation
try:
    last_state = None
    print("LDR Sensor Monitoring Started (Press CTRL+C to exit)")
    print("----------------------------------------")
    
    while True:
        current_state = GPIO.input(LDR_PIN)
        if current_state != last_state:
            # Reversed the logic to match expected behavior
            if current_state == 0:
                print("Light level: HIGH")  # When D0 is LOW (0), light level is actually HIGH
            else:
                print("Light level: LOW")   # When D0 is HIGH (1), light level is actually LOW
            last_state = current_state
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
