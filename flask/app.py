from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__)
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/")
def index():
    return "Flask Server!"

api.add_resource(HelloApiHandler, '/flask/hello')

if __name__ == "__main__":
    app.run()