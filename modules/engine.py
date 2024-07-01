import RPi.GPIO as GPIO
import time
import logging

log = logging.getLogger(__name__)

RELAY_PIN = 26  # BCM 
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)


last_time = time.time()
interval = 2
status = False

def check():
    global last_time
    global status
    
    now = time.time()
    delta_time = now - last_time
    if delta_time >= interval:
        status = not status
        GPIO.output(RELAY_PIN, GPIO.LOW if status else GPIO.HIGH)
        last_time = now
        log.info(f"Engine: {status}")