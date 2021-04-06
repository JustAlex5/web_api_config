from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["ENV"]='staging'
api=Api(app)




if app.config["ENV"] == "staging":

    app.config.from_object("config.StagingConfig")

elif app.config["ENV"] == "dev":

    app.config.from_object("config.DevConfig")

else:

    app.config.from_object("config.ProductionConfig")


from app import views