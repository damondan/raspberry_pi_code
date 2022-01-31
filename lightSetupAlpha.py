#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
redM = 16
buzzer = 18
buzzerFlag = "True"
gradientStarRed = 11
gradientStarBlue = 13
gradientStarGreen = 15
GPIO.setup(redM, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(gradientStarRed, GPIO.OUT)
GPIO.setup(gradientStarBlue, GPIO.OUT)
GPIO.setup(gradientStarGreen, GPIO.OUT)

ledRed = GPIO.PWM(gradientStarRed,100)
ledBlue = GPIO.PWM(gradientStarBlue,100)
ledGreen = GPIO.PWM(gradientStarGreen,100)

ledRed.start(0)
ledBlue.start(0)
ledGreen.start(0)

pause_time = 0.1

try:  
    while True:  
        if bool(buzzerFlag):
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(1)
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.HIGH)
            print ("Beep")
            sleep(0.1)
            GPIO.output(buzzer,GPIO.LOW)
            print ("No Beep")
            sleep(0.1)
            buzzerFlag = ""
            GPIO.output(redM,True)

        for i in range(0,101):      #101
            ledRed.ChangeDutyCycle(i)  
            time.sleep(pause_time)
            print("in ledRed cycling up")
        for i in range(100,-1,-1):  #100      
            ledRed.ChangeDutyCycle(i)  
            time.sleep(pause_time)

        for i in range(0,101):      #101
            ledBlue.ChangeDutyCycle(i)  
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledBlue.ChangeDutyCycle(i)  
            time.sleep(pause_time)

        for i in range(0,101):      #101
            ledGreen.ChangeDutyCycle(i)  
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledGreen.ChangeDutyCycle(i)  
            time.sleep(pause_time)

        for i in range(0,101):      #101
            ledRed.ChangeDutyCycle(i)
            ledBlue.ChangeDutyCycle(i)  
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledRed.ChangeDutyCycle(i)
            ledBlue.ChangeDutyCycle(i) 
            time.sleep(pause_time)
        
        for i in range(0,101):      #101
            ledRed.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i)  
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledRed.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i) 
            time.sleep(pause_time)
            
        for i in range(0,101):      #101
            ledBlue.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i)  
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledBlue.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i) 
            time.sleep(pause_time)
            
        for i in range(0,101):      #101
            ledRed.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i)
            ledBlue.ChangeDutyCycle(i)
            time.sleep(pause_time)  
        for i in range(100,-1,-1):  #100      
            ledRed.ChangeDutyCycle(i)
            ledGreen.ChangeDutyCycle(i)
            ledBlue.ChangeDutyCycle(i)
            time.sleep(pause_time)


except KeyboardInterrupt:
    print("Keyboard Interrupt")
    ledRed.stop()
    ledBlue.stop()
    ledGreen.stop()
    GPIO.output(redM,False)
    GPIO.cleanup()  
