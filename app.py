from flask import Flask, jsonify , render_template, request
from flask_migrate import Migrate
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.routes_users import routes_users as users
from routes.routes_auth import routes_auth as auth
from routes.routes_main import routes_main as main
from routes.routes_hand import routes_hand as hand

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

# Register blueprints
app.register_blueprint(users)
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(hand)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Create database tables
with app.app_context():
    #db.drop_all()
    db.create_all()

# Simple route to test the app

@app.route('/')
def home():
    return render_template('home.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
