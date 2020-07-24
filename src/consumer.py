'''消费着 消费主题'''

# encoding:utf8
from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['tqs-admin-event-1']
# 获取 consumer 消费者
consumer = topic.get_simple_consumer(consumer_group="test", reset_offset_on_start=True)
for message in consumer:
    print(message)
    if message is not None:
        print(">>>>>>>>>>", message.offset)
        print(">>>>>>>>>>", message.value)
