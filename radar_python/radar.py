import capteur
import RPi.GPIO as GPIO
import time

red = 22    # LED rouge connectée au PIN 22 du Raspberry
orange = 27 # LED orange connectée au PIN 27 du Raspberry
green = 17  # LED verte connectée au PIN 17 du Raspberry

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__': # fonction main (principale)
    try:

        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(orange, GPIO.OUT)
        while True:
            ## TODO: recuperer la distance (fonction distance())
            ## et allumer les leds en fonction de cette distance :
            ## rouge : distance < 10 cm
            ## orange : distance < 15 cm
            ## verte : distance < 20 cm



    except KeyboardInterrupt:
        print("Measurement stopped by user")
        capteur.cleanup()
        GPIO.cleanup()
