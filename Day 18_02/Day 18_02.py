from flask import flask, Flask

app = Flask(__name__)

client = MongoClient("Mongo://localhost:27017")
db = client {"software_infotech"}
collectin = db["students"]