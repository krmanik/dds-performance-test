import time

from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader, Subscriber

from utils.data_type import Message


class ThroughputTestSubscriber:
    def __init__(self, topic_name: str):
        self.received_samples = 0
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, topic_name, Message)
        self.subscriber = Subscriber(self.participant)
        self.data_reader = DataReader(self.subscriber, self.topic)

    def run(self, duration: float) -> int:
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            samples = self.data_reader.take()
            for sample in samples:
                self.received_samples += 1

        return self.received_samples
