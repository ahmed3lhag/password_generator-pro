from flask import Flask, request, jsonify
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    data = request.json
    characters_numbers = int(data['characters'])

    if characters_numbers < 6:
        return jsonify({'error': 'Password should be at least 6 characters long.'}), 400

    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(characters_numbers * 30 / 100)
    part2 = round(characters_numbers * 20 / 100)

    password = []

    for i in range(part1):
        if i < len(s1):
            password.append(s1[i])
        if i < len(s2):
            password.append(s2[i])

    for i in range(part2):
        if i < len(s3):
            password.append(s3[i])
        if i < len(s4):
            password.append(s4[i])

    random.shuffle(password)
    password = "".join(password)

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
