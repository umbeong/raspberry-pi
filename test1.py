import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO.setup ( 40 ,GPIO.OUT )

while True:

  GPIO.output ( 40 ,GPIO.HIGH )

  print ( "LED on" )

  sleep ( 1 )

  GPIO.output ( 40 ,GPIO.LOW )

  print ( "LED off" )

  sleep ( 1 )

#dddd
