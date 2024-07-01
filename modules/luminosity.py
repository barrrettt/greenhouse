import smbus2
import logging

log = logging.getLogger(__name__)

BH1750FVI_DEVICE = 0x23
ONE_TIME_HIGH_RES_MODE = 0x20

bus = smbus2.SMBus(1)

def convert_to_number(data):
    return (data[1] + (256 * data[0])) / 1.2

def read(addr=BH1750FVI_DEVICE):
    try:
        data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE,2)
        lux = convert_to_number(data)
        log.debug(f": {lux}")
        return lux
    
    except Exception as e:
        log.error(f"Cant read device: {e}")
        return None
    
