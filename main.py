import threading
from workers import mqtt_connect
from api.utils import load_topics
from api import app

topics = load_topics()

api_thread = threading.Thread(name=f"api", target=app.run)
api_thread.start()

for topic in topics:
    reader_thread = threading.Thread(name=f"{topic}_reader", target=mqtt_connect, args=(topic,))
    reader_thread.start()



