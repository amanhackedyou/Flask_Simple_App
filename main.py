from flask import Flask
App = Flask(__name__)
@App.route("/")
def home():
	return "<h1>Aman's Flask App...</h1>"
	
App.run(debug=False, host="0.0.0.0")