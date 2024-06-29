import logging

from modules import my_log
from modules import humidity
def main():
    log = my_log.logger
    log.info("Start greenhouse 🌱🌾🍅🫑")
    humidity.read()
    
# script run
if __name__ == "__main__": 
    main()


