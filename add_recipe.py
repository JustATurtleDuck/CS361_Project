import csv

recipe_file = "recipes.csv"
input_file = "add_recipe_input.txt"

while True:
    with open(input_file, 'r') as file:
        data = file.readline().strip()
        if data:
            recipe_name, ingredients, instructions = data.split(';')
            with open(recipe_file, 'a', newline='') as recipe_file_open:
                writer = csv.writer(recipe_file_open, delimiter=';')
                writer.writerow([recipe_name, ingredients, instructions])
            with open(input_file, 'w') as file:
                file.write('')