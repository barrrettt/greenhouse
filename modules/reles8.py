import RPi.GPIO as GPIO
import time
import logging

log = logging.getLogger(__name__)

# RELES8 🤖
PINS = {
    14: False,
    15: False,
    18: False,
    25: False,
    8: False,
    7: False,
    12: False,
    16: False,
}

def setup(pins):
    global PINS 
    if pins:
        PINS = pins
        
    # all are output
    GPIO.setmode(GPIO.BCM)
    for pin in PINS: 
        GPIO.setup(pin, GPIO.OUT)
    
def set_pin_state(pin_number, state):
    if pin_number in PINS:
        if state:
            #  HIGH (True)
            PINS[pin_number] = True
            log.debug(f"RELE8🤖 {pin_number} 💡")
            
        else:
            PINS[pin_number] = False

        # set state
        GPIO.output(pin_number, GPIO.LOW if state else GPIO.HIGH)
        
    else:
        log.error(f"NO PIN {pin_number} in dicctionary")