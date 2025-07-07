from flask import Flask
from database import db
from routes import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # atau sesuai kebutuhan
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(auth_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)