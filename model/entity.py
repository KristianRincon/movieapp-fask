class Movie:

    def __init__(self, code, name, image_url = None, year = None, ) -> None:
        self.code = code 
        self.name = name
        self.image_url = image_url
        self.year = year

# Creando un metodo que toma el objeto y lo debuelve en forma de diccionario (para que se pueda convertir a Json)
    def toDic(self):
        return {
            "code": self.code,
            "name": self.name,
            "image_url": self.image_url,
            "year": self.year
        }

class Review:

    def __init__(self, name, email, description, rating, movie_code, id = None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.description = description
        self.rating = rating
        self.code = movie_code
        
    def toDic(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "description": self.description,
            "rating": self.rating,
            "code": self.code
        }