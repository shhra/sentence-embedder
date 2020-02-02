from flask import Flask, request, jsonify
import numpy as np
from sentence_transformers import SentenceTransformer


app = Flask(__name__, instance_relative_config=True)
model_path = 'language_model'
model = SentenceTransformer(model_path)

@app.route('/')
def hello():
    return "Thank you for visiting me. May god bless you!"

@app.route('/encode', methods=['GET'])
def encode():
    shout = request.get_json()
    value = model.encode(shout['shout'])
    my_val = [val.tolist() for val in value]
    data = {'encodings': my_val}
    return jsonify(data)

    # return pickle.dumps(model.encode(shout))


