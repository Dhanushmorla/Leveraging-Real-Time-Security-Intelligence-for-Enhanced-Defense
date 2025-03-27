import json
import requests
import time
import numpy as np
from sklearn.ensemble import IsolationForest

def fetch_security_data():
    """Simulate fetching real-time security data"""
    try:
        threat_scores = np.random.randint(0, 100, 50).tolist()  # Generate random threat scores
        return {"threat_scores": threat_scores}
    except Exception as e:
        print(f"Failed to fetch security data: {e}")
        return None

def train_anomaly_model(data):
    """Train an Isolation Forest model for anomaly detection"""
    if not data:
        print("No data available for training the model.")
        return None
    try:
        model = IsolationForest(contamination=0.05, random_state=42)
        np_data = np.array(data).reshape(-1, 1)
        model.fit(np_data)
        return model
    except Exception as e:
        print(f"Error training anomaly detection model: {e}")
        return None

def detect_anomalies(model, data):
    """Detect anomalies in security data"""
    if model is None or not data:
        print("Model is not trained or data is empty.")
        return []
    try:
        np_data = np.array(data).reshape(-1, 1)
        predictions = model.predict(np_data)
        anomalies = [data[i] for i in range(len(predictions)) if predictions[i] == -1]
        return anomalies
    except Exception as e:
        print(f"Error detecting anomalies: {e}")
        return []

def main():
    print("Starting real-time security intelligence system...")
    while True:
        security_data = fetch_security_data()
        if security_data and "threat_scores" in security_data:
            model = train_anomaly_model(security_data["threat_scores"])
            anomalies = detect_anomalies(model, security_data["threat_scores"])
            if anomalies:
                print(f"ALERT: {len(anomalies)} anomalies detected!")
                print("Anomalies:", anomalies)
        else:
            print("No valid security data received.")
        time.sleep(10)  # Fetch data every 10 seconds for testing

if __name__ == "__main__":
    main()