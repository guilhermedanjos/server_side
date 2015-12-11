import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
freq = 50
#verde = 11
#azul = 13
#vermelho = 15

GPIO.setup(11, GPIO.OUT)        #vermelho
GPIO.setup(13, GPIO.OUT)        #verde
GPIO.setup(15, GPIO.OUT)        #azul

verde = GPIO.PWM(11,freq)
azul = GPIO.PWM(13,freq)
verm = GPIO.PWM(15,freq)

verm.start(0)
verde.start(0)
azul.start(0)

try:
        while True:
                for i in range(100):
                        verm.ChangeDutyCycle(i)
                        time.sleep(0.02)
                for i in range(100):
                        verm.ChangeDutyCycle(100-i)
                        time.sleep(0.02)

try:
        while True:
                for i in range(100):
                        verm.ChangeDutyCycle(i)
                        time.sleep(0.02)
                for i in range(100):
                        verm.ChangeDutyCycle(100-i)
                        time.sleep(0.02)

                for i in range(100):
                        verde.ChangeDutyCycle(i)
                        time.sleep(0.02)
                for i in range(100):
                        verde.ChangeDutyCycle(100-i)
                        time.sleep(0.02)

                for i in range(100):
                        azul.ChangeDutyCycle(i)
except KeyboardInterrupt:
        pass

verm.stop()
verde.stop()
azul.stop()


GPIO.cleanup()




