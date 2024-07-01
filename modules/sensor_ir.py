import RPi.GPIO as GPIO
import time
import logging
log = logging.getLogger(__name__)

SENSOR_LEFT_PIN = 13  
SENSOR_RIGHT_PIN = 6  
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_LEFT_PIN, GPIO.IN)
GPIO.setup(SENSOR_RIGHT_PIN, GPIO.IN)

def check():
    try:
        left_sensor = GPIO.input(SENSOR_LEFT_PIN)
        right_sensor = GPIO.input(SENSOR_RIGHT_PIN)

        if left_sensor == 0:
            log.info("LEFT: ***")
        else:
            log.info("LEFT:")
            
        if right_sensor == 0:
            log.info("RIGHT: ***")
        else:
            log.info("RIGHT:")
            
        return (left_sensor, right_sensor)
    
    except Exception as e:
        log.error(f"No se puede leer el sensor:{e}")
        return (False,False)    
    
