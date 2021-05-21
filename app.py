from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

#creates an instance of the Flask class.
#arguments- static_url_path='' can be used to specify a different path for the static files on the web
#path defaults to the name of the static_folder folder
app = Flask(__name__, static_url_path='', static_folder='frontend/build')

#this line, along with line 3 above, get rid of CORS error 
CORS(app) #comment this on deployment
api = Api(app)


#three lines below - @app.route dectorator tells Flask which URL should trigger our serve(path) function
# send_from_directory allows us to send our "index.html" file from our frontend/build directory
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')

# lines 4, 