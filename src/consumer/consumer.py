from kafka import KafkaConsumer
import time
import os

topic = "my-topic" if os.getenv("KAFKA_TOPIC") == None else os.getenv("KAFKA_TOPIC") 
consumer_group = "my-group" if os.getenv("KAFKA_CONSUMER_GROUP") == None else os.getenv("KAFKA_CONSUMER_GROUP")
broker = "kafka.kafka.svc.cluster.local:9092" if os.getenv("KAFKA_BROKER") == None else os.getenv("KAFKA_BROKER")

consumer = KafkaConsumer(topic,
                         group_id=consumer_group,
                         bootstrap_servers=[broker])
for message in consumer:
    time.sleep(2)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    consumer.commit()
