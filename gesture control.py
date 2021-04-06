import os
import subprocess
import glob
import RPi.GPIO as GPIO
import time
from time import sleep

TRIGGER = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
os.chdir('/home/pi/Music')
musicFilePath ='Preet.mp3'
f = glob.glob('Preet.mp3')
h = len(f)
status = 1
pointer = 0
start = 0
volume = 20
    
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
    return distance
      
for d in range(4,4000):
    d= int (distance())
    player = subprocess.Popen(["omxplayer {}".format(musicFilePath)],stdin=subprocess.PIPE)
    fi = player.poll()
    while d==True:
        player.stdin.write("p")
        if d>4 and d<=45:        
            vol = d/3
            if(vol>volume):
                for counter in range(1,vol-volume):
                    player.stdin.write("+")
                    volume = volume + 1
                    sleep(0.1)
            elif(vol<volume):
                for counter in range(1,volume-vol):
                    player.stdin.write("-")
                    volume = volume - 1
                    sleep(0.1)
                    print("play while 4-45cm")
        elif d>45:
            volume=0
            print("mute")
        else:
            player.stdin.write("q")
            print("out of range")

while KeyboardInterrupt:
    print("Stopped by user")
    GPIO.cleanup()
