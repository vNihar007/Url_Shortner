from flask import Flask, jsonify
from app.routes.shorten import shorten_bp
from app.routes.redirect import redirect_bp
from app.routes.stats import stats_bp

def create_app():
    app = Flask(__name__,static_folder = '../static') # for the static folder
    app.register_blueprint(shorten_bp)
    app.register_blueprint(redirect_bp)
    app.register_blueprint(stats_bp)
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not Found'}), 404
    
    return app

app = create_app()

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)