import threading
from workers import api_worker
from workers import TopicReader
from api.utils import load_topics

topics = load_topics()
print(topics)
for topic in topics:
    reader_thread = threading.Thread(name=f"{topic}_rether", target=TopicReader(topic))
    reader_thread.start()

thread = threading.Thread(name="flask", target=api_worker)

thread.start()


