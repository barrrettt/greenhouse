import time
import logging
from modules import my_log
from modules import humidity
from modules import luminosity

def main():
    log = logging.getLogger("__name__")
    log.info("Start greenhouse 🌱🌾🍅🫑")
    try:
        # main loop
        while True:
            try:
                humidity.read()
                luminosity.read()
                time.sleep(0.1)
                
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
    except KeyboardInterrupt:
        log.info("User stop") 
        
# script run
if __name__ == "__main__": 
    main()


