import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_40"
led1="P9_41"
led2="P9_30"
led3="P9_23"
led4="P8_11"

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
while(1):
        potval=ADC.read(analogPin)*1000
        a=int(potval)
        print a
        sleep(0.5)
        if (a>500 and  a<525):
                GPIO.output(led1,GPIO.HIGH)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
        elif(potval>=525 and  potval<550):
                GPIO.output(led1,GPIO.LOW)
		GPIO.output(led2,GPIO.HIGH)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
        elif(potval>=550 and potval<575):
                GPIO.output(led1,GPIO.LOW)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.HIGH)
                GPIO.output(led4,GPIO.LOW)
        else:
                GPIO.output(led1,GPIO.LOW)
		GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.HIGH)

GPIO.cleanup()
