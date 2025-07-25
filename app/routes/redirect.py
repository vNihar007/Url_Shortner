from flask import Blueprint ,redirect ,  abort 
from app.models  import url_store , store_lock ,click_stats
from datetime import datetime



redirect_bp = Blueprint('redirect',__name__)

@redirect_bp.route('/<string:code>',methods = ['GET'])
def redirect_code(code):
    with store_lock:
        entry = url_store.get(code)
        if not entry :  
            abort(400)
        # check for expiry 
        if 'expires_at' in entry and datetime.utcnow() >  entry['expires_at']:
           return "Link Expired " , 410 

        # Track clicks 
        entry['clicks'] += 1 
        if code not in click_stats:
            click_stats[code] = []
        click_stats[code].append(datetime.utcnow())
        
        return redirect(entry['url'])