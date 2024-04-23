import csv

recipe_file = "recipes.csv"
input_file = "search_recipe_input.txt"
output_file = "search_recipe_output.txt"

while True:
    with open(input_file, 'r') as file:
        recipe_name = file.readline().strip()
        if recipe_name:
            with open(recipe_file, 'r') as recipe_file_open:
                reader = csv.reader(recipe_file_open)
                for row in reader:
                    if row[0] == recipe_name:
                        with open(output_file, 'w') as output_file_open:
                            output_file_open.write(f'Recipe: {row[0]}\nIngredients:\n' + '\n'.join(row[1:]))
                        break
                else:
                    with open(output_file, 'w') as output_file_open:
                        output_file_open.write('Recipe not found.')
            with open(input_file, 'w') as file:
                file.write('')