from flask import Flask
import json
from flask import request, jsonify
from os.path import isfile
from flask.json import load
from .utils import load_topics
from workers import mqtt_connect
import threading

app = Flask(__name__)

# Disable app reloader to avoid errors 
app.use_reloader = False

@app.route("/subscribe/", methods=["POST"])
def subscribe_to_channel():
    new_channel = request.get_json().get("channel")
    if isfile("channels.json"):
        currents = load_topics()
        if new_channel in currents["channels"]:
            return {"error": f"Channel already subscribed to channel {new_channel}"}, 400
        currents["channels"].append(new_channel)
    else:
        currents = {"channels": [new_channel]}
    with open("channels.json", "w") as final:
        json.dump(currents, final)
        final.close()
    # Create new thread to manage new topic
    reader_thread = threading.Thread(name=f"{new_channel}_reader", target=mqtt_connect, args=(new_channel,))
    reader_thread.start()
    return {"data": f"Subscribed to channel {new_channel}"}, 200
