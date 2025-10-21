from flask import Flask 
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.routes_users import routes_users as users

# Initialize Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(users)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'
db.init_app(app)

# Create database tables
with app.app_context():
    db.drop_all()
    db.create_all()

# Simple route to test the app
@app.route('/')
def index():
    return "<h2>Ir a <a href='/users'>Dashboard de usuarios</a></h2>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
