from app import app
from controllers import books

app.register_blueprint(books.router)
