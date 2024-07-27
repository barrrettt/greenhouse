from actuators import reles8
from modules import database
from datetime import datetime, time, timedelta
import logging

log = logging.getLogger(__name__)

PIN_RELE = 16
READS_TO_WET = 5

START_TIME_1 = time(20, 00)  # Start
END_TIME_1 = time(20, 3)     # End
START_TIME_2 = time(8, 0)    # Start2
END_TIME_2 = time(8, 3)      # End2

def run():
    try:
        wet = is_wet()
        irrigate_time = is_time()
        irrigate = irrigate_time #(not wet and irrigate_time)
        
        #log.debug(f"Controller: Wet={wet}, Irrigate={irrigate_time} -> Irrigate={irrigate}")
        
        if irrigate:
            reles8.set_pin_state(PIN_RELE, True)
            log.debug("Starting irrigation 🌱💧")
        else:
            reles8.set_pin_state(PIN_RELE, False)
            
    except Exception as e:
        log.error(f"Error in run function: {e}")

def is_time():
    now = datetime.now().time()
    
    # ¿Estamos en el primer rango horario?
    if START_TIME_1 <= now <= END_TIME_1:
        return True
    
    # ¿Estamos en el segundo rango horario?
    elif START_TIME_2 <= now <= END_TIME_2:
        return True
    
    elif datetime.now().minute %2 == 0:
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
