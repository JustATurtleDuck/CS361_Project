from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create database connection
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# Create recipes table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS recipes (
             id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             ingredients TEXT NOT NULL,
             instructions TEXT NOT NULL
             )''')
conn.commit()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        c.execute('INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)', (title, ingredients, instructions))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

# Route to view all recipes
@app.route('/view_recipes')
def view_recipes():
    c.execute('SELECT * FROM recipes')
    recipes = c.fetchall()
    return render_template('view_recipes.html', recipes=recipes)

# Route to search for recipes
@app.route('/search_recipes', methods=['GET', 'POST'])
def search_recipes():
    if request.method == 'POST':
        query = request.form['query']
        c.execute("SELECT * FROM recipes WHERE title LIKE ? OR ingredients LIKE ?", ('%' + query + '%', '%' + query + '%'))
        recipes = c.fetchall()
        return render_template('search_results.html', recipes=recipes, query=query)
    return render_template('search_recipes.html')

if __name__ == '__main__':
    app.run(debug=True)
