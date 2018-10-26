from flask import Flask,render_template, request
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
import sub
import os
import numpy
import pandas as pd
from sklearn.preprocessing import StandardScaler



@app.route('/')
def hello_world():
  return  render_template("frontpage.html")

@app.route('/hello', methods = ['POST','GET'])
def hello_world1():
  
  if request.method == 'POST':
    
        f = request.files['file']
        dataset =pd.read_csv('train.csv')
        f.save(secure_filename(f.filename))
        abc=sub.Model(dataset)
        return 'file uploaded successfully'

if __name__ == '__main__':
  app.run()
