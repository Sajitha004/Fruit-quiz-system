# Import the necessary module(s).
import json



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")



# This function repeatedly prompts for input until a float with a minimum of 0 is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Value must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    with open("data.txt", "w") as file:
        json.dump(data, file, indent=4)


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    with open("data.txt", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Fruit Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 
        
    if choice == 'a':
        # Add a new fruit.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        name = input_something("Enter fruit name: ")
        if any(fruit["name"].lower() == name.lower() for fruit in data):
            print(f'"{name}" already exists in data.')
            continue

        print(f"In 100 grams of {name}, how many...")
        energy = input_float("Calories are there?: ")
        fibre = input_float("Grams of fibre are there?: ")
        sugar = input_float("Grams of sugar are there?: ")
        potassium = input_float("Milligrams of potassium are there?: ")

        data.append({"name": name, "energy": energy, "fibre": fibre, "sugar": sugar, "potassium": potassium})
        save_data(data)
        print("Fruit added!")


    
    elif choice == 'l':
        # List the current fruit.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No fruit saved.")
            continue
        print("List of fruit:")
        for idx, fruit in enumerate(data, start=1):
            print(f"{idx}) {fruit['name']}")



    elif choice == 's':
        # Search the current fruit.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No fruit saved.")
            continue
        term = input_something("Enter search term: ").lower()
        result = [fruit for fruit in data if term in fruit["name"].lower()]
        if result:
            print("Search results:")
            for idx, fruit in enumerate(result, start=1):
                print(f"{idx}) {fruit['name']}")
        else:
            print("No results found.")



    elif choice == 'v':
        # View a fruit.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No fruit saved.")
            continue
        try:
            index = int(input("Fruit number to view: ")) - 1
            if 0 <= index < len(data):
                fruit = data[index]
                print(f"Nutritional information for 100 grams of {fruit['name']}:")
                print(f" Energy: {fruit['energy']} calories")
                print(f" Fibre: {fruit['fibre']} grams")
                print(f" Sugar: {fruit['sugar']} grams")
                print(f" Potassium: {fruit['potassium']} milligrams")
            else:
                print("Invalid index number.")
        except ValueError:
            print("Invalid input.")



    elif choice == 'd':
        # Delete a fruit.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No fruit saved.")
            continue
        try:
            index = int(input("Fruit number to delete: ")) - 1
            if 0 <= index < len(data):
                deleted_fruit = data.pop(index)
                save_data(data)
                print('Fruit deleted.')
            else:
                print("Invalid index number.")
        except ValueError:
            print("Invalid input.")



    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice!")

