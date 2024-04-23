import csv

recipe_file = "recipes.csv"
input_file = "remove_recipe_input.txt"

while True:
    with open(input_file, 'r') as file:
        recipe_name = file.readline().strip()
        if recipe_name:
            lines = []
            with open(recipe_file, 'r') as recipe_file_open:
                reader = csv.reader(recipe_file_open)
                for row in reader:
                    if row[0] != recipe_name:
                        lines.append(row)
            with open(recipe_file, 'w', newline='') as recipe_file_open:
                writer = csv.writer(recipe_file_open)
                writer.writerows(lines)
            with open(input_file, 'w') as file:
                file.write('')