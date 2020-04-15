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

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(
        os.getenv('PORT', '5000')), debug=True)
