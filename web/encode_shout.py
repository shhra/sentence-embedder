from flask import Flask, request
import pickle
from sentence_transformers import SentenceTransformer


app = Flask(__name__, instance_relative_config=True)
model_path = 'language_model'
model = SentenceTransformer(model_path)

@app.route('/')
def hello():
    return "Thank you for visiting me. May god bless you!"

@app.route('/encode')
def encode():
    shout = request.args.get('shout')
    value = pickle.dumps(model.encode(shout))
    return value


