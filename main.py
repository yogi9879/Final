from flask import Flask,render_template, request
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
import ml1
import os
import numpy
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

@app.route('/')
def hello_world():
  return  render_template("index.html")

@app.route('/hello', methods = ['POST','GET'])

def hello_world1():
  
  if request.method == 'POST':
    
        f = request.files['file']
        data=pd.read_csv(f)
        #SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        #json_url = os.path.join(SITE_ROOT, 'static', 'finaldata.csv')
        #data =pd.read_csv(open(json_url))
        #data =pd.read_csv(url_for('static', filename="finaldata"))
        f.save(secure_filename(f.filename))
        
        bot=ml1.model_1(data)
        
        return render_template("result.html",bot=bot)

      

if __name__ == '__main__':
  app.run()
