import RPi.GPIO   GPIO

GPIO.setwarnings ( false )

GPIO.setmode(GPIO.BCM)

GPIO.setting ( 18 ,GPIO.OUT )

while the truth:

  GPIO.output ( 18 ,GPIO.HIGH )

  Print ( "LED on" )

  sleep ( 1 )

  GPIO.OUTPUT ( 18 ,GPIO.LOW )

  Print ( "LED off" )

  sleep ( 1 )