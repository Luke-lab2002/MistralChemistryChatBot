from flask import Flask, jsonify, request
from rag.generation import generation
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return jsonify({"message": "Hello World!"})

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    #
    conversation_content = data["conversation"]
    print(conversation_content)



    result = generation(conversation_content)

    return jsonify({"message": result})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT", 5000))
