from pygame import mixer
import RPi.GPIO as GPIO
import time
from time import sleep

TRIGGER = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
mixer.init()
mixer.music.load("/home/pi/Music/Preet.mp3")

def vol(float):
    mixer.music.set_volume(float)

vol(0.7)
mixer.music.play()

def distance():
    GPIO.output(TRIGGER, GPIO.LOW)
    print ("Waiting for sensor to settle")
    time.sleep(2)
    print ("Calculating distance")
    GPIO.output(TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, GPIO.LOW)
    while GPIO.input(ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print ("Distance:",distance,"cm")
    return d
      
for d in range(4,1000):
    d= int (distance())
    while d==True:
        vol(0.7)
        mixer.music.play()
        if d>4 and d<=15:        
            vol(0.3)
            print("volune 3 while 4-15cm")
        elif d>15 and d<=30:
            vol(1)
            print("volune 10 while 15-30cm")
        elif d>30 and d<=45:
            vol(1.5)
            print("volune 15 while 30-45cm")
        elif d>45:
            vol(None)
            print("mute")
        

while KeyboardInterrupt:
    mixer.music.pause()
    print("Stopped by user")
    GPIO.cleanup()
