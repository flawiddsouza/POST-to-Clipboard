from flask import Flask, request
import pyperclip

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_to_clipboard():
    data = request.form.get('data')
    pyperclip.copy(data)
    return 'Copied to Clipboard'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, threaded=True)