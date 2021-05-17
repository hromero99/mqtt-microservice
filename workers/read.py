import paho.mqtt.client as mqtt
import os


def on_connect(client, user_data, flags, rc):
    # On connect callback for client
    client.subscribe(user_data["topic"])


def on_message(client, userdata, msg):
    # Function for getting message
    print(msg.topic + " " + str(msg.payload))


def mqtt_connect(topic):
    # Function to subscribe into topic
    client = mqtt.Client(userdata={"topic": topic})
    client.connect(host=os.getenv("MQTT_SERVER"), port=1883)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
