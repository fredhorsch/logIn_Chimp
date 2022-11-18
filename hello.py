from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/login", methods=['POST'])
def login():

    content = request.get_json(force=True) # getting json from the request

    # this is what we get form the frontend/browser
    # {
    #   "username": "Frederic"
    #   "password": "123"
    # }

    if not 'username' in content or not 'password' in content:
        return 'Not working'

    liste = {}

    liste['frederic'] = '123'
    liste['hans'] = '456'

    # liste = { 'frederic : '123', 'hans': '456' }

    for username in liste: # go through each user in the list and store the key in the varaiable username, e.g. username becomes the string frederic

        if username == content['username'] and liste[username] == content['password']: # Check here whether the current username, e.g. Frederic, is the same as the request. If so, then go on and check whether the password of the user from the list is the same as the password from the request.
            return 'ok'


    return 'wrong' # after the for loop, send back false.

