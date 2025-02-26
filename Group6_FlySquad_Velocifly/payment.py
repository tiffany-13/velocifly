#payment.py
import guest_detail
import ticket
import luggage_meal
import qrcode
from PIL import Image #to generate and display QR code image

#dictionary of defferent bank details
banks = {
    "1":{"name": "Sarawak Pay", "account": "123-456-789", "holder": "VelociFly Airlines", "qr_text": "https://www.example.com/sarawak_pay_payment"},
    "2":{"name": "Maybank", "account": "456-789-123", "holder": "VelociFly Airlines", "qr_text": "https://www.example.com/maybank_payment"},
    "3":{"name": "Public Bank", "account": "321-987-654", "holder": "VelociFly Airlines", "qr_text": "https://www.example.com/public_bank_payment"},
}

# Function to generate and save a fake QR code for payment
def generate_fake_qr(qr_text):
    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_text) # Use the qr_text argument passed to the function
        qr.make(fit=True)

        # Create an image of the QR code
        qr_img = qr.make_image(fill="black", back_color="white")

        # Save the QR code image to a file
        qr_img.save("fake_qr_payment.png")
        print("Fake QR code for payment saved as 'fake_qr_payment.png'. Check your project directory.")

        # Display the QR code image
        qr_img.show()  # Opens the QR code image for viewing

    except Exception as e:
        print("Error generating QR code:", e)

#Print bank details
def print_bank():
    print("\n~~~~~~~~ Payment Section ~~~~~~~~")
    print("Please select a payment method: ")
    print("1. Sarawak Pay\n2. Maybank\n3. Public Bank")

    while True:
        selection = input("Enter the number for your payment method [1,2 or 3]: ").strip()
        if selection and selection in banks:
            print("\n~~~~~Bank Details~~~~~")
            print(f"Payment Method: {banks[selection]['name']}")
            print(f"Account Number: {banks[selection]['account']}")
            print(f"Account Holder: {banks[selection]['holder']}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

            # Generate and show fake QR code for payment
            generate_fake_qr(banks[selection]["qr_text"])
            break
        else:
            print("Invalid selection. Please select 1,2 or 3.")
            continue
        
#Print total price
def print_total_price():
    total_ticket_price = sum(ticket.ticket_prices)
    overall_total_price = total_ticket_price + luggage_meal.total_luggage_price + luggage_meal.total_meal_price
    print("------------------------------------------------")
    print(f"Total Ticket Price: RM {total_ticket_price:.2f}")
    print(f"Total Luggage Price: RM {luggage_meal.total_luggage_price:.2f}")
    print(f"Total Meal Price: RM {luggage_meal.total_meal_price:.2f}")
    print(f"Overall Total Price: RM {overall_total_price:.2f}")
    return overall_total_price

import tkinter as tk
from tkinter import ttk
import requests

# Fetch exchange rates
def fetch_exchange_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/MYR")  # Replace MYR with your base currency
        response.raise_for_status()
        return response.json().get("rates", {})
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return {}
    
# Print converted price
def exchange():    
    # Create Tkinter root
    root = tk.Tk()
    root.title("Currency Exchange")
    root.geometry("400x300")

    # Fetch total value
    overall_total_price = print_total_price()

    # Display the total price in base currency (MYR)
    total_label = tk.Label(root, text=f"Total Price: RM {overall_total_price:.2f}", font=("Arial", 14))
    total_label.pack(pady=10)

    # Fetch exchange rates
    rates = fetch_exchange_rates()
    
    # Currency selection dropdown
    currency_var = tk.StringVar()
    currency_var.set("ALL")
    currency_dropdown = ttk.Combobox(root, textvariable=currency_var, state="readonly")
    currency_dropdown["values"] = list(rates.keys())
    currency_dropdown.pack(pady=10)
    
    # Display converted price
    converted_label = tk.Label(root, text="Select a currency to see the converted price.", font=("Arial", 12))
    converted_label.pack(pady=10)
    
    def update_price(event):
        selected_currency = currency_var.get().strip()
        print(currency_var.get())
        if selected_currency in rates:
            converted_price = overall_total_price * rates[selected_currency]
            converted_label.config(
                text=f"Price in {selected_currency}: {converted_price:.2f}"
            )
        else:
            converted_label.config(text="Invalid currency selected.")

    # Bind dropdown selection to update the price
    currency_dropdown.bind("<<ComboboxSelected>>", update_price)
    
    # Add a close button
    close_button = tk.Button(root, text="Close", command=root.destroy, bg='#F44336', fg='white')
    close_button.pack(pady=20)

    root.mainloop()

#Confirm Payment
def confirm_pay():
    while True:
        paid = input("\nHave you paid? [YES or NO]: ").strip().upper()
        if paid == "YES":
            dest_key = ticket.destination[ticket.destination_key][0]
            if dest_key in ticket.seat_availability:
                for class_option in ticket.flightclass:
                    if class_option.upper() == "ECONOMY":
                        ticket.seat_availability[dest_key]["economy_seat"] -= 1
                    elif class_option.upper() == "BUSINESS":
                        ticket.seat_availability[dest_key]["business_seat"] -= 1
                # Save the updated seat availability to the file
                ticket.write_seat_availability("seat_availability.txt")
            # Call append_purchase_to_guest_details directly
            append_purchase_to_guest_details()
            print("\nOrder confirmed! Thank you for your payment.")
            break
        elif paid == "NO":
            print("\nPlease complete your payment to proceed.")
            print_bank()
        else:
            print("\nInvalid response. Response should be YES or NO.")

#Confirm order
def confirm_order():
    while True:
        confirm = input("\nConfirm order? [YES or NO]: ").strip().upper()
        if confirm == "YES":
            print_bank()
            confirm_pay()
            break
        elif confirm == "NO":
            delete_record()
            break
        else:
            print("\nInvalid response. Response should be YES or NO.")
            continue
        
#Delete previous record
def delete_record():
    while True:
        delete = input("\nDelete previous progress? [YES or NO]: ").strip().upper()
        if delete == "YES":
            print("\nProgress deleted.")
            from main_module import run_program
            run_program()
            break
        elif delete == "NO":
            print("\nProgress not deleted.")
            confirm_order()
            break
        else:
            print("\nInvalid response. Response should be YES or NO.")
            continue
        
def append_purchase_to_guest_details():
    try:
        # Read progress from purchase_history.txt
        with open("guest_details.txt", "a") as guest_file:
            guest_file.write("\n~~~~~~~~~~ Purchase History ~~~~~~~~~~\n")
            guest_file.write(f"Destination: {ticket.destination[ticket.destination_key][0]}\n")
            guest_file.write(f"Flight Number: {ticket.destination[ticket.destination_key][2]}\n")
            guest_file.write(f"Departure Time: {ticket.destination[ticket.destination_key][4]}\n")
            guest_file.write(f"Duration: {ticket.destination[ticket.destination_key][3]}\n")
            guest_file.write(f"Flight Type: {ticket.destination[ticket.destination_key][5]}\n")
            guest_file.write("Guest Details:\n")
            for i in range(len(guest_detail.name)):
                guest_file.write(f"Guest {i + 1}:\n")
                guest_file.write(f"  Name: {guest_detail.name[i]}\n")
                guest_file.write(f"  IC: {guest_detail.number[i]}\n")
                guest_file.write(f"  Age: {guest_detail.age[i]}\n")
                guest_file.write(f"  Flight Class: {ticket.flightclass[i]}\n")
                guest_file.write(f"  Ticket Price: RM {ticket.ticket_prices[i]:.2f}\n")
                guest_file.write(f"  Meal Preferences: {', '.join([luggage_meal.menu_names[item] for item in luggage_meal.meal_list[i]])}\n")
                guest_file.write(f"  Meal Total Price: RM {luggage_meal.meal_prices[i]:.2f}\n")
                guest_file.write(f"  Luggage Weight: {luggage_meal.luggage_list[i]} kg\n")
                guest_file.write(f"  Luggage Total Price: RM {luggage_meal.luggage_prices[i]:.2f}\n\n")
    except FileNotFoundError:
        with open(guest_file, "w") as guest_file:
            guest_file.write("\n~~~~~~~~~~ Purchase History ~~~~~~~~~~\n")
            guest_file.write(f"Destination: {ticket.destination[ticket.destination_key][0]}\n")
            guest_file.write(f"Flight Number: {ticket.destination[ticket.destination_key][2]}\n")
            guest_file.write(f"Departure Time: {ticket.destination[ticket.destination_key][4]}\n")
            guest_file.write(f"Duration: {ticket.destination[ticket.destination_key][3]}\n")
            guest_file.write(f"Flight Type: {ticket.destination[ticket.destination_key][5]}\n")
            guest_file.write("Guest Details:\n")
            for i in range(len(guest_detail.name)):
                guest_file.write(f"Guest {i + 1}:\n")
                guest_file.write(f"  Name: {guest_detail.name[i]}\n")
                guest_file.write(f"  IC: {guest_detail.number[i]}\n")
                guest_file.write(f"  Age: {guest_detail.age[i]}\n")
                guest_file.write(f"  Flight Class: {ticket.flightclass[i]}\n")
                guest_file.write(f"  Ticket Price: RM {ticket.ticket_prices[i]:.2f}\n")
                guest_file.write(f"  Meal Preferences: {', '.join([luggage_meal.menu_names[item] for item in luggage_meal.meal_list[i]])}\n")
                guest_file.write(f"  Meal Total Price: RM {luggage_meal.meal_prices[i]:.2f}\n")
                guest_file.write(f"  Luggage Weight: {luggage_meal.luggage_list[i]} kg\n")
                guest_file.write(f"  Luggage Total Price: RM {luggage_meal.luggage_prices[i]:.2f}\n\n")

    except Exception as e:
        print(f"An error occurred while appending purchase details: {e}")
    guest_detail.name = []
    guest_detail.number = []
    guest_detail.age = []
    ticket.flightclass = []
    ticket.ticket_prices = []
    ticket.total_price=0
    luggage_meal.luggage_list = []
    luggage_meal.luggage_prices = []
    luggage_meal.total_luggage_price = 0
    luggage_meal.meal_list = []
    luggage_meal.meal_prices = []
    luggage_meal.total_meal_price = 0
