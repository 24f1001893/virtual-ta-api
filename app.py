from flask import Flask, request, jsonify
from helper import answer_question

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Virtual TA API is running. Use POST /api/ to ask questions. Can use POSTMAN"

@app.route('/api/', methods=['POST'])  
def answer():
    data = request.get_json(force=True)
    question = data.get("question")
    image_data = data.get("image")

    result = answer_question(question, image_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
