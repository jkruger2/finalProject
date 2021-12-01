from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return{"username": "iShot#21899"}
    def post(self):
        return{"data":"Posted"}

api.add_resource(HelloWorld, "/helloworld")

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes
