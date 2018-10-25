from flask import Flask,render_template, request
app = Flask(__name__)
import sub
import numpy


@app.route('/')
def hello_world():
  return 'Hey its dfsk application!'

@app.route('/hello')
def hello_world1():
  return  render_template("frontpage.html")



if __name__ == '__main__':
  app.run()
