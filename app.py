from http import HTTPStatus
from flask import flash, request
import sys
from extensions import db
from flask import Flask, jsonify, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_restful import Api
from models.recipe import Recipe
from config import Config

def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)

    routes(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
def routes(app):
    @app.route('/')

    def all():
        all_recipes = Recipe.get_all()
        
        return render_template('index.html', recipes=all_recipes)

    # @app.route('/recipes')

    @app.route('/search')
    def get_by_id():
        rid = request.args.get('search')
        if rid.isdigit():
            rid = int(rid)
            data = Recipe.get_by_id(rid)
            if data is None:
                return  {"Message":" recipe not found"}
            return render_template('search-recipe.html',recipes=data)
        return {"Message":"Entry type should be integer or number"}