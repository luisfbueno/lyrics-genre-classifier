from flask import Flask,request,jsonify
from sklearn.externals import joblib
import string
from nltk.corpus import stopwords
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/",methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            lyric = [data['Lyrics']]

            svm = joblib.load("./svc.pkl")
        except ValueError:
            return jsonify("Please enter a Text.")

        resp = svm.predict(lyric).tolist()
        print(resp)
        return jsonify(resp)

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

if __name__ == '__main__':
    app.run(debug=True)
