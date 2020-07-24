"""这个呢就是简单的查看下broker的信息"""
from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
print(client.brokers)

for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    id = client.brokers[n].id
    print("host=%s | port=%s | broker.id=%s " %(host,port,id))