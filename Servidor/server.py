from flask import Flask,request,jsonify
from flask_cors import CORS
from sklearn.externals import joblib

class server():
    def run(self):
        app = Flask(__name__)
        # Habilitar Cross Origin Resource header para conseguir receber o request
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
                return jsonify(resp)

        app.run()
