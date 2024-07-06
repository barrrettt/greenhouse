import RPi.GPIO as GPIO
import logging
import time

log = logging.getLogger(__name__)

# set up B0B2DY4CZS 🌱 
GPIO.setmode(GPIO.BCM)
PIN = 26
GPIO.setup(PIN, GPIO.IN)


def read_loop(data,running):
     while running():
        try:
            if not GPIO.input(PIN):
                log.debug("🌱")
                data["humidity_ground"] = True 
            else:
                log.debug("--")
                data["humidity_ground"] = False 
        except:
            log.debug("No se puede leer el IR")
            data["humidity_ground"] = False 

        finally:
            time.sleep(0.5)
