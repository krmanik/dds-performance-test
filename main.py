import time
import argparse
from cyclone_dds import LatencyTestPublisher
from cyclone_dds import ThroughputTestPublisher
from cyclone_dds import JittersTestPublisher
from cyclone_dds import LatencyTestSubscriber
from cyclone_dds import ThroughputTestSubscriber
from cyclone_dds import JittersTestSubscriber
from utils import LATENCY_TEST, THROUGHPUT_TEST, JITTER_TEST

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--participant", type=str, default="subscriber",
                        help="Participant name, publisher or subscriber")
    parser.add_argument("--test", type=str, default="latency",
                        help="Test name, latency, throughput, jitters or reliability")
    args = parser.parse_args()

    # ------------------ subscriber -----------------
    # run subscriber test
    # -----------------------------------------------
    if args.participant == "subscriber":
        # run latency test
        if args.test == "latency":
            test_subscriber = LatencyTestSubscriber(LATENCY_TEST)
            while True:
                test_subscriber.run()

        # run throughput test
        if args.test == "throughput":
            test_subscriber = ThroughputTestSubscriber(THROUGHPUT_TEST)
            received_samples = test_subscriber.run(10.0)
            print(f"Received {received_samples} samples in 10 seconds")
        
        # run jitters test
        if args.test == "jitters":
            test_subscriber = JittersTestSubscriber(JITTER_TEST)
            while True:
                test_subscriber.run()

    # ------------------ publisher ------------------
    # run publisher test
    # -----------------------------------------------
    if args.participant == "publisher":
        # run latency test
        if args.test == "latency":
            test_publisher = LatencyTestPublisher(LATENCY_TEST)
            for i in range(10):
                test_publisher.run()
                time.sleep(1)

        # run throughput test
        if args.test == "throughput":
            message_count = 1000
            message_size = 1024
            message_rate_hz = 100
            test_publisher = ThroughputTestPublisher(
                THROUGHPUT_TEST, message_count, message_size, message_rate_hz)
            test_publisher.run()

        if args.test == "jitters":
            message_count = 10
            interval = 0.5
            jitter = 0.1
            publisher = JittersTestPublisher(JITTER_TEST,
                                             message_count, interval, jitter)
            publisher.run()
