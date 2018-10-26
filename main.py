from flask import Flask,render_template, request
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
#import sub
#import numpy



@app.route('/')
def hello_world():
  return  render_template("frontpage.html")

@app.route('/hello', methods = ['POST','GET'])
def hello_world1():
  target = os.path.join(app_root, 'static/')
  if not os.path.isdir(target):
        os.makedirs(target)
  if request.method == 'POST':
    files=request.files['file']
    file_name = files.filename or ''
    destination = '/'.join([target, file_name])
    files.save(destination)
    
  
    return  render_template("frontpage.html")


if __name__ == '__main__':
  app.run()
