#https://github.com/KieraninTehdas/dht20-sensor
from dht20_sensor.sensor import DHT20Sensor
import logging
import time

log = logging.getLogger(__name__)

# set up
sensor = DHT20Sensor()


def read_loop(data,running):
     while running():
        try:
            t, h = sensor.read()
            log.debug(f"🌡️ {t} - 💧 {h}")
            data["temperature_air"] = t.value
            data["humidity_air"] = h.value
            
        except:
            log.debug("No se puede leer i2c.dht20")
            data["temperature_air"] = None 
            data["humidity_air"] = None 

        finally:
            time.sleep(2)