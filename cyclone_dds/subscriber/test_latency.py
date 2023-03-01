import time

from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader, Subscriber

from utils.data_type import Message


class LatencyTestSubscriber:
    def __init__(self, topic_name: str):
        self.latencies = []
        self.received_messages = 0
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, topic_name, Message)
        self.subscriber = Subscriber(self.participant)
        self.data_reader = DataReader(self.subscriber, self.topic)

    def on_data_available(self):
        for msg in self.data_reader.take():
            if isinstance(msg, Message):
                timestamp = time.time()
                latency = timestamp - msg.timestamp
                self.latencies.append(latency)
                self.received_messages += 1
                print(f"Received message: {msg.text}, with timestamp: {msg.timestamp} Latency: {latency} ns")

    def wait_for_messages(self, count):
        while self.received_messages < count:
            time.sleep(0.1)

    def get_average_latency(self):
        return sum(self.latencies) / len(self.latencies)

    def run(self):
        self.on_data_available()
