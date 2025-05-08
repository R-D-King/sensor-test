from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep
import signal
import sys
import atexit

# Set GPIO mode before creating LCD object
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Configuration for LCD display using GPIO pins
# Define pins for RS, E and data pins [D4, D5, D6, D7]
lcd = CharLCD(cols=16, rows=2, pin_rs=25, pin_e=24, pins_data=[23, 17, 18, 22],
              numbering_mode=GPIO.BCM)

# Function to display shutdown message and clean up
def cleanup():
    try:
        # Display shutdown message
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("System Inactive")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("LCD Stopped")
        sleep(1)  # Brief pause to ensure message is displayed
        
        # Then clear and close
        lcd.clear()
        lcd.close(clear=True)
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        # Only clean up GPIO pins we've used
        GPIO.cleanup([25, 24, 23, 17, 18, 22])

# Register cleanup function to run at exit
atexit.register(cleanup)
 
# Function to handle clean exit
def signal_handler(sig, frame):
    print("\nProgram terminated.")
    # Exit will trigger the atexit handler
    sys.exit(0)

# Register signal handler for clean exit
signal.signal(signal.SIGINT, signal_handler)

def main():
    print("LCD 16x2 Display Test Started")
    print("Press CTRL+C to exit")
    print("----------------------------------------")
    
    try:
        # Clear the display at start
        lcd.clear()
        
        # Write to first line (row 0) - exactly 16 characters
        lcd.cursor_pos = (0, 0)
        line1 = "Hello There!    "
        lcd.write_string(line1[:16])  # Limit to 16 chars
        sleep(2)
        
        # Move cursor to second line (row 1) - exactly 16 characters
        lcd.cursor_pos = (1, 0)
        line2 = "LCD 16x2 OK!    "
        lcd.write_string(line2[:16])  # Limit to 16 chars
        
        # Keep the program running without writing more text
        while True:
            sleep(1)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        # The atexit handler will take care of cleanup

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
