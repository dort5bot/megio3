import csv
import os
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def log_signal(alarm_type, data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{DATA_DIR}/{alarm_type.lower()}_history.csv"
    new_file = not os.path.exists(file_path)
    row = [datetime.now().isoformat(), alarm_type, data]
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "alarm_type", "data"])
        w.writerow(row)
    # Burada 500 satır sonrası dosya gönderme vb opsiyon eklenebilir

def log_io_signal(data):
    file_path = f"{DATA_DIR}/io_history.csv"
    new_file = not os.path.exists(file_path)
    row = [datetime.now().isoformat(), data.get("total_volume",0), data.get("stable_volume",0)]
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "total_volume", "stable_volume"])
        w.writerow(row)

def log_etf_signal(data):
    file_path = f"{DATA_DIR}/etf_history.csv"
    new_file = not os.path.exists(file_path)
    row = [datetime.now().isoformat(), data]
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "data"])
        w.writerow(row)
