import logging

# Basics
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8'),  # file
        logging.StreamHandler()  # in console
    ]
)

# Crear un logger
logger = logging.getLogger(__name__)
