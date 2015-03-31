from flask import Blueprint

index = Blueprint('index', __name__)

@index.route("/")
def root():
    return "Index"
