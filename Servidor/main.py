from flask import Flask
from flask import request
from flask import jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from flask_cors import CORS,cross_origin
