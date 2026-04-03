import time
from paho.mqtt import client as mqtt_client

from app.config import MQTT_BROKER_URL, PORT, TOPIC, PARAMETER

broker = 'broker.hivemq.com'
port = 1883

def connect_broker():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
            print("Read and send data ...")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish_data(client, value):
    result = client.publish(TOPIC, value)
    if result[0] != 0:
        print(f"Failed to publish data {result}")

