from luma.core.interface.serial import spi  # Installation: See README.md for proper installation instructions
from luma.lcd.device import st7920  # Installation: See README.md for proper installation instructions
from PIL import ImageDraw, Image  # Installation: See README.md for proper installation instructions
from time import sleep

# Define the connection
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25)

# Define the display
device = st7920(serial_interface=serial)

try:
    print("LCD Test Started (Press CTRL+C to exit)")
    print("----------------------------------------")
    
    # Simple drawing
    image = Image.new("1", device.size)
    draw = ImageDraw.Draw(image)
    
    # Draw a rectangle
    draw.rectangle((10, 10, 100, 50), outline=1, fill=0)
    
    # Add text
    draw.text((15, 20), "Hello Khaled!", fill=1)
    
    # Display the image
    device.display(image)
    print("Test image displayed. Will clear in 5 seconds...")
    sleep(5)
    
    # Clear the display
    device.clear()
    print("Display cleared.")

except KeyboardInterrupt:
    print("Program stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up
    if 'device' in locals():
        device.clear()
    print("Test completed.")