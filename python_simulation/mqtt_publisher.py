import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883


def publish_data(topic, payload):

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION1
    )

    client.connect(
        BROKER,
        PORT,
        60
    )

    client.publish(
        topic,
        json.dumps(payload)
    )

    print(f"Published -> {topic}")

    client.disconnect()