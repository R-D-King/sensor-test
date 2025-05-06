from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep

# ??? ?????? ??? ??? GPIO ?????? ????????
lcd = CharLCD(cols=16, rows=2, pin_rs=25, pin_e=24, pins_data=[23, 17, 18, 22],
              numbering_mode=GPIO.BCM)

lcd.clear()
lcd.write_string('Hello, Korolos!')
sleep(3)
lcd.cursor_pos = (1, 0)
lcd.write_string('LCD 16x2 OK!')
