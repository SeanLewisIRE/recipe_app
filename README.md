# Recipe App
Recipe app that allows user submissions. 

## Demo
The live site can be found [here](https://recipe-share-app.herokuapp.com/)

## UX
When a user lands on the site homepage, they will be greeted by a tiled grid of recipes that users have input. To add to visual appeal, these display the image associated with the recipe or a placeholder if none is present. 
Users can clict the tile to read information about the recipe and can follow the link displayed to go to the recipe page. 
The recipe page is a simple display of additional recipe information whch includes instructions and ingredients.
Management of recipes and recipe categories is centralised to two pages. Here users can add or delete recipes/categories or, when required, edit specific recipes and categories.

My goal in the design of this website was to make it obvious as to the purpose of the application and keep it simple to use. To achieve this, the [Materialize CSS framework](https://materializecss.com/) was used liberally. The application background is a simple clean white and the tiles contrast with it appropriatly. 
All content is centered to draw used attention and make appropriate use of the space available. This ensures that the application design is uniform across all screen sizes and devices. 


## Features:

**Existing Features** 

  * Mobile-first layout
  * Responsive design
  * Full-stack application
  * User input allowed
  * Data persists
  * Editing of data allowed in-app

**Features Left to Implement**

  * Favories tab, allow users to mark recipe as favorite
  * Search bar

## Technologies
* HTML
* CSS
* JavaScript
* Python (Flask, PyMongo)
* MongoDB

## Testing

**Introduction**\
The application was tested to ensure it was fit for purpose.\
**In Scope** \
The scope of this testing was the project design and functionality.\
**Performance Testing**
* Design/Layout\
To ensure this project maintained it's desired layout the site was tested across multiple browsers (Chrome, Firefox, Microsoft Edge and Safari). 
Using browser developer tools, multiple device sizes were also tested to ensure responsiveness.

* Functionality\
Functionality of this site was tested across a variety of browsers and mobile devices to ensure essential features worked as intended.\
A bug noted during testing was that when editing a recipe, the category would not update with the previous value. This was leading to the recipe category always updating. This bug was addressed and further testing confirmed it was fixed.

**Infastructure**\
The application is a full-stack application built on the frontend using the Materialize CSS framework and the backend using Python, Flask, MongoBD and PyMongo. This fullstack setup allows users to add, edit and delete recipes and recipe categories as required. Data from the MongoDB database is generated dynamically using PyMongo is conjunction with Flask to reduce code replication (DRY programming). This also ensures that the application can scale to accomidate as many recipes as users wish to input. 

## Deployment

This site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch.
A deployed live version of this application is available [here](https://recipe-share-app.herokuapp.com/)

To run locally, you can clone this repository directly into the editor of your choice by pasting 'git clone https://github.com/SeanLewisIRE/recipe_app.git'  into your terminal. 
Required packages can be installed using the included 'requirements.txt' file by typing '$pip3 install -r requirements.txt' into the terminal. Installing these packages will allow for the application to be run locally by typing 'python3 app.py'.
To cut ties with this GitHub repository, type git remote rm origin into the terminal.

## Credits

**Content**
* README layout and content inpired by Code Institute sample, available [here](https://github.com/Code-Institute-Solutions/StudentExampleProjectGradeFive)
* FLASK routing inspired by Code Institute code along turorial. An example of this application is available [here](https://github.com/SeanLewisIRE/task_manager)
* [Materialize CSS framework](https://materializecss.com/) was used to assist in layout/design of application. 

**Media**
* Starter recipes taken from Runnerbeans food blog. Their work can be seen [here](https://www.runnerbeans.co/)
* Default stock image taken from [Pexels](https://www.pexels.com/)