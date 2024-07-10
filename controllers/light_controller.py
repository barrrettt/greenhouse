# Ligths on controller
from actuators import reles8
from modules import database
import time
import logging

log = logging.getLogger(__name__)

PIN_RELE = 21
LUX_LIMIT = 10
READS_TO_NIGHT = 5
READS_TO_MOVEMENT = 2
TIME_ON = 5

# LOGIC: if is night (luminosity sensor)
# if 5 reads <10 is night 
# and pasive ir detect motion
# then lights on: 10seconds

last_time = time.time()

def run():
    try:
        night = is_night()
        movement = has_movement()
        on_light = (night and movement)
        
        #print(f"controler: {night} {movement}")
        
        global last_time
        now = time.time()
        if on_light: 
            last_time = now
        delta_time = now - last_time
        
        if delta_time <= TIME_ON:
            reles8.set_pin_state(PIN_RELE,True)
        else:
            reles8.set_pin_state(PIN_RELE,False)
            
    except Exception as e:
                log.error(f"Error  {e}") 
    
def is_night():
    datas = database.fetch_last_10_rows()
    true_condition_count = 0
    for data in datas:
        if data["luminosity"] and data["luminosity"]<= LUX_LIMIT:
            true_condition_count += 1
    
    is_night = (true_condition_count >= READS_TO_NIGHT)
    return is_night

def has_movement():
    datas = database.fetch_last_10_rows()
    true_condition_count = 0
    for data in datas:
        if data["pasive_ir"]:
            true_condition_count += 1
    
    has_movement = (true_condition_count >= READS_TO_MOVEMENT)
    return has_movement