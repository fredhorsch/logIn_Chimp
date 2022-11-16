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
        return 'Geht nicht'

    liste = {}

    liste['frederic'] = '123'
    liste['hans'] = '456'

    # liste = { 'frederic : '123', 'hans': '456' }

    for username in liste: # gehe jeden user in der liste durch und speichere den key in der varaiable username, z.B. username wird zum string frederic
        if username == content['username'] and liste[username] == content['password']: # überprüfe hier ob der aktuelle username z.B. frederic gleich der anfrage ist. Wenn ja, dann gehe weiter und überprüfe ob das passwort vom user aus der liste gleich dem passwort aus der Anfrage ist.
            return 'ok'


    return 'falsch' # nach der for schleife, schicke falsch zurück.



    #dictionaries
    #for schleifen
    #if mit else und not
    #json