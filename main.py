import RPi.GPIO as GPIO
import threading
import time

import logging
from modules import my_log

from sensors import humidity_ground
from sensors import luminosity
from sensors import pasive_ir
from sensors import temp_humidity_dht20

from actuators import reles8

data = {
    'humidity': None,
    'luminosity': None,
    'pasive_ir': None,
    'humidity_ground': None,
    'temperature_air': None,
    'humidity_air': None,
}

running = True
log = logging.getLogger()

def main():
    
    log.info("Start greenhouse 🌱🌾🍅🫑")
    
    global data
    global running
    
    try:
        # launch threads
        t_luminosity = threading.Thread(
            target=luminosity.read_loop, 
            args=(data, lambda:running)
            )
        t_luminosity.start()
        
        t_pasive_ir= threading.Thread(
            target=pasive_ir.read_loop, 
            args=(data, lambda:running)
            )
        t_pasive_ir.start()
        
        t_humidity_ground = threading.Thread(
            target=humidity_ground.read_loop, 
            args=(data, lambda:running)
            )
        t_humidity_ground.start()

        t_dht20 = threading.Thread(
            target=temp_humidity_dht20.read_loop, 
            args=(data, lambda:running)
            )
        t_dht20.start()        

        # Main loop 
        while True:
            try:
                save_data()

                # Actuators ----
                #engine_on_off.check()
                
                light_on = (data["luminosity"] <= 10)
                reles8.set_pin_state(21,light_on)
            
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
            finally:
                time.sleep(0.2)
                
    except KeyboardInterrupt:
        log.debug("User interrupt: stopping...") 
        running = False
        # waiting for threads finish 
        t_luminosity.join()
        t_pasive_ir.join()
        t_humidity_ground.join()
        t_dht20.join()
        
    finally:
        GPIO.cleanup()
        log.debug("Exit 👋") 
        
        
def save_data():
    global data
    #log.debug(f"Sensor Data: {data}")
    
    
# script run
if __name__ == "__main__": 
    main()


