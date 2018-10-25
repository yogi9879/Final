from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

@app.route('/hello')
def hello_world1():
  return 'Hey its Python Ffflask application!'



if __name__ == '__main__':
  app.run()
