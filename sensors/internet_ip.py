import subprocess
import os

def get_local_ip():
    try:
        result = subprocess.check_output(['hostname', '-I'])
        local_ip = result.decode('utf-8').strip()
        return local_ip
    except subprocess.CalledProcessError as e:
        print(f"Error obteniendo IP local: {e}")
        return None

def check_internet_connection():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        if result.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error comprobando conexión a Internet: {e}")
        return False


def read_loop(data,running):
     while running():
        try:
            data["ip_local"] = get_local_ip()
            data["internet"] = check_internet_connection()
        except:
            log.debug("Error IP - INTERNET")
            data["ip_local"] = None
            data["internet"] = False

        finally:
            time.sleep(0.5)

