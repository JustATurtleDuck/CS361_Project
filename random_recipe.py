# random_recipe.py
import csv
import random

recipe_file = "recipes.csv"
output_file = "random_recipe_output.txt"

while True:
    with open(recipe_file, 'r') as recipe_file_open:
        reader = csv.reader(recipe_file_open, delimiter=';')
        recipes = list(reader)
        random_recipe = random.choice(recipes)
        with open(output_file, 'w') as output_file_open:
            output_file_open.write(f'\nRecipe: {random_recipe[0]}\n')
            output_file_open.write('Ingredients:\n')
            for ingredient in random_recipe[1].strip('[]').split(','):
                output_file_open.write(f'- {ingredient.strip()}\n')
            output_file_open.write('Instructions:\n')
            for instruction in random_recipe[2].strip('[]').split(','):
                output_file_open.write(f'- {instruction.strip()}\n')