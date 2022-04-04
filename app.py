from flask import Flask, request, jsonify, render_template, send_from_directory
import os
app = Flask(__name__)


# @app.get('/')
# def index_get():
#     return render_template('base.html')
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'static/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def home():
    return 'Testing of Ubot Fake API'


@app.route('/<string:text>')
def predict(text):
    dict1 = {
        'hi': 'Hello, How can I help you',
        'thanks': 'Welcome',
        'varsity': 'I am study in UAP',
        'uap': 'University Asia Pacific'
    }
    # text = request.get_json().get('message')
    text = text.strip().lower()
    print(text)
    try:
        response = dict1[text]
    except:
        response = 'Empty data'
    message = {'conversation': response}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=False)
