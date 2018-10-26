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
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score


@app.route('/')
def hello_world():
  return  render_template("frontpage.html")

@app.route('/hello', methods = ['POST','GET'])

def hello_world1():
  
  if request.method == 'POST':
    
        f = request.files['file']
        dataset =pd.read_csv(f)
        f.save(secure_filename(f.filename))
        bot=sub.Model(dataset)
        
        return render_template("result.html")

      

if __name__ == '__main__':
  app.run()
