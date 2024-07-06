import RPi.GPIO as GPIO
import time
import logging
log = logging.getLogger(__name__)

# Config Pasive IR 👁️
PIN = 19 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

def read_loop(data,running): 
    while running():
        try:
            if GPIO.input(PIN):
                log.debug("👁️")
                data["pasive_ir"] = True 
            else:
                log.debug("--")
                data["pasive_ir"] = False 
        except:
            log.debug("No se puede leer el IR")
            data["pasive_ir"] = False 
            
        finally:
            time.sleep(0.5)
