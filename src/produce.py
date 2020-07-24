import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

msg_dict = {
    "operatorId":"test",#公交公司ID
    "terminalId":"123",#设备Id
    "terminalCode":"123",#设备编码（使用车辆ID）
    "terminalNo":"1",#同一车辆内terminal序号从1开始
}
msg = json.dumps(msg_dict).encode() #这里加了encode 进行了编码
producer.send('tqs-admin-event-1', msg)
producer.close()
print("结束")
