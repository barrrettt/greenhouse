
import time
from modules import humidity
import logging

def main():
    log = logging.getLogger("main")
    log.info("Start greenhouse 🌱🌾🍅🫑")
    
    try:
        # main loop
        while True:
            try:
                humidity.read()
                time.sleep(0.1)
                
            except Exception as e:
                log.error(f"Error main loop {e}") 
                
    except KeyboardInterrupt:
        log.info("User stop") 
        
# script run
if __name__ == "__main__": 
    main()


