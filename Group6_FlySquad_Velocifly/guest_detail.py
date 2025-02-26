#guest_detail.py

#Create empty lists
global name, number, age
name = []
number = []
age = [] 

#Add new item to a list
def add_item(listname, new_item):
    listname.append(new_item)
    
#Return specific list item
def get_specific_item_from_list(listname, index):
    return listname[index]

#Confirmation
def confirm(user_input, category):
    while True:
        confirm_message = "Confirm "+ user_input+ " as your "+ category+ "? [Yes or No]"
        confirm_result = input(confirm_message)
        if confirm_result.strip().upper() == "YES":
            return "YES"
        elif confirm_result.strip().upper() == "NO":
            return "NO"
        else:
            print("\nYour answer should only be YES or No.")
            continue

#Ask user name + validation + confirmation + save name
def ask_name():
    while True:
        NAME = input ("\nName [Enter full name as per IC]: ")
        if not all(char.isalpha() or char.isspace() for char in NAME):
            print ("\nIt should contain ONLY alphabets and spacing.")
            continue
        result = confirm (NAME,"name")
        if result == "YES":
            add_item(name, NAME)
            break
        elif result == "NO":
            continue
                    
#Ask user IC + validation + confirmation + save IC
def ask_IC_number():
    while True:
        NUMBER = input ("\nIC number [Enter ONLY numbers]: ")
        if NUMBER.isdigit() == False:
            print("\nIt should contain ONLY numbers.")
            continue
        if len(NUMBER) != 12:
            print ("It should contain 12 numbers.")
            continue
        result = confirm(NUMBER, "IC number")
        if result == "YES":
            add_item(number, NUMBER)
            break
        elif result == "NO":
            continue
            
#Ask user age + validation + confirmation + save age
def ask_age():
    while True:
        AGE = input ("\nAge[Enter ONLY numbers]:")
        if AGE.isdigit() == False:
            print("\nIt should contain ONLY numbers.")
            continue
        if int(AGE)> 150 or int(AGE)< 0 or AGE == "0":
            print ("It should be between 1 to 150.")
            continue
        result = confirm(AGE, "age")
        if result == "YES":
            add_item(age, AGE)
            break
        elif result == "NO":
            continue

import ticket
import luggage_meal
#Print guest detail summary
def print_guest_summary():
    output = "\nGuest Details:\n"
    output += "------------------------------------------------\n"
    for i in range(len(name)):
        output += f"Guest {i + 1}:\n"
        output += f"  Name: {name[i]}\n"
        output += f"  Age: {age[i]}\n"
        output += f"  IC: {number[i]}\n"
        output += f"  Flight Class: {ticket.flightclass[i]}\n"
        output += f"  Ticket Price: RM {ticket.ticket_prices[i]:.2f}\n"
        output += f"  Meal Preferences: {', '.join([luggage_meal.menu_names[item] for item in luggage_meal.meal_list[i]])}\n"
        output += f"  Meal Total Price: RM {luggage_meal.meal_prices[i]:.2f}\n"
        output += f"  Luggage Weight: {luggage_meal.luggage_list[i]} kg\n"
        output += f"  Luggage Total Price: RM {luggage_meal.luggage_prices[i]:.2f}\n"
    print(output)


def write_guest_details(filename="guest_details.txt"):
    """Writes guest details to a separate file."""
    with open(filename, "a") as file:  # Append to the file instead of overwriting
        file.write("~~~~~~~~~~ Guest Details ~~~~~~~~~~\n")
        min_length = min(len(name), len(number), len(age))
        for i in range(min_length):
            file.write(f"Guest {i + 1}:\n")
            file.write(f"  Name: {name[i]}\n")
            file.write(f"  Age: {age[i]}\n")
            file.write(f"  IC: {number[i]}\n")
            file.write(f"  Flight Class: {ticket.flightclass[i]}\n")
            file.write(f"  Ticket Price: RM {ticket.ticket_prices[i]:.2f}\n")
            file.write(f"  Meal Preferences: {', '.join([luggage_meal.menu_names[item] for item in luggage_meal.meal_list[i]])}\n")
            file.write(f"  Meal Total Price: RM {luggage_meal.meal_prices[i]:.2f}\n")
            file.write(f"  Luggage Weight: {luggage_meal.luggage_list[i]} kg\n")
            file.write(f"  Luggage Total Price: RM {luggage_meal.luggage_prices[i]:.2f}\n\n")

def read_guest_details(filename="guest_details.txt"):
    """Reads guest details from a separate file."""
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No guest details found.")
    except Exception as e:
        print(f"Error reading guest details file: {e}")
















                        

