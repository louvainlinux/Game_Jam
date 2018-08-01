import capteur
import RPi.GPIO as GPIO
import time

red = 22
blue = 27
green = 17

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    try:

        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        while True:
            dist = capteur.distance()
            print("Measured distance = %1f cm" % dist)
            time.sleep(0.1)
            if dist < 10.0:
                GPIO.output(red, True)
            else:
                GPIO.output(red, False)

            if dist < 15.0:
                GPIO.output(blue, True)
            else:
                GPIO.output(blue,False)

            if dist < 20.0:
                GPIO.output(green, True)
            else:
                GPIO.output(green, False)


    except KeyboardInterrupt:
        print("Measurement stopped by user")
        capteur.cleanup()
        GPIO.cleanup()
