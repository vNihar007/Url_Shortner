from textwrap import shorten
from flask import Blueprint , request , jsonify , url_for 
from flask import request
from datetime import datetime 
from app.models import url_store , click_stats ,store_lock
from app.utils import generate_code , is_valid_url ,generate_qr_code
from app.limiter import is_rate_limited
from datetime import datetime , timedelta

shorten_bp = Blueprint('shorten',__name__)

@shorten_bp.route('/api/shorten',methods =['POST'])
def shorten_url():

    ip = request.remote_addr # for rate-limiting of ip  
    if is_rate_limited(ip):
        return jsonify({'error':'Rate limit exceeded . Try again later'}) , 429

    data = request.get_json()
    url = data.get('url')
    expires_in = data.get('expires_in') # in general in seconds 

    if not url or not is_valid_url(url):
        return jsonify({'error':'Invalid URL'}) , 400
    
    code  = generate_code()

    with store_lock:
        while code in url_store:
            code = generate_code()

        entry = {
            'url': url,
            'created_at' : datetime.utcnow(),
            'clicks' :  0
        }

        if expires_in:
            try:
                expires_in = int(expires_in)
                entry['expires_at'] = datetime.utcnow() + timedelta(seconds=expires_in)
            except:
                return jsonify({'error':'expires_in must be an integer'}) , 400

        url_store[code] = entry


    short_url = request.host_url  + code 
    generate_qr_code(short_url,code)

    qr_url = request.host_url + f"static/qr_codes/{code}.png"

    return jsonify({'short_code': code  ,'short_url':short_url, 'qr_code_url':qr_url}) ,200
