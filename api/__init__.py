from  flask import Flask
import json
from flask import request, jsonify
from os.path import isfile

from flask.json import load
from .utils import load_topics
app = Flask(__name__)

# Disable app reloader to avoid errors 
app.use_reloader=False

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
    return {"data": f"Subscribed to channel {new_channel}"}, 200
