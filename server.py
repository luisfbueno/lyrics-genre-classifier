from flask import Flask
from flask import request
from flask import jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords

app = Flask(__name__)

def processamento_texto(txt):
    # remover quebras de linha
    txt = txt.replace('\n',' ')
    # remover símbolos de pontuação, resultando em um array de caracteres
    txt = [char for char in txt if char not in string.punctuation]
    # depois, juntar os caracteres em palavras novamente e separá-los em uma lista de tokens
    txt = ''.join(txt).split()
    # por fim, remover as stopwords da lista
    txt = [word for word in txt if word.lower() not in stopwords.words('portuguese')]

    return txt


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            lyric = [data['Lyrics']]

            svm = joblib.load("./svc.pkl")
        except ValueError:
            return jsonify("Please enter a Text.")

        resp = svm.predict(lyric).tolist()
        print(resp)
        return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
