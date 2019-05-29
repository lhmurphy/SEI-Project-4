from app import app
from controllers import books
from controllers import locations, reviews

app.register_blueprint(books.router)
app.register_blueprint(locations.router)
app.register_blueprint(reviews.router)
