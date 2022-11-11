## AUTHOR: Garima
## TASK : 7.3D (RPi PWM)

from gpiozero import LED
import RPi.GPIO 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)   # setting GPIO numbering
GPIO.setwarnings(False)   # to disable warnings

TRIG = 18
ECHO = 24

GPIO.setup(12, GPIO.OUT)    # setting 12 as output pin 

led = GPIO.PWM(12, 100)     #Creates an PWM instance and assigns it to variable led
led.start(0)              #starts the PWM

GPIO.setup(TRIG, GPIO.OUT)     
GPIO.setup(ECHO, GPIO.IN)

def Distance():
    GPIO.output(TRIG, True)    # sets Trig to HIGH
    time.sleep(0.001)
    GPIO.output(TRIG, False)   # sets Trig to LOW
 
    start_time = time.time()
    stop_time = time.time()
  
    while GPIO.input(ECHO) == 0:   #saves the start time
        start_time = time.time()
 
    while GPIO.input(ECHO) == 1:   #saves the stop time
        stop_time = time.time()
 
    TimeElapsed = stop_time - start_time
    distance = (TimeElapsed * 34300) / 2       
 
    return int(distance)

try:
    while True:
        dist = Distance()
        print ("Distance = " + str(dist) + " cm")    
        if dist < 50:
                led.ChangeDutyCycle((50 - dist)*2)   # to change the intensity of led
        else:
            led.start(0)    #starts the PWM    
        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()     #cleans up all the ports used
