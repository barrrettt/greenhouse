import time
import RPi.GPIO as GPIO
import logging
from modules import my_log
from modules import humidity
from modules import luminosity
from modules import pasive_ir
from modules import sensor_ir
from modules import engine

def main():
    log = logging.getLogger("__name__")
    log.info("Start greenhouse 🌱🌾🍅🫑")
    try:
        # Main loop 
        while True:
            try:
                # Sensors 
                humidity.read()
                #luminosity.read()
                #pasive_ir.check()
                #sensor_ir.check()
                
                # Actuators ----
                engine.check()
                
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
            finally:
                time.sleep(0.5)   
                
    except KeyboardInterrupt:
        log.info("User stop") 
        
    finally:
        GPIO.cleanup()
        
# script run
if __name__ == "__main__": 
    main()


