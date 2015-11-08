import RPi.GPIO as GPIO
import time

# Stablish connections with the AndroidApp

GPIO.setmode(GPIO.BCM)#GPIO number

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT)
#GPIO.setup(20, GPIO.OUT)

PWM_FREQ = 100
DUTY_CYCLE = 100

#Motor 1
pwm_pin1 = GPIO.PWM(18,PWM_FREQ)
pwm_pin1.start(0)
pwm_pin1.ChangeDutyCycle(DUTY_CYCLE)

#motor 1
pwm_pin2 = GPIO.PWM(23,PWM_FREQ)
pwm_pin2.start(0)
pwm_pin2.ChangeDutyCycle(DUTY_CYCLE)

#Motor 2
#pwm_pin3 = GPIO.PWM(16,PWM_FREQ)
#pwm_pin3.start(0)
#pwm_pin3.ChangeDutyCycle(DUTY_CYCLE)

#motor 2
#pwm_pin4 = GPIO.PWM(20,PWM_FREQ)
#pwm_pin4.start(0)
#pwm_pin4.ChangeDutyCycle(DUTY_CYCLE)


time.sleep(10)

pwm_pin1.stop()
pwm_pin2.stop()
#pwm_pin3.stop()
#pwm_pin4.stop()

GPIO.cleanup()
