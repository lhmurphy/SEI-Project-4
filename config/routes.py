from app import app
from controllers import books, locations, reviews, auth

app.register_blueprint(books.router, url_prefix='/api')
app.register_blueprint(locations.router, url_prefix='/api')
app.register_blueprint(reviews.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
