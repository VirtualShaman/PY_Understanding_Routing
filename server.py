from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Dojo')
def dojo():
    return 'Dojo!'

@app.route('/Hi/<string:name>/')
def hi(name):
    return f'Hi {name}'

@app.route('/Hi/repeat/<int:num>/<string:name>/')
def excessiveHi(num, name):
    return f'Hi {name}'*num


if __name__=="__main__":

    app.run(debug=True)

