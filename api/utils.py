import json


def load_topics() -> dict:
    with open("channels.json",'r') as channels:
            currents = json.load(channels)
            channels.close()
    return currents