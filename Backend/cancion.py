from flask import Flask, request, jsonify

app = Flask(__name__)

canciones = []

@app.route('/agregar-cancion', methods=['POST'])
def agregar_cancion():
    data = request.json
    nombre = data.get('nombre')
    artista = data.get('artista')
    album = data.get('genero musical')

    nueva_cancion = {
        'nombre': nombre,
        'artista': artista,
        'album': album
    }
    canciones.append(nueva_cancion)

    return jsonify({'mensaje': 'Canción agregada', 'cancion': nueva_cancion}), 201

if __name__ == '__main__':
    app.run(debug=True)