# Ligths on controller
from actuators import reles8
from modules import database
from actuators import email
import time
import logging

log = logging.getLogger(__name__)

# LOGIC: send email when local_ip change.

last_time = time.time()
local_ip = None

def run():
    global last_time
    global local_ip
    try:
        datas = database.fetch_last_10_rows()
        ip = datas[0]["ip_local"]
        if ip != local_ip:
            last_time = time.time()
            email.send_email(f'IP LOCAL{ip}')
            local_ip = ip
            log.debug("📧 email enviado ")
            
    except Exception as e:
                log.error(f"Error  {e}") 
