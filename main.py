import RPi.GPIO as GPIO
import threading
import time

import logging
from modules import my_log

from modules import humidity_ground
from modules import luminosity
from modules import pasive_ir

from modules import reles8

data = {
    'humidity': None,
    'luminosity': None,
    'pasive_ir': None,
}

running = True

def main():
    log = logging.getLogger()
    log.info("Start greenhouse 🌱🌾🍅🫑")
    
    global data
    global running
    
    try:
        
        luminosity_thread = threading.Thread(target=luminosity.read_loop, args=(data, lambda:running))
        luminosity_thread.start()
        
        pasive_ir_thread = threading.Thread(target=pasive_ir.read_loop, args=(data, lambda:running))
        pasive_ir_thread.start()
        
        # Main loop 
        while True:
            try:
                log.info(f"Sensor Data: {data}")
                # Sensors 
                #humidity_ground.read()
                #status = pasive_ir.check() #ok
                
    
                #sensor_ir.check()
                
                # Actuators ----
                #engine_on_off.check()
                
                #light_on = (lux <= 10)
                #reles8.set_pin_state(16,light_on)
            
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
            finally:
                time.sleep(0.2)
                
    except KeyboardInterrupt:
        log.debug("User interrupt: stopping...") 
        running = False
        luminosity_thread.join()
        
    finally:
        GPIO.cleanup()
        log.debug("Exit 👋") 
        
# script run
if __name__ == "__main__": 
    main()


