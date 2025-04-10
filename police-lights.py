import RPi.GPIO as GPIO  # Installation: See README.md for proper installation instructions
import time

# تعريف أرقام البنوط
RED_LED_PIN = 17    # البن المستخدم للـ LED الأحمر
BLUE_LED_PIN = 18   # البن المستخدم للـ LED الأزرق

# إعداد وضع الـ GPIO
GPIO.setmode(GPIO.BCM)  # استخدم أرقام BCM بدلًا من أرقام اللوحة
GPIO.setup(RED_LED_PIN, GPIO.OUT)  # ضبط بن الـ LED الأحمر كخرج
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)  # ضبط بن الـ LED الأزرق كخرج

try:
    while True:
        # تشغيل الـ LED الأحمر وإيقاف الـ LED الأزرق
        GPIO.output(RED_LED_PIN, GPIO.HIGH)  # تشغيل LED الأحمر
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)  # إيقاف LED الأزرق
        print("RED LED ON | BLUE LED OFF")
        time.sleep(0.2)  # الانتظار لمدة 0.2 ثانية

        # تشغيل الـ LED الأزرق وإيقاف الـ LED الأحمر
        GPIO.output(RED_LED_PIN, GPIO.LOW)  # إيقاف LED الأحمر
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)  # تشغيل LED الأزرق
        print("RED LED OFF | BLUE LED ON")
        time.sleep(0.2)  # الانتظار لمدة 0.2 ثانية

except KeyboardInterrupt:
    # في حالة إيقاف البرنامج بالضغط على Ctrl+C
    print("تم إيقاف البرنامج")
    GPIO.output(RED_LED_PIN, GPIO.LOW)  # التأكد من إيقاف الـ LED الأحمر
    GPIO.output(BLUE_LED_PIN, GPIO.LOW)  # التأكد من إيقاف الـ LED الأزرق
    GPIO.cleanup()  # إعادة ضبط إعدادات الـ GPIO