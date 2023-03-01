import time
from collections import deque

from cyclonedds.domain import DomainParticipant
from cyclonedds.sub import Subscriber, DataReader
from cyclonedds.topic import Topic

from utils.data_type import Message


class JittersTestSubscriber:
    def __init__(self, topic_name, timeout=10):
        self.timeout = timeout
        self.topic_name = topic_name
        self.participant = DomainParticipant()
        self.topic = Topic(self.participant, self.topic_name, Message)
        self.subscriber = Subscriber(self.participant)
        self.data_reader = DataReader(self.subscriber, self.topic)

    def run(self):
        messages = deque(maxlen=1000)
        start_time = time.monotonic()
        count = 0
        while (time.monotonic() - start_time) < self.timeout:
            try:
                msg = self.data_reader.take()
            except KeyboardInterrupt:
                break
            if msg:
                msg = msg[0]
                if isinstance(msg, Message):
                    messages.append((msg.timestamp, time.monotonic()))
                    count += 1

        jitters = []
        last_receive_time = None
        for msg_timestamp, receive_time in messages:
            if last_receive_time is not None:
                jitters.append(receive_time - last_receive_time -
                               (msg_timestamp - last_msg_timestamp))
            last_receive_time = receive_time
            last_msg_timestamp = msg_timestamp

        average_jitter = sum(jitters) / len(jitters) if jitters else 0
        max_jitter = max(jitters) if jitters else 0

        print(f"Jitter Test Results:")
        print(f"-----------------------")
        print(f"Number of messages received: {count}")
        print(f"Average jitter: {average_jitter:.6f} seconds")
        print(f"Maximum jitter: {max_jitter:.6f} seconds")
