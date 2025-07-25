# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata


from threading import Lock 
from datetime import datetime 

url_store = {}
click_stats = {}
store_lock = Lock()
