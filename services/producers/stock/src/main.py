import json
from ensurepip import bootstrap

from kafka import KafkaProducer

from services.producers.stock.src.stock_producer import StockProducer

companies = ["MSFT", "AAPL", "NVDA"]
poll_interval = 75 # in seconds

if __name__ == '__main__':
    print("Stock producer...")
    k = KafkaProducer(
        bootstrap_servers="localhost:9999",
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer = StockProducer(poll_interval, companies, k)
    producer.run()


