# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def hello():
# 	return "Hello World!"

# @app.route('/cache-me')
# def cache():
# 	return "nginx will cache this response"

# @app.route('/info')
# def info():

# 	resp = {
# 		'connecting_ip': request.headers['X-Real-IP'],
# 		'proxy_ip': request.headers['X-Forwarded-For'],
# 		'host': request.headers['Host'],
# 		'user-agent': request.headers['User-Agent']
# 	}

# 	return jsonify(resp)

# @app.route('/flask-health-check')
# def flask_health_check():
# 	return "success"

from flask import Flask

# create the extension

# create the app
def create_app():
    app = Flask(__name__,template_folder='templates')
    from home.routes import home_blueprint

    app.register_blueprint(home_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",port=5001, debug=True)