from application import app
from model.repository import MovieRepository
from model.entity import Movie
from flask import request

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    movies = repository.findAll() # la lista tiene las peliculas en forma de diccionario
    response = [] 
    for movie in movies: # recorre las peliculas que se encuentran como un diccionario y las almacena en una lista 
        response.append(movie.toDic()) 
    return response, 200

@app.route("/api/movie/<code>", methods=["GET"])
def findByCode(code):
    movie = repository.findByCode(code) #solo obtine un elemento que mediante el metodo toDic se convierte de objeto a diccionario
    return movie.toDic(), 200

@app.route("/api/movies", methods=["POST"])
def create():
    code = request.json["code"]
    name = request.json["name"]
    image = request.json["image_url"]
    year = request.json["year"]

    movie = Movie(code, name, image_url=image, year=year)
    repository.insert(movie)

    return "{'message': 'Muy bien'}", 201