import RPi.GPIO as GPIO
import time
import logging

log = logging.getLogger(__name__)

# RELES8 🤖
PINS = {
    18: False,
    23: False,
    24: False,
    25: False,
    12: False,
    16: False,
    20: False,
    21: False,
}
        
# all are output
GPIO.setmode(GPIO.BCM)
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
                
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