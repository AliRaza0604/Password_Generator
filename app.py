from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    uppercase = request.form.get('uppercase') == 'on'
    lowercase = request.form.get('lowercase') == 'on'
    digits = request.form.get('digits') == 'on'
    special = request.form.get('special') == 'on'
    password = generate_password(length, uppercase, lowercase, digits, special)
    return render_template('result.html', password=password)


def generate_password(length, uppercase, lowercase, digits, special):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


if __name__ == '__main__':
    app.run(debug=True)
