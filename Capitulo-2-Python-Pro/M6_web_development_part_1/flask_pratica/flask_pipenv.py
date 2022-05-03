from flask import Flask

app = Flask(__name__) #importa o nome do nosso arquivo main como nome da aplicação Flask

@app.route("/") #decorator
def gello_world():
    return "<p>Hello world</p>"

@app.route("/novarota") #decorator(ESTUDAR MAIS)
def novarota():
    return "<h2>Hello world</p>"
    