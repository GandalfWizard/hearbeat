# main.py

import time
from config import SERVICES
from utils import ping_service, check_http_service, get_timestamp
from firebase_client import initialize_firebase, send_to_firebase
from elasticsearch_client import send_to_elasticsearch

initialize_firebase()

if __name__ == "__main__":
    while True:
        for service in SERVICES:
            timestamp = get_timestamp()
            if service["type"] == "ping":
                status, error = ping_service(service["address"])
                response_time = None if error else "N/A"
            elif service["type"] == "http":
                status, response_time = check_http_service(service["address"])
            else:
                continue

            send_to_firebase(service["name"], status, timestamp, response_time)

            #send_to_elasticsearch(service["name"], status, timestamp, response_time)

        time.sleep(60)