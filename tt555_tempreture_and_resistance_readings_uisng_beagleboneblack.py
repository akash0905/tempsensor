import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_40"
led1="P9_41"
led2="P9_30"
led3="P9_23"
led4="P8_11"
led5="P8_8"
led6="P8_10"
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.setup(led5,GPIO.OUT)
GPIO.setup(led6,GPIO.OUT)
while(1):
        potval=ADC.read(analogPin)
        potvolt=potval*1.8
        r2=(r1*((1.8/potvolt)-1))/1000
        print"The Tempreture is",r2
        sleep(0.5)
        if (a>=5.32 and  a<5.89):
                print"The tempreture is 40 Degree Celsius"
                GPIO.output(led1,GPIO.HIGH)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.LOW)

        elif(a>=5.89 and  a<6.53):
                print"The tempreture is 37 Degree Celsius"
                GPIO.output(led1,GPIO.LOW)
		GPIO.output(led2,GPIO.HIGH)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.LOW)
        elif(a>=6.53 and  a<7.24):
                print"The tempreture is 35 Degree Celsius"
                GPIO.output(led1,GPIO.LOW)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.HIGH)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.LOW)
        elif (a>=7.24 and  a<8.05):
                print"The tempreture is 30 Degree Celsius"
                GPIO.output(led1,GPIO.HIGH)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.HIGH)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.LOW)
        if (a>=8.05 and  a<8.96):
                print"The tempreture is 27.5 Degree Celsius"
                GPIO.output(led1,GPIO.HIGH)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.HIGH)
                GPIO.output(led6,GPIO.LOW)
        if (a>=8.96 and  a<10):
                print"The tempreture is 25 Degree Celsius"
                GPIO.output(led1,GPIO.HIGH)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.HIGH)
        else:
                print"The tempreture is below 24 Degree Celsius"
                GPIO.output(led1,GPIO.LOW)
		GPIO.output(led2,GPIO.LOW)
                GPIO.output(led3,GPIO.LOW)
                GPIO.output(led4,GPIO.LOW)
                GPIO.output(led5,GPIO.LOW)
                GPIO.output(led6,GPIO.LOW)

GPIO.cleanup()
