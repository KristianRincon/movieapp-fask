from MySQLdb import IntegrityError
from application import app
from model.repository import MovieRepository
from model.entity import Movie
from controller.response.api import ApiResponse
from flask import request

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    movies = repository.findAll() # la lista tiene las peliculas en forma de diccionario
    response = [] 
    for movie in movies: # recorre las peliculas que se encuentran como un diccionario y las almacena en una lista 
        response.append(movie.toDic()) 

    api = ApiResponse(data=response)

    return api.toDic(), 200

@app.route("/api/movies/<code>", methods=["GET"])
def findByCode(code):
    api = None
    status = 200
    try:
        movie = repository.findByCode(code) #solo obtine un elemento que mediante el metodo toDic se convierte de objeto a diccionario
        
        api = ApiResponse(data=movie.toDic())
    except Exception as ex:
        status = 400
        api = ApiResponse(message=str(ex))

    return api.toDic(), status

@app.route("/api/movies", methods=["POST"])
def create():
    api = None
    status = 201
    try:
        data = request.get_json(force=True)

        if data.get("code") is None:
            api = ApiResponse(message="El codigo de la pelicula es obligatorio")
            status = 400
        elif data.get("name") is None:
            api = ApiResponse(message="El nombre de la pelicula es obligatorio")
            status = 400
        else:
            if not(isinstance(data.get("code"),str)):
                api = ApiResponse(message="El codigo debe ser una cadena")
                status = 400
            else:
                movie = Movie(
                    data.get("code"), 
                    data.get("name"), 
                    data.get("image_url"),
                    data.get("year"))
                repository.insert(movie)
                api = ApiResponse(True)
    except IntegrityError as ex:
        status = 400
        if ex.args[0] == 1062:
            api = ApiResponse(message="Ya existe una pelicula con este codigo")
        else:
            api = ApiResponse(message=str(ex))
    except Exception as ex:
        status = 400
        api = ApiResponse(message=str(ex))

    return api.toDic(), status