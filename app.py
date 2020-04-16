import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipie_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:NecfIPUD5PTBlYMe@practicecluster-tjxfj.mongodb.net/recipie_app?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def recipes_page():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)

@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=_recipe)

@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.meal_category.find()
    return render_template("addrecipe.html", categories=categories)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes_page'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=_recipe)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(
        os.getenv('PORT', '5000')), debug=True)
