import time
from paho.mqtt import client as mqtt_client

from app.config import MQTT_BROKER_URL, PORT, TOPIC

def connect_broker():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
            print("Read and send data ...")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(MQTT_BROKER_URL, PORT)
    return client

def publish_data(client, value):
    value = float(value.split(' ')[0])
    result = client.publish(TOPIC, value)
    if result[0] != 0:
        print(f"Failed to publish data {result}")

