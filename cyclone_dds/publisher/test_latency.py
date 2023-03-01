import time

from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.pub import DataWriter, Publisher

from utils.data_type import Message


class LatencyTestPublisher:
    def __init__(self, topic_name: str):
        self.topic_name = topic_name
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, topic_name, Message)
        self.publisher = Publisher(self.participant)
        self.data_writer = DataWriter(self.publisher, self.topic)

    def publish(self):
        msg = Message(text="Hello from Publisher", timestamp=time.time())
        start_time = time.monotonic_ns()
        self.data_writer.write(msg)
        end_time = time.monotonic_ns()
        latency = end_time - start_time
        print(f"Published message: {msg.text}, with timestamp: {msg.timestamp} Latency: {latency} ns")

    def run(self):
        self.publish()
