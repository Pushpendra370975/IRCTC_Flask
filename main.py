
from flask import Flask
from app.routes.auth import auth
from app.utils.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/irctc'
db.init_app(app)

app.register_blueprint(auth, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
