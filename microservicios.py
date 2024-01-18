# Importacion de librerias
from flask import Flask, jsonify

# Creacion de una instancia Flask
app = Flask(__name__)

# Definicion ruta microservicio informacion de libros
@app.route('/books_info', methods=['POST'])
def books_info():
    books = [
        {"id": 1, "titulo": "El señor de los anillos", "autor": "J.R.R. Tolkien"},
        {"id": 2, "titulo": "1984", "autor": "George Orwell"},
        {"id": 3, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    ]
    
    return jsonify(books)

# Definicion ruta microservicio informacion de peliculas
@app.route('/movies_info', methods=['POST'])
def movies_info():
    movies = [
        {"id": 1, "titulo": "El Padrino", "director": "Francis Ford Coppola", "anio": 1972},
        {"id": 2, "titulo": "Titanic", "director": "James Cameron", "anio": 1997},
        {"id": 3, "titulo": "Forrest Gump", "director": "Robert Zemeckis", "anio": 1994},
    ]
    return jsonify(movies)

# Ejecucion de la aplicacion
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)