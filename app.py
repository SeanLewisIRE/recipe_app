import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
mongo_cluster = os.environ.get('MONGO_CLUSTER_NAME')
mongo_dbname = os.environ.get('MONGO_DB_NAME')
mongo_username = os.environ.get('MONGO_DB_USERNAME')
mongo_password = os.environ.get('MONGO_DB_PASSWORD')
app.config["MONGO_DBNAME"] = mongo_dbname
app.config["MONGO_URI"] = 'mongodb+srv://' + mongo_username + ':' + mongo_password + '@' + mongo_cluster + '-tjxfj.mongodb.net/' + mongo_dbname + '?retryWrites=true&w=majority'
mongo = PyMongo(app)

# 'mongodb+srv://MONGO_DB_USERNAME:MONGO_DB_PASSWORD@MONGO_CLUSTER_NAME-tjxfj.mongodb.net/MONGO_DB_NAME?retryWrites=true&w=majority'

@app.route('/')
def recipes_page():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=_recipe)


@app.route('/manage_recipes')
def manage_recipes():
    recipe = mongo.db.recipes.find()
    categories = mongo.db.meal_category.find()
    return render_template('managerecipes.html', recipes=recipe, categories=categories)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    if request.form.get('recipe_image') != '':
        recipes.insert_one(
            {
                'recipe_name': request.form.get('recipe_name'),
                'recipe_intro': request.form.get('recipe_intro'),
                'ingredients': request.form.get('ingredients'),
                'instructions': request.form.get('instructions'),
                'recipe_image': request.form.get('recipe_image'),
                'category_name': request.form.get('category_name')
            })
    else:
        recipes.insert_one(
            {
                'recipe_name': request.form.get('recipe_name'),
                'recipe_intro': request.form.get('recipe_intro'),
                'ingredients': request.form.get('ingredients'),
                'instructions': request.form.get('instructions'),
                'recipe_image': 'https://images.pexels.com/photos/277253/pexels-photo-277253.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
                'category_name': request.form.get('category_name')
            })
    return redirect(url_for('recipes_page'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    categories = mongo.db.meal_category.find()
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=_recipe, categories=categories)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_intro': request.form.get('recipe_intro'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions'),
        'recipe_image': request.form.get('recipe_image'),
        'category_name': request.form.get('category_name'),
        'is_favorite': request.form.get('is_favorite')
    })
    return redirect(url_for('recipes_page'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('manage_recipes'))


@app.route('/manage_categories')
def manage_categories():
    category = mongo.db.meal_category.find()
    print(category.count())
    return render_template('managecategories.html', categories=category)


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    _category = mongo.db.meal_category.find_one({"_id": ObjectId(category_id)})
    return render_template('editcategory.html', category=_category)


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories = mongo.db.meal_category
    categories.update({'_id': ObjectId(category_id)},
                   {
        'category_name': request.form.get('category_name')
    })
    return redirect(url_for('manage_categories'))


@app.route('/add_category')
def add_category():
    return render_template("addcategory.html")


@app.route('/insert_category', methods=["POST"])
def insert_category():
    categories = mongo.db.meal_category
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('manage_categories'))


@app.route('/delte_category/<category_id>')
def delete_category(category_id):
    mongo.db.meal_category.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('manage_categories'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(
        os.getenv('PORT', '5000')), debug=True)
