from sklearn.externals import joblib
import string
from nltk.corpus import stopwords
from server import server

# Função de processamento de texto utilizada pelo modelo
def processamento_texto(txt):
    txt = txt.replace('\n',' ')
    txt = [char for char in txt if char not in string.punctuation]
    txt = ''.join(txt).split()
    txt = [word for word in txt if word.lower() not in stopwords.words('portuguese')]

    return txt

if __name__ == '__main__':
    flaskServer = server()
    flaskServer.run()
