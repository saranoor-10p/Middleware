from distutils.log import debug
from flask import Flask, request
from middleware import Middleware

app = Flask(__name__)

#calling our middleware
app.wsgi_app = Middleware(app.wsgi_app)

@app.route("/")
def hello_world():
    user = request.environ['user']
    return "Hi %s"%user['name']

if __name__ == "__main__":
    app.run(debug=True)
