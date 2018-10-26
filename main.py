from flask import Flask,render_template, request
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
import sub
import os
import numpy



@app.route('/')
def hello_world():
  return  render_template("upload.html")

@app.route('/hello', methods = ['POST','GET'])
def hello_world1():
  target = os.path.join(app_root, 'static')
  if not os.path.isdir(target):
        os.makedirs(target)
  if request.method == 'POST':
    
        f = request.files['file']
        
        file_name = f.filename or ''
        destination = '/'.join([target, file_name])
        file.save(destination)
        #f.save(secure_filename(f.filename))
    return 'file uploaded successfully'

if __name__ == '__main__':
  app.run()
