from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

# Configuration for LCD display using GPIO pins
# Define pins for RS, E and data pins [D4, D5, D6, D7]
lcd = CharLCD(cols=16, rows=2, pin_rs=25, pin_e=24, pins_data=[23, 17, 18, 22],
              numbering_mode=GPIO.BCM)
 
# Function to handle clean exit
def signal_handler(sig, frame):
    print("\nProgram terminated.")
    # Clear the display before exit
    try:
        lcd.clear()
    except:
        pass
    GPIO.cleanup()
    sys.exit(0)

# Register signal handler for clean exit
signal.signal(signal.SIGINT, signal_handler)

def main():
    print("LCD 16x2 Display Test Started")
    print("Press CTRL+C to exit")
    print("----------------------------------------")
    
    try:
        # Clear the display
        lcd.clear()
        
        # Write to first line (row 0)
        lcd.write_string('Hello There!')
        sleep(3)
        
        # Move cursor to second line (row 1)
        lcd.cursor_pos = (1, 0)
        lcd.write_string('LCD 16x2 OK!')
        
        # Keep the program running
        while True:
            sleep(1)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # This will run if an exception occurs but not if CTRL+C is pressed
        # (which is handled by signal_handler)
        try:
            lcd.clear()
            GPIO.cleanup()
        except:
            pass

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
