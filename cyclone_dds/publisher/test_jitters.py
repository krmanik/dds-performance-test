import time
import random
from typing import List

from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.pub import DataWriter, Publisher

from utils import Message
from utils import JITTER_TEST


class JittersTestPublisher:
    def __init__(self, topic_name: str, message_count: int, interval: float, jitter: float) -> None:
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, topic_name, Message)
        self.publisher = Publisher(self.participant)
        self.data_writer = DataWriter(self.publisher, self.topic)
        self.num_messages = message_count
        self.interval = interval
        self.jitter = jitter
        self.msgs = self.generate_messages()
        self.received_msgs = 0
        self.time_list = []

    def generate_messages(self) -> List[Message]:
        msgs = []
        for i in range(self.num_messages):
            msg = Message(text=f"Message {i}", timestamp=time.time())
            msgs.append(msg)
        return msgs

    def publish(self) -> None:
        for msg in self.msgs:
            delay = self.interval + random.uniform(-self.jitter, self.jitter)
            timestamp = time.time()
            self.time_list.append(timestamp)
            time.sleep(delay)
            self.data_writer.write(msg)
            print(
                f"Published message {msg.text} with timestamp {msg.timestamp} at {timestamp}")

    def calculate_jitters(self) -> float:
        jitter_sum = 0
        for i in range(1, len(self.time_list)):
            jitter = self.time_list[i] - self.time_list[i-1] - self.interval
            jitter_sum += jitter
        return jitter_sum / (len(self.time_list) - 1)

    def run(self) -> None:
        print("Publishing messages...")
        self.publish()
        print(
            f"Published {self.num_messages} messages with a {self.interval} second interval and {self.jitter} jitter.")
        jitter = self.calculate_jitters()
        print(f"Jitter: {jitter} seconds.")
