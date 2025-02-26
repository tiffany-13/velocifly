#luggage_meal.py

#Create empty list
global luggage_list, luggage_prices
luggage_list = []
luggage_prices = []

#Set fixed luggage price rate
luggage_rate = 4

import guest_detail
#Ask user luggage purchase + validation + confirmation + save luggage purchase
def ask_luggage():
    """Handles luggage selection with progress saving."""
    while True:
        LUGGAGE = input("\nLuggage purchase (0-14 kg) [Enter ONLY numbers within the range 0-14]: ")
        if not LUGGAGE.isdigit():
            print("\nIt should contain ONLY numbers.")
            continue
        elif 0 <= int(LUGGAGE) <= 14:
            result = guest_detail.confirm(f"{LUGGAGE} kg", "luggage allowance purchase")
            if result == "YES":
                guest_detail.add_item(luggage_list, int(LUGGAGE))
                break
            elif result == "NO":
                continue
        else:
            print("It should be within the range 0-14.")

import ticket
#Calculate luggage price
def cal_luggage():
    counter5 = 0
    global total_luggage_price, luggage_prices
    total_luggage_price = 0
    for counter5 in range(ticket.n):
        p_luggage = int(luggage_list[counter5]) * luggage_rate
        luggage_prices.append(p_luggage)
        total_luggage_price += p_luggage
#_____________________________________________________________________________
#Create empty list
global meal, meal_prices
meal_list = []
meal_prices = []

#Set the menu details
menu_food = [["Food","Price (RM)"],["[N]asi Lemak", "7.00"], ["[H]ainanese Chicken Rice", "6.50"],["[K]olo Mee", "6.00"],["[M]ee Jawa", "7.50"]]
menu_drink = [["Drink","Price (RM)"],["[T]eh Tarik", "3.00"], ["[L]emon Tea", "2.00"], ["Ko[P]i", "2.50"],["Mineral [W]ater", "1.50"],["N[O]ne", "0.00"]]

#Set the price of each food or drink
menu = {"N":7, "H":6.50, "K":6, "M":7.50, "T":3, "L":2, "P":2.50, "W":1.50,"O":0.00}

#Set the list of food & drink
menu_list = ["N", "H", "K", "M","T","L","P","W","O"]

#Set shortform of food & drink to respective name
global menu_names
menu_names = {"N":"Nasi Lemak", "H":"Hainanese Chicken Rice", "K":"Kolo Mee", "M":"Mee Jawa","T":"Teh Tarik","L":"Lemon Tea","P":"Kopi","W":"Mineral Water","O":"None"}

#Print menu
def print_menu():
    print ("\n~~~~~~~~~~~~ Menu ~~~~~~~~~~~~~~")
    for row in menu_food:
      print(f"{row[0]:<25} {row[1]:<10}")
    print("\n")        
    for row in menu_drink:
      print(f"{row[0]:<25} {row[1]:<10}")

#Ask user meal + validation + confirmation + save meal
def ask_meal():
    """Handles meal selection with progress saving."""
    while True:
        MEAL = input("\nMeal preference [Enter the alphabet in []. Separate your order with commas.]: ")
        MEAL = [item.strip().upper() for item in MEAL.split(",")]
        checker_meal = True
        meal_current_guest = []
        for item in MEAL:
            if item in menu_list:
                meal_current_guest.append(item)
            else:
                print(f"Invalid food/drink: {item}. Please recheck.")
                checker_meal = False
        if checker_meal:
            result = guest_detail.confirm(', '.join([menu_names[item] for item in meal_current_guest]), "meal order")
            if result == "YES":
                guest_detail.add_item(meal_list, meal_current_guest)
                break
            elif result == "NO":
                continue
#Calculate meal price
def cal_meal():  
    global total_meal_price, meal_prices  
    
    # Reset meal prices list  
    meal_prices.clear()  
    total_meal_price = 0  
    
    # Ensure meal_list has the same length as the number of tickets  
    while len(meal_list) < len(ticket.flightclass):  
        meal_list.append([])  # Add empty list for passengers without meal selection  
    
    # Calculate meal price for each passenger  
    for counter5 in range(len(ticket.flightclass)):  
        # If no meal selected, set price to 0  
        if not meal_list[counter5]:  
            meal_prices.append(0)  
            continue  
        
        # Calculate meal price  
        try:  
            p_meal = sum([menu[item] for item in meal_list[counter5]])  
            meal_prices.append(p_meal)  
            total_meal_price += p_meal  
        except KeyError as e:  
            print(f"Warning: Invalid meal code {e} for passenger {counter5 + 1}")  
            meal_prices.append(0)

def cal_luggage():  
    global total_luggage_price, luggage_prices  
    
    # Reset luggage prices list  
    luggage_prices.clear()  
    total_luggage_price = 0  
    
    # Ensure luggage_list has the same length as the number of tickets  
    while len(luggage_list) < len(ticket.flightclass):  
        luggage_list.append(0)  # Add 0 kg for passengers without luggage selection  
    
    # Calculate luggage price for each passenger  
    for counter4 in range(len(ticket.flightclass)):  
        # Calculate luggage price based on weight  
        if luggage_list[counter4] == 0:  
            luggage_prices.append(0)  
        elif luggage_list[counter4] <= 7:  
            luggage_prices.append(50)  
        else:  
            luggage_prices.append(50 + (luggage_list[counter4] - 7) * 10)  
        
        # Update total luggage price  
        total_luggage_price += luggage_prices[counter4]