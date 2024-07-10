# Ligths on controller
from actuators import reles8
from modules import database
import time
from datetime import datetime
import logging

log = logging.getLogger(__name__)

PIN_RELE = 20
READS_TO_WET = 5
TIME_ON = 60
TIME_START_1 = "22:00"
TIME_START_2 = "08:00"

# LOGIC: if is time (2 times at day) start irrigate for 1 minute (except is wet)
last_time = time.time()

def run():
    try:
        wet = is_wet()
        irrigate_time = is_time()
        irrigate = (not wet and irrigate_time)
        
        print(f"controler: {wet} {irrigate_time}")
        
        global last_time
        now = time.time()
        if irrigate: 
            last_time = now
        delta_time = now - last_time
        
        if delta_time <= TIME_ON:
            reles8.set_pin_state(PIN_RELE,True)
        else:
            reles8.set_pin_state(PIN_RELE,False)
            
    except Exception as e:
                log.error(f"Error  {e}") 

def is_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    if current_time == TIME_START_1 or current_time == TIME_START_2:
        return True
    else:
        return False

def is_wet():
    datas = database.fetch_last_10_rows()
    true_condition_count = 0
    for data in datas:
        if data["humidity_ground"]:
            true_condition_count += 1
    
    wet = (true_condition_count >= READS_TO_WET)
    return wet