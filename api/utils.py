import json


def load_topics() -> list:
    with open("channels.json",'r') as channels:
            currents = json.load(channels)
            channels.close()
    return list(currents["channels"])
