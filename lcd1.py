import spidev
import time
import RPi.GPIO as GPIO

# ???????
RST_PIN = 25  # RST ?????? ??
CS_PIN = 8    # RS ?? CS ?????? ??

# ????? GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RST_PIN, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT)

# ????? ????? ??????
GPIO.output(RST_PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(RST_PIN, GPIO.HIGH)

# ????? SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0 (CE0)
spi.max_speed_hz = 500000

def send_command(cmd):
    GPIO.output(CS_PIN, GPIO.LOW)
    spi.writebytes([0xF8, cmd & 0xF0, (cmd << 4) & 0xF0])
    GPIO.output(CS_PIN, GPIO.HIGH)
    time.sleep(0.001)

def send_data(data):
    GPIO.output(CS_PIN, GPIO.LOW)
    spi.writebytes([0xFA, data & 0xF0, (data << 4) & 0xF0])
    GPIO.output(CS_PIN, GPIO.HIGH)
    time.sleep(0.001)

def init_display():
    send_command(0x30)  # Basic Instruction
    send_command(0x0C)  # Display ON
    send_command(0x01)  # Clear display
    time.sleep(0.01)

def write_text(line, text):
    addresses = [0x80, 0x90, 0x88, 0x98]  # ?????? ???????
    send_command(addresses[line])
    for char in text:
        send_data(ord(char))

# ????? ??????
init_display()
write_text(0, "Hello ST7920!")
write_text(1, "From Raspberry Pi")

# ?????
time.sleep(10)
spi.close()
GPIO.cleanup()