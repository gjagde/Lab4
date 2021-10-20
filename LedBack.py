 #!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPinB = 13
ledPinG = 19
ledPinY = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPinB, GPIO.OUT)
GPIO.setup(ledPinG, GPIO.OUT)
GPIO.setup(ledPinY, GPIO.OUT)

pwmB = GPIO.PWM(ledPinB, 100) # PWM object on our pin at 100 Hz
pwmB.start(0) # start with LED off

pwmG = GPIO.PWM(ledPinG, 100) # PWM object on our pin at 100 Hz
pwmG.start(0) # start with LED off

pwmY = GPIO.PWM(ledPinY, 100) # PWM object on our pin at 100 Hz
pwmY.start(0) # start with LED off

while True:
  with open("led_pwm.txt", 'r') as file:
    data = json.load(file) # read duty cycle value from file
  dutyCycle = int(data['slider1'])
  if(int(str(data['option'])) == 0):
    pwmB.ChangeDutyCycle(dutyCycle)
  elif(int(str(data['option'])) == 0):
    pwmG.ChangeDutyCycle(dutyCycle)
  elif(int(str(data['option'])) == 0):
    pwmG.ChangeDutyCycle(dutyCycle)  
  time.sleep(0.1)
