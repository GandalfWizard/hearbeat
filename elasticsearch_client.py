from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_HOST

es = Elasticsearch(ELASTICSEARCH_HOST)

def send_to_elasticsearch(service_name, status, timestamp, response_time=None):
    data = {
        "service_name": service_name,
        "timestamp": timestamp,
        "status": status,
        "response_time": response_time if response_time else None
    }
    try:
        es.index(index="service-monitoring", document=data)
        print(f"Sent to Elasticsearch: {service_name} - {status} at {timestamp}")
    except Exception as e:
        print(f"Failed to send to Elasticsearch: {e}")
