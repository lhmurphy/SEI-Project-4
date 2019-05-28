from app import app
from controllers import books
from controllers import locations

app.register_blueprint(books.router)
app.register_blueprint(locations.router)
