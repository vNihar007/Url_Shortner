from collections import defaultdict 
from datetime import datetime ,timedelta ,timezone
from threading import Lock 

# Storing IP -> TimeStamps 
request_logs = defaultdict(list)
lock  = Lock()

MAX_REQUESTS = 10 
WINDOW_SECONDS = 60 

def is_rate_limited(ip):
    now = datetime.now(timezone.utc)

    with lock : 
        logs = request_logs[ip]
        # remove the ip outside the window--> dict 
        request_logs[ip] = [ts for ts in logs if now -ts <  timedelta(seconds=WINDOW_SECONDS)]

        if len(request_logs[ip]) >= MAX_REQUESTS:
            return True 
        
        request_logs[ip].append(now)
        return False

def reset_limiter():
    with lock:
        request_logs.clear()