import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect(
    "broker.hivemq.com",
    1883,
    60
)

print("Connected Successfully")

client.disconnect()