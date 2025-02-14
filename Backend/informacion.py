from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/informacion', methods=['GET'])
def info():
    return jsonify({
        'nombre': 'Manolo Ricardo Ramirez Mazariegos',
        'carnet': '201503933'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)