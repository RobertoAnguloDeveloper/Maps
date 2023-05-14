from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, mundo!'

@app.route('/saludo')
def saludo():
    return '¡Hola desde la página de saludo!'

if __name__ == '__main__':
    app.run()
