import RPi.GPIO as GPIO  # Installation: See README.md for proper installation instructions
import time

# تعريف رقم البن الذي سيتم توصيل LED عليه
LED_PIN = 17
# وقت التشغيل والإيقاف بالثواني
ON_TIME = 5
OFF_TIME = 5

# إعداد وضع الـ GPIO
GPIO.setmode(GPIO.BCM)  # استخدم أرقام BCM بدلًا من أرقام اللوحة
GPIO.setup(LED_PIN, GPIO.OUT)  # ضبط البن كخرج

try:
    print(f"LED Test Started on GPIO {LED_PIN} (Press CTRL+C to exit)")
    print("----------------------------------------")
    
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # تشغيل LED
        print("LED ON")
        time.sleep(ON_TIME)

        GPIO.output(LED_PIN, GPIO.LOW)  # إيقاف LED
        print("LED OFF")
        time.sleep(OFF_TIME)

except KeyboardInterrupt:
    print("Program stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()  # إعادة ضبط GPIO عند الخروج
    print("GPIO cleaned up")