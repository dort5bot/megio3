import threading, time, requests, os

KEEP_ALIVE_URL = os.getenv("KEEP_ALIVE_URL")
def ping():
    while True:
        try:
            if KEEP_ALIVE_URL:
                requests.get(KEEP_ALIVE_URL, timeout=10)
        except Exception:
            pass
        time.sleep(300)  # 5 dk

def keep_alive():
    t = threading.Thread(target=ping)
    t.daemon = True
    t.start()
