import paho.mqtt.client as mqtt


class TopicReader(object):
    def __init__(self, topic: str) -> None:        
        self.topic = topic
        self.mqtt_connect()
   
    def on_connect(self, client:mqtt, user_data, flags,rc):
        # On connect callback for client
        client.subscribe(self.topic)


    def on_message(self,client, userdata, msg):
        # Function for getting message
        print(msg.topic+" "+str(msg.payload))

    def mqtt_connect(self):
        # Function to subscribe into topic
        client = mqtt.Client()
        client.connect(host="localhost", port=1883)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.loop_forever()
