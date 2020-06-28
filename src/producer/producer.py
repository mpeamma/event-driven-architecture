from kafka import KafkaProducer
from kafka.errors import KafkaError
import sys
import os

broker = "kafka.kafka.svc.cluster.local" if os.getenv("KAFKA_BROKER") == None else os.getenv("KAFKA_BROKER")
topic = "my-topic" if os.getenv("KAFKA_TOPIC") == None else os.getenv("KAFKA_TOPIC")

num_message = int(sys.argv[1])

producer = KafkaProducer(bootstrap_servers=[broker])

for x in range(0, num_message):
    future = producer.send(topic, b'raw_bytes')
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        log.exception()
        pass

# Successful result returns assigned partition and offset
print ("Successfully produced " + str(num_message) + " messages")
