from app import app
from controllers import books, locations, reviews, auth

app.register_blueprint(books.router)
app.register_blueprint(locations.router)
app.register_blueprint(reviews.router)
app.register_blueprint(auth.router)
