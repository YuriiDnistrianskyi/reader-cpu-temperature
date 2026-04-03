from os import getenv
from dotenv import load_dotenv

load_dotenv()

PARAMETER = getenv("Parameter")
DEBOUNCE_READ = float(getenv("DEBOUNCE_READ"))

MQTT_BROKER_URL = getenv("MQTT_BROKER_URL")
PRIVATE_NAME = getenv("PRIVATE_NAME")
TOPIC = f"object/{PRIVATE_NAME}/temperature"
