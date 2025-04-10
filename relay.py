import RPi.GPIO as GPIO  # Installation: See README.md for proper installation instructions
from time import sleep

# Configuration
relay_pin = 17  # Replace with your GPIO pin number
on_time = 1     # Time in seconds to keep relay ON
off_time = 1    # Time in seconds to keep relay OFF

# Setup GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
# Initialize relay to OFF state
GPIO.output(relay_pin, GPIO.LOW)

print(f"Relay control started on GPIO pin {relay_pin}")
print("Press CTRL+C to exit")

try:
    while True:
        # Turn on the relay
        GPIO.output(relay_pin, GPIO.HIGH)  # Note: Some relays may use LOW for ON
        print("Relay ON")
        sleep(on_time)

        # Turn off the relay 
        GPIO.output(relay_pin, GPIO.LOW)   # Note: Some relays may use HIGH for OFF
        print("Relay OFF")
        sleep(off_time)

except KeyboardInterrupt:
    print("Program stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Always clean up GPIO settings on exit
    GPIO.cleanup()
    print("GPIO cleaned up")