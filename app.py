import os
import pandas as pd
import pickle
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import jsonify

# Allow only CSV input
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # print(request.url)
        # print(request.json())
        returnJSON = jsonify({
            "1": "hope",
            "2": "buy",
            "3": "fun",
            "4": "mother",
            })
        print(returnJSON)
        print("load from file")
        abspathName = os.path.realpath(__file__)
        abspathOnly = os.path.dirname(abspathName)
        modelPath11 = os.path.join(abspathOnly, 'models', 'model_1.pkl')
        pickled_data1 = pickle.load(open(modelPath11, "rb"))
        print("1st pickle")
        print(pickled_data1)
        modelPath12 = os.path.join(abspathOnly, 'models', 'model_2.pkl')
        pickled_data2 = pickle.load(open(modelPath12, "rb"))
        print("2nd pickle")
        print(pickled_data2)
        modelPath13 = os.path.join(abspathOnly, 'models', 'model_3.pkl')
        pickled_data3 = pickle.load(open(modelPath13, "rb"))
        print("3rd pickle")
        print(pickled_data3)
        modelPath14 = os.path.join(abspathOnly, 'models', 'model_4.pkl')
        pickled_data4 = pickle.load(open(modelPath14, "rb"))
        print("4th pickle")
        print(pickled_data4)
        return(returnJSON)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

