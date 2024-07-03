import RPi.GPIO as GPIO
import logging

log = logging.getLogger(__name__)

# set up pin
GPIO.setmode(GPIO.BCM)
pin_DO = 17
GPIO.setup(pin_DO, GPIO.IN)


def read():
    status = GPIO.input(pin_DO)
    
    if status == GPIO.HIGH:
        log.debug("Humidity: ---")
    else:
        log.debug("Humidity: YES")
    
    return status
