import time
import RPi.GPIO as GPIO
import logging
from modules import my_log
from modules import humidity_ground
from modules import temperature_humidity
from modules import luminosity
from modules import pasive_ir
from modules import sensor_ir
#from modules import engine_on_off
from modules import reles8



def main():
    log = logging.getLogger()
    log.info("Start greenhouse 🌱🌾🍅🫑")
    try:
        # Main loop 
        while True:
            try:
                # Sensors 
                #humidity_ground.read()
                lux = luminosity.read()
                status = pasive_ir.check()
                result = temperature_humidity.read()
                #sensor_ir.check()
                
                # Actuators ----
                #engine_on_off.check()
                
                light_on = (lux <= 10)
                reles8.set_pin_state(16,light_on)
            
                
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
            finally:
                time.sleep(0.2)
                
    except KeyboardInterrupt:
        log.debug("User stop") 
        
    finally:
        GPIO.cleanup()
        
# script run
if __name__ == "__main__": 
    main()


