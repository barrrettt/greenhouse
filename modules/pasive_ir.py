import RPi.GPIO as GPIO
import time
import logging
log = logging.getLogger(__name__)

# Config
PIN = 13 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

def check():
    try:
        if GPIO.input(PIN):
            log.info("Movimiento detectado!")
            return True
        else:
            log.info("---")
            return False
    except:
        log.info("No se puede leer el IR")
        return False
