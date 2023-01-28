from application import app
from model.repository import ReviewRepository
from model.entity import Review

repository = ReviewRepository()

@app.route("/api/reciewa/movie/<code>", methods=["GET"])
def list(code):
    return repository.findByMovieCode(movie_code=code)

@app.rooute("api/reviews/<id>", methods=["GET"])
def findById(id):
    return repository.findById(id)

@app.route("/api/reviews", methods=["POST"])
def create():
    review = Review(
        id = id
    )
    repository.insert(review)

@app.route("/api/reciews/<id>", methods=["PUT"])
def update(id):
    review = Review()
    repository.update(review)

@app.route("/api/reviews/<id>", methods=["DELETE"])
def delete(id):
    repository.delete(id)