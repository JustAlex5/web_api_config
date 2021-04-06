from app import app
from flask_restful import Api, Resource

api=Api(app)
class HelloWord(Resource):
    def get(self):
        return{"data":"Hello"+" "+ app.config["TYPE"]}

api.add_resource(HelloWord,"/helloword")