from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

# @app.get('/')
# def index_get():
#     return render_template('base.html')


@app.route('/predict/<string:text>')
def predict(text):
    # text = request.get_json().get('message')
    print(text)
    response = get_response(text)
    message = {'response': response}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)
