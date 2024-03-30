
from kafka import KafkaProducer
import pandas as pd
import json

producer = KafkaProducer(
    bootstrap_servers='sincere-urchin-11015-us1-kafka.upstash.io:9092',
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username='c2luY2VyZS11cmNoaW4tMTEwMTUkeO8taxsDgNacDWzlISDj-p3p002Gl4NzH1M',
    sasl_plain_password='NzRhZDFmODgtZWVjZC00ODAyLWJiY2YtZmI0ODY2ZjM2YjE4',
    api_version_auto_timeout_ms=100000,    
)

tracks = pd.read_csv('tracks.csv')

for dt in tracks.to_dict(orient='records'):
    data = json.dumps(dt).encode('utf-8')

    try:
        result = producer.send('tracks', data).get(timeout = 60)    
        print("Message produced:", result)
    except Exception as e:
        print(f"Error producing message: {e}")
producer.close()