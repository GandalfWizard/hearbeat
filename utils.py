import subprocess
import time
import requests
from datetime import datetime

def ping_service(address):
    try:
        response = subprocess.run(["ping", "-c", "1", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            return "online", None
        else:
            return "offline", None
    except Exception as e:
        return "offline", str(e)

def check_http_service(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        response_time = round((time.time() - start_time) * 1000, 2)  # Response time in ms
        if response.status_code == 200:
            return "online", response_time
        else:
            return "offline", response_time
    except Exception as e:
        return "offline", str(e)

def get_timestamp():
    return datetime.now().isoformat()
