import firebase_admin
from firebase_admin import credentials, db
from config import FIREBASE_CREDENTIALS, FIREBASE_DATABASE_URL

def initialize_firebase():
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

def send_to_firebase(service_name, status, timestamp, response_time=None):
    ref = db.reference(f"monitoring/{service_name}")
    data = {
        "timestamp": timestamp,
        "status": status,
        "response_time": response_time if response_time else "N/A"
    }
    ref.push(data)
    print(f"Sent to Firebase: {service_name} - {status} at {timestamp}")
