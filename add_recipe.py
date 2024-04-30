import csv

recipe_file = "recipes.csv"
input_file = "add_recipe_input.txt"

while True:
    with open(input_file, 'r') as file:
        data = file.readline().strip()
        if data:
            recipe_name, ingredients, instructions = data.split(';')
            lines = []
            with open(recipe_file, 'r') as recipe_file_open:
                reader = csv.reader(recipe_file_open, delimiter=';')
                for row in reader:
                    if row[0] != recipe_name:
                        lines.append(row)
            with open(recipe_file, 'w', newline='') as recipe_file_open:
                writer = csv.writer(recipe_file_open, delimiter=';')
                writer.writerows(lines)
                writer.writerow([recipe_name, ingredients, instructions])
            with open(input_file, 'w') as file:
                file.write('')
