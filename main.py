import time
import csv

def main():
    recipe_file = "recipes.csv"
    add_recipe_input_file = "add_recipe_input.txt"
    remove_recipe_input_file = "remove_recipe_input.txt"
    search_recipe_input_file = "search_recipe_input.txt"
    search_recipe_output_file = "search_recipe_output.txt"

    while True:
        restart = False
        print("\nPress ENTER to see contents of the recipe book")
        print("1 to add a recipe")
        print("2 to remove a recipe (cannot be undone)")
        print("3 to search a recipe")
        print("0 to exit the program\n")
        user_input = input("Please enter a command: ")

        if user_input == "":
            with open(recipe_file, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    print(f'\nRecipe: {row[0]}')
                    print('Ingredients:')
                    for ingredient in row[1].strip('[]').split(','):
                        print(f'- {ingredient.strip()}')
                    print('Instructions:')
                    for instruction in row[2].strip('[]').split(','):
                        print(f'- {instruction.strip()}')
                    print()

        elif user_input == "1":
            while True:
                recipe_name = input("Enter the name of the recipe (or 'back' to go back): ")
                if recipe_name.lower() == 'back':
                    break
                with open(recipe_file, 'r') as file:
                    reader = csv.reader(file, delimiter=';')
                    for row in reader:
                        if row[0] == recipe_name:
                            replace = input("This recipe already exists. Do you want to replace it? (yes/no): ")
                            if replace.lower() != 'yes':
                                restart = True
                                break
                    if restart:
                        break
                    ingredients = input("Enter the ingredients of the recipe separated by commas (or 'back' to go back): ")
                    if ingredients.lower() == 'back':
                        continue
                    instructions = input("Enter the instructions of the recipe separated by commas (or 'back' to go back): ")
                    if instructions.lower() == 'back':
                        continue
                    with open(add_recipe_input_file, 'w') as file:
                        file.write(f'{recipe_name};{ingredients};{instructions}')
                    break

        elif user_input == "2":
            recipe_name = input("Enter the name of the recipe to remove: ")
            with open(remove_recipe_input_file, 'w') as file:
                file.write(recipe_name)

        elif user_input == "3":
            recipe_name = input("Enter the name of the recipe to search: ")
            with open(search_recipe_input_file, 'w') as file:
                file.write(recipe_name)
            time.sleep(2)
            with open(search_recipe_output_file, 'r') as file:
                print(file.read())

        elif user_input == "0":
            break

        else:
            print("Invalid input. Please try again.")

        if restart:
            continue

if __name__ == "__main__":
    main()