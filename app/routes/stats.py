from flask import Blueprint , jsonify , Response 
from app.models import url_store , store_lock , click_stats
import matplotlib
matplotlib.use('Agg') # for the non-gui stats/chart using matplotlib
import matplotlib.pyplot as plt 
import io
from collections import Counter

stats_bp = Blueprint('stats',__name__)

@stats_bp.route('/api/stats/<string:code>',methods=['GET'])
def get_stats(code) :
    with store_lock : 
        entry = url_store.get(code)
        if not entry:  
            return jsonify({'error':'Short code not Found'}), 404 

        response = {
            'url' :entry['url'],
            'clicks' :entry['clicks'],
            'created_at': entry['created_at'].isoformat()
        }
        
        if 'expires_at' in entry: 
            response['expires_at'] = entry['expires_at'].isoformat()

        return jsonify(response),200

@stats_bp.route('/api/stats/<string:code>/chart', methods=['GET'])
def stats_chart(code):
    with store_lock:
        timestamps = click_stats.get(code)
        if not timestamps:
            return jsonify({'error': 'No clicks found'}), 404

        # Group clicks per day
        days = [dt.strftime("%Y-%m-%d") for dt in timestamps]
        daily_counts = Counter(days)

        # Plot
        fig, ax = plt.subplots()
        ax.bar(daily_counts.keys(), daily_counts.values(), color='skyblue')
        ax.set_title(f"Click History for {code}")
        ax.set_ylabel("Clicks")
        ax.set_xlabel("Date")

        # Output image
        buf = io.BytesIO()
        plt.xticks(rotation=45)
        plt.tight_layout()
        fig.savefig(buf, format='png')
        buf.seek(0)

        print("Data used in chart:", daily_counts)
        return Response(buf.getvalue(), mimetype='image/png')
