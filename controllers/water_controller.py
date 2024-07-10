# Ligths on controller
from actuators import reles8
from modules import database
import time
from datetime import datetime
import logging

log = logging.getLogger(__name__)

PIN_RELE = 20
READS_TO_WET = 5

START_TIME_1 = time(22, 0)   # 22:00
END_TIME_1 = time(22, 5)     # 22:05 (5 minutos después)
START_TIME_2 = time(8, 0)    # 08:00
END_TIME_2 = time(8, 5)      # 08:05 (5 minutos después)

# LOGIC: if is time (2 times at day) start irrigate for 1 minute (except is wet)
last_time = time.time()

def run():
    try:
        wet = is_wet()
        irrigate_time = is_time()
        irrigate = (not wet and irrigate_time)
        
        print(f"controler: {wet} {irrigate_time}-> {irrigate}")
        
        if irrigate:
            reles8.set_pin_state(PIN_RELE,True)
            log.debug("🌱💧💧💧")
        else:
            reles8.set_pin_state(PIN_RELE,False)
            
    except Exception as e:
                log.error(f"Error  {e}") 

def is_time():
    now = datetime.now().time()
    
    # IN first range?
    if START_TIME_1 <= now <= END_TIME_1:
        return True
    
    # IN second range?
    elif START_TIME_2 <= now <= END_TIME_2:
        return True
    
    return False

def is_wet():
    datas = database.fetch_last_10_rows()
    true_condition_count = 0
    for data in datas:
        if data["humidity_ground"]:
            true_condition_count += 1
    
    wet = (true_condition_count >= READS_TO_WET)
    return wet