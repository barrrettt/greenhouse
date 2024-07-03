import RPi.GPIO as GPIO
import time
import logging
log = logging.getLogger(__name__)

# Config Pasive IR 👁️
PIN = 26 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

def check():
    try:
        if GPIO.input(PIN):
            log.debug("👁️")
            return True
        else:
            log.debug("--")
            return False
    except:
        log.debug("No se puede leer el IR")
        return False
