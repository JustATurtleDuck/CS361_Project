# search_by_ingredient.py
import csv

recipe_file = "recipes.csv"
input_file = "search_by_ingredient_input.txt"
output_file = "search_by_ingredient_output.txt"

while True:
    with open(input_file, 'r') as file:
        ingredient = file.readline().strip()
        if ingredient:
            with open(recipe_file, 'r') as recipe_file_open:
                reader = csv.reader(recipe_file_open, delimiter=';')
                with open(output_file, 'w') as output_file_open:
                    for row in reader:
                        if ingredient in row[1]:
                            output_file_open.write(f'Recipe: {row[0]} contains {ingredient}\n')
            with open(input_file, 'w') as file:
                file.write('')