import logging

log_file_path = '/home/barrrettt/proyectos/barrrettt/greenhouse/app.log'

# Basics
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file_path, encoding='utf-8'),  # file
        logging.StreamHandler()  # in console
    ]
)