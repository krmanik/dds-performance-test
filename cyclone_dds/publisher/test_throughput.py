import time

from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.pub import DataWriter, Publisher

from utils.data_type import Message
from typing import List


class ThroughputTestPublisher:
    def __init__(self, topic_name: str, message_count: int, message_size: float, message_rate_hz: int):
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, topic_name, Message)
        self.publisher = Publisher(self.participant)
        self.data_writer = DataWriter(self.publisher, self.topic)
        self.rate = message_rate_hz
        self.num_messages = message_count
        self.message_size = message_size
        self.msg_count = 0
        self.timestamp_list = []

    def publish(self) -> List[float]:
        start_time = time.monotonic()
        for i in range(self.num_messages):
            msg = Message(text="x" * self.message_size, timestamp=time.time())
            self.timestamp_list.append(time.monotonic())
            self.data_writer.write(msg)

            self.msg_count += 1
            time.sleep(1.0 / self.rate)

        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        throughput = self.msg_count / elapsed_time
        print(
            f"Published {self.msg_count} messages in {elapsed_time:.2f} seconds.")
        print(f"Throughput: {throughput:.2f} messages/second.")

    def run(self):
        self.publish()
