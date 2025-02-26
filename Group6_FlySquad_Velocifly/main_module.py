import tkinter as tk  
from tkinter import ttk, messagebox, simpledialog
import qrcode  
from PIL import Image, ImageTk  
import os  

# Import your custom modules  
import ticket  
import guest_detail  
import luggage_meal  
import payment  

class VelociFlyApp:  
    def __init__(self, master):  
        self.master = master  
        self.master.title("VelociFly Airline Booking System")  
        self.master.geometry("800x600")
        self.master.configure(bg='#c2f1f2')

        # Initialize key variables  
        self.destination = None  
        self.num_tickets = 0  
        self.current_passenger = 0  

        # Create main menu  
        self.create_main_menu()  

    def create_main_menu(self):  
        # Clear any existing widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Main menu frame  
        menu_frame = tk.Frame(self.master, bg='#c2f1f2')  
        menu_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            menu_frame,   
            text="VelociFly Airline Booking System",   
            font=("Helvetica", 16, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=20)  

        # Buttons  
        buttons = [  
            ("Purchase New Ticket", self.start_ticket_purchase),  
            ("View Purchase History", self.view_purchase_history),  
            ("Exit", self.master.quit)
        ]  

        for text, command in buttons:  
            btn = tk.Button(  
                menu_frame,   
                text=text,   
                command=command,  
                width=30,  
                bg='#4CAF50',  
                fg='white',  
                font=("Helvetica", 12)  
            )  
            btn.pack(pady=10)  

    def start_ticket_purchase(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Destination Selection Frame  
        dest_frame = tk.Frame(self.master, bg='#f0f0f0')  
        dest_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            dest_frame,   
            text="Select Your Destination",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Destination Dropdown  
        dest_label = tk.Label(dest_frame, text="Choose Destination:", bg='#f0f0f0')  
        dest_label.pack()  

        # Create destination dropdown  
        destinations = list(ticket.destination.values())  
        dest_names = [dest[0] for dest in destinations]  
        
        dest_var = tk.StringVar()  
        dest_dropdown = ttk.Combobox(  
            dest_frame,   
            textvariable=dest_var,   
            values=dest_names,  
            width=30  
        )  
        dest_dropdown.pack(pady=10)  

        # Confirm Button  
        confirm_btn = tk.Button(  
            dest_frame,   
            text="Confirm Destination",   
            command=lambda: self.confirm_destination(dest_var.get()),  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(pady=10)  

        # Back to Main Menu Button  
        back_btn = tk.Button(  
            dest_frame,   
            text="Back to Main Menu",   
            command=self.create_main_menu,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(pady=10)  

    def confirm_destination(self, selected_destination):  
        if not selected_destination:  
            messagebox.showerror("Error", "Please select a destination")  
            return  

        # Find the key for the selected destination  
        for key, dest_info in ticket.destination.items():  
            if dest_info[0] == selected_destination:  
                ticket.destination_key = key  
                ticket.location = selected_destination  
                break  

        # Proceed to number of tickets selection  
        self.select_number_of_tickets()  

    def select_number_of_tickets(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Number of Tickets Frame  
        tickets_frame = tk.Frame(self.master, bg='#f0f0f0')  
        tickets_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            tickets_frame,   
            text=f"Select Number of Tickets for {ticket.location}",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Seat Availability Display  
        ticket.read_seat_availability()  
        seats = ticket.seat_availability.get(ticket.location, {"business_seat": 0, "economy_seat": 0})  
        
        availability_label = tk.Label(  
            tickets_frame,   
            text=f"Available Seats:\nBusiness: {seats['business_seat']}, Economy: {seats['economy_seat']}",   
            bg='#f0f0f0'  
        )  
        availability_label.pack(pady=10)  

        # Number of Tickets Spinbox  
        tickets_var = tk.IntVar(value=1)  
        tickets_spinbox = tk.Spinbox(  
            tickets_frame,   
            from_=1,   
            to=min(seats['business_seat'] + seats['economy_seat'], 10),  
            textvariable=tickets_var,  
            width=5  
        )  
        tickets_spinbox.pack(pady=10)  

        # Confirm Button  
        confirm_btn = tk.Button(  
            tickets_frame,   
            text="Confirm Number of Tickets",   
            command=lambda: self.proceed_to_passenger_details(tickets_var.get()),  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(pady=10)  

        # Back Button  
        back_btn = tk.Button(  
            tickets_frame,   
            text="Back",   
            command=self.start_ticket_purchase,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(pady=10)  

    def proceed_to_passenger_details(self, num_tickets):  
        # Validate number of tickets  
        ticket.n = num_tickets  
        self.num_tickets = num_tickets  

        # Reset passenger-related lists  
        guest_detail.name.clear()  
        guest_detail.number.clear()  
        guest_detail.age.clear()  
        ticket.flightclass.clear()  

        # Start passenger details input  
        self.current_passenger = 0  
        self.input_passenger_details()  

    def input_passenger_details(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Passenger Details Frame  
        details_frame = tk.Frame(self.master, bg='#f0f0f0')  
        details_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            details_frame,   
            text=f"Passenger {self.current_passenger + 1} Details",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Name Input  
        name_label = tk.Label(details_frame, text="Full Name (as per IC):", bg='#f0f0f0')  
        name_label.pack()  
        name_entry = tk.Entry(details_frame, width=30)  
        name_entry.pack(pady=5)  

        # IC Number Input  
        ic_label = tk.Label(details_frame, text="IC Number (12 digits):", bg='#f0f0f0')  
        ic_label.pack()  
        ic_entry = tk.Entry(details_frame, width=30)  
        ic_entry.pack(pady=5)  

        # Age Input  
        age_label = tk.Label(details_frame, text="Age:", bg='#f0f0f0')  
        age_label.pack()  
        age_entry = tk.Entry(details_frame, width=30)  
        age_entry.pack(pady=5)  

        # Validation and Next Steps  
        def validate_and_proceed():  
            name = name_entry.get().strip()  
            ic = ic_entry.get().strip()  
            age = age_entry.get().strip()  

            # Validate name (only alphabets and spaces)  
            if not all(char.isalpha() or char.isspace() for char in name):  
                messagebox.showerror("Error", "Name should contain only alphabets and spaces")  
                return  

            # Validate IC (12 digits)  
            if not (ic.isdigit() and len(ic) == 12):  
                messagebox.showerror("Error", "IC number must be 12 digits")  
                return  

            # Validate age  
            try:  
                age_num = int(age)  
                if age_num <= 0 or age_num > 150:  
                    messagebox.showerror("Error", "Age must be between 1 and 150")  
                    return  
            except ValueError:  
                messagebox.showerror("Error", "Age must be a number")  
                return  

            # Add details to lists  
            guest_detail.name.append(name)  
            guest_detail.number.append(ic)  
            guest_detail.age.append(age)  

            # Move to next passenger or next step  
            self.current_passenger += 1  
            if self.current_passenger < self.num_tickets:  
                self.input_passenger_details()  
            else:  
                self.select_flight_class()  

        # Buttons  
        btn_frame = tk.Frame(details_frame, bg='#f0f0f0')  
        btn_frame.pack(pady=10)  

        confirm_btn = tk.Button(  
            btn_frame,   
            text="Confirm Details",   
            command=validate_and_proceed,  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(side=tk.LEFT, padx=5)  

        back_btn = tk.Button(  
            btn_frame,   
            text="Back",   
            command=lambda: self.proceed_to_passenger_details(self.num_tickets),  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(side=tk.LEFT, padx=5)  

    def view_purchase_history(self):  
        # Create a new window for purchase history  
        history_window = tk.Toplevel(self.master)  
        history_window.title("Purchase History")  
        history_window.geometry("600x400")  

        # Text widget to display history  
        history_text = tk.Text(history_window, wrap=tk.WORD)  
        history_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  

        # Read and display purchase history  
        try:  
            with open("guest_details.txt", "r") as file:  
                history = file.read()  
                history_text.insert(tk.END, history)  
                history_text.config(state=tk.DISABLED)  
        except FileNotFoundError:  
            history_text.insert(tk.END, "No purchase history found.")  
            history_text.config(state=tk.DISABLED)  
    def select_flight_class(self):  
        # Clear previous widgets  
        self.current_passenger = 0 
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Flight Class Frame  
        class_frame = tk.Frame(self.master, bg='#f0f0f0')  
        class_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            class_frame,   
            text="Select Flight Class",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Seat Availability  
        seats = ticket.seat_availability.get(ticket.location, {"business_seat": 0, "economy_seat": 0})  
        availability_label = tk.Label(  
            class_frame,   
            text=f"Available Seats:\nBusiness: {seats['business_seat']}, Economy: {seats['economy_seat']}",   
            bg='#f0f0f0'  
        )  
        availability_label.pack(pady=10)  

        # Flight Class Selection for each passenger  
        self.current_passenger = 0  
        self.select_individual_flight_class()  

    def select_individual_flight_class(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Flight Class Frame  
        class_frame = tk.Frame(self.master, bg='#f0f0f0')  
        class_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            class_frame,   
            text=f"Flight Class for Passenger {self.current_passenger + 1}",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Seat Availability  
        seats = ticket.seat_availability.get(ticket.location, {"business_seat": 0, "economy_seat": 0})  

        # Flight Class Variable  
        flight_class_var = tk.StringVar()  

        # Radio Buttons for Flight Class  
        economy_radio = tk.Radiobutton(  
            class_frame,   
            text=f"Economy (Available: {seats['economy_seat']})",   
            variable=flight_class_var,   
            value="Economy",  
            bg='#f0f0f0'  
        )  
        business_radio = tk.Radiobutton(  
            class_frame,   
            text=f"Business (Available: {seats['business_seat']})",   
            variable=flight_class_var,   
            value="Business",  
            bg='#f0f0f0'  
        )  
        economy_radio.pack(pady=5)  
        business_radio.pack(pady=5)  

        def validate_flight_class():  
            selected_class = flight_class_var.get()  
            
            if not selected_class:  
                messagebox.showerror("Error", "Please select a flight class")  
                return  

            # Check seat availability  
            if selected_class == "Economy" and seats['economy_seat'] == 0:  
                messagebox.showerror("Error", "No economy seats available")  
                return  
            
            if selected_class == "Business" and seats['business_seat'] == 0:  
                messagebox.showerror("Error", "No business seats available")  
                return  

            # Add flight class to the list  
            ticket.flightclass.append(selected_class)  

            # Move to next passenger or next step  
            self.current_passenger += 1  
            if self.current_passenger < self.num_tickets:  
                self.select_individual_flight_class()  
            else:  
                # Reset passenger counter before meal selection  
                self.current_passenger = 0  
                self.select_meal()   

        # Buttons  
        btn_frame = tk.Frame(class_frame, bg='#f0f0f0')  
        btn_frame.pack(pady=10)  

        confirm_btn = tk.Button(  
            btn_frame,   
            text="Confirm Flight Class",   
            command=validate_flight_class,  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(side=tk.LEFT, padx=5)  

        back_btn = tk.Button(  
            btn_frame,   
            text="Back",   
            command=self.input_passenger_details,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(side=tk.LEFT, padx=5)  

    def select_meal(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Meal Selection Frame  
        meal_frame = tk.Frame(self.master, bg='#f0f0f0')  
        meal_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            meal_frame,   
            text=f"Meal Selection for Passenger {self.current_passenger + 1}",  
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Display Menu  
        def display_menu():  
            menu_text = "Food Menu:\n"  
            for row in luggage_meal.menu_food[1:]:  
                menu_text += f"{row[0]:<25} {row[1]:<10}\n"  
            menu_text += "\nDrink Menu:\n"  
            for row in luggage_meal.menu_drink[1:]:  
                menu_text += f"{row[0]:<25} {row[1]:<10}\n"  
            return menu_text  

        menu_label = tk.Label(  
            meal_frame,   
            text=display_menu(),   
            font=("Courier", 10),   
            justify=tk.LEFT,   
            bg='#f0f0f0'  
        )  
        menu_label.pack(pady=10)  

        # Meal Selection  
        meal_var = tk.StringVar()  
        meal_entry = tk.Entry(meal_frame, width=55)  
        meal_entry.pack(pady=5)  
        meal_entry.insert(0, "Enter meal codes (e.g., N,T for Nasi Lemak and Teh Tarik)")  

        def validate_meal():  
                meal_input = meal_entry.get().strip().upper().split(',')  
                
                # Validate meal selections  
                valid_meals = []  
                for item in meal_input:  
                    if item.strip() in luggage_meal.menu_list:  
                        valid_meals.append(item.strip())  
                    else:  
                        # If no valid meals, use an empty list  
                        valid_meals = []  
                        break  

                # Add meal to the list  
                luggage_meal.meal_list.append(valid_meals)  

                # Move to next passenger or next step    
                self.current_passenger += 1  
                if self.current_passenger < self.num_tickets:  
                    self.select_meal()  
                else:  
                    # Reset passenger counter for luggage selection  
                    self.current_passenger = 0  
                    self.select_luggage()  
 
        # Buttons  
        btn_frame = tk.Frame(meal_frame, bg='#f0f0f0')  
        btn_frame.pack(pady=10)  

        confirm_btn = tk.Button(  
            btn_frame,   
            text="Confirm Meal Selection",   
            command=validate_meal,  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(side=tk.LEFT, padx=5)  

        back_btn = tk.Button(  
            btn_frame,   
            text="Back",   
            command=self.select_flight_class,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(side=tk.LEFT, padx=5)  

    def select_luggage(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Luggage Selection Frame  
        luggage_frame = tk.Frame(self.master, bg='#f0f0f0')  
        luggage_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            luggage_frame,   
            text=f"Luggage Selection for Passenger {self.current_passenger + 1}",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Luggage Weight Spinbox  
        luggage_var = tk.IntVar(value=0)  
        luggage_label = tk.Label(  
            luggage_frame,   
            text="Select Luggage Weight (0-14 kg):",   
            bg='#f0f0f0'  
        )  
        luggage_label.pack(pady=5)  

        luggage_spinbox = tk.Spinbox(  
            luggage_frame,   
            from_=0,   
            to=14,  
            textvariable=luggage_var,  
            width=5  
        )  
        luggage_spinbox.pack(pady=5)  

        def validate_luggage():  
            luggage_weight = luggage_var.get()  
            
            # Add luggage to the list  
            luggage_meal.luggage_list.append(luggage_weight)  

            # Move to next passenger or next step  
            self.current_passenger += 1  
            if self.current_passenger < self.num_tickets:  
                self.select_luggage()  
            else:  
                # Calculate luggage and meal prices  
                luggage_meal.cal_luggage()  
                luggage_meal.cal_meal()  
                
                # Calculate ticket prices  
                ticket.cal_ticket()  
                
                # Proceed to payment  
                self.proceed_to_payment()  

        # Buttons  
        btn_frame = tk.Frame(luggage_frame, bg='#f0f0f0')  
        btn_frame.pack(pady=10)  

        confirm_btn = tk.Button(  
            btn_frame,   
            text="Confirm Luggage",   
            command=validate_luggage,  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(side=tk.LEFT, padx=5)  

        back_btn = tk.Button(  
            btn_frame,   
            text="Back",   
            command=self.select_meal,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(side=tk.LEFT, padx=5)  

    def proceed_to_payment(self):  
        # Clear previous widgets  
        for widget in self.master.winfo_children():  
            widget.destroy()  

        # Payment Frame  
        payment_frame = tk.Frame(self.master, bg='#f0f0f0')  
        payment_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  

        # Title  
        title_label = tk.Label(  
            payment_frame,   
            text="Payment Summary",   
            font=("Helvetica", 14, "bold"),   
            bg='#f0f0f0'  
        )  
        title_label.pack(pady=10)  

        # Calculate and display total prices  
        total_ticket_price = sum(ticket.ticket_prices)  
        total_luggage_price = luggage_meal.total_luggage_price  
        total_meal_price = luggage_meal.total_meal_price  
        overall_total_price = total_ticket_price + total_luggage_price + total_meal_price  

        # Price Summary  
        summary_text = f"""  
        Total Ticket Price: RM {total_ticket_price:.2f}  
        Total Luggage Price: RM {total_luggage_price:.2f}  
        Total Meal Price: RM {total_meal_price:.2f}  
        
        Overall Total Price: RM {overall_total_price:.2f}  
        """  

        summary_label = tk.Label(  
            payment_frame,   
            text=summary_text,   
            font=("Courier", 12),   
            justify=tk.LEFT,   
            bg='#f0f0f0'  
        )  
        summary_label.pack(pady=10)

        # Money exchange button
        money_frame = tk.Frame(payment_frame, bg='#f0f0f0')  
        money_frame.pack(pady=10)

        currency_btn = tk.Button(  
            money_frame,   
            text="Currency Exchange",   
            command=payment.exchange,  
            bg='#4CAF50',  
            fg='white'  
        )  
        currency_btn.pack(side=tk.LEFT, padx=5)

        # Payment Method Selection  
        payment_method_var = tk.StringVar()  
        payment_method_label = tk.Label(  
            payment_frame,   
            text="Select Payment Method:",   
            bg='#f0f0f0'  
        )  
        payment_method_label.pack(pady=5)  

        payment_methods = list(payment.banks.values())  
        payment_method_names = [bank['name'] for bank in payment_methods]  

        payment_dropdown = ttk.Combobox(  
            payment_frame,   
            textvariable=payment_method_var,   
            values=payment_method_names,  
            width=30,  
            state="readonly"  
        )  
        payment_dropdown.pack(pady=5)  

        def generate_qr_and_confirm():  
            selected_method = payment_method_var.get()  
            if not selected_method:  
                messagebox.showerror("Error", "Please select a payment method")  
                return  

            # Find the corresponding bank details  
            selected_bank = next((bank for bank in payment_methods if bank['name'] == selected_method), None)  
            if not selected_bank:  
                messagebox.showerror("Error", "Invalid payment method")  
                return  

            # Generate QR code  
            try:  
                # Create a Toplevel window for QR code  
                qr_window = tk.Toplevel(self.master)  
                qr_window.title(f"QR Code - {selected_method}")  
                qr_window.geometry("600x600")  

                # Generate QR code  
                qr = qrcode.QRCode(  
                    version=1,  
                    error_correction=qrcode.constants.ERROR_CORRECT_L,  
                    box_size=10,  
                    border=4,  
                )  
                qr.add_data(selected_bank['qr_text'])  
                qr.make(fit=True)  

                # Create an image of the QR code  
                qr_img = qr.make_image(fill="black", back_color="white")  
                
                # Convert PIL Image to PhotoImage  
                tk_img = ImageTk.PhotoImage(qr_img)  

                # Display QR code  
                qr_label = tk.Label(qr_window, image=tk_img)  
                qr_label.image = tk_img  # Keep a reference  
                qr_label.pack(pady=10)  

                # Bank Details  
                details_text = f"""  
                Bank: {selected_bank['name']}  
                Account: {selected_bank['account']}  
                Holder: {selected_bank['holder']}  
                """  
                details_label = tk.Label(qr_window, text=details_text)  
                details_label.pack(pady=10)  

                # Confirm Payment Button  
                def confirm_payment():  
                    result = messagebox.askyesno("Confirm Payment", "Have you completed the payment?")  
                    if result:  
                        self.finalize_booking()  
                        qr_window.destroy()  

                confirm_btn = tk.Button(  
                    qr_window,   
                    text="I Have Paid",   
                    command=confirm_payment,  
                    bg='#4CAF50',  
                    fg='white'  
                )  
                confirm_btn.pack(pady=10)  

            except Exception as e:  
                messagebox.showerror("QR Code Error", f"Could not generate QR code: {str(e)}")  

        # Buttons  
        btn_frame = tk.Frame(payment_frame, bg='#f0f0f0')  
        btn_frame.pack(pady=10)  

        confirm_btn = tk.Button(  
            btn_frame,   
            text="Generate Payment QR",   
            command=generate_qr_and_confirm,  
            bg='#4CAF50',  
            fg='white'  
        )  
        confirm_btn.pack(side=tk.LEFT, padx=5)  

        back_btn = tk.Button(  
            btn_frame,   
            text="Back",   
            command=self.select_luggage,  
            bg='#F44336',  
            fg='white'  
        )  
        back_btn.pack(side=tk.LEFT, padx=5)  

    def finalize_booking(self):  
        try:  
            # Update seat availability  
            dest_key = ticket.destination[ticket.destination_key][0]  
            if dest_key in ticket.seat_availability:  
                for class_option in ticket.flightclass:  
                    if class_option.upper() == "ECONOMY":  
                        ticket.seat_availability[dest_key]["economy_seat"] -= 1  
                    elif class_option.upper() == "BUSINESS":  
                        ticket.seat_availability[dest_key]["business_seat"] -= 1  
                
                # Save the updated seat availability  
                ticket.write_seat_availability("seat_availability.txt")  

            # Append purchase details to guest details file  
            self.append_purchase_to_guest_details()  

            # Show success message  
            messagebox.showinfo("Booking Confirmed", "Your booking is complete! Thank you for choosing VelociFly.")

            # Return to main menu  
            self.create_main_menu()  

        except Exception as e:  
            messagebox.showerror("Booking Error", f"An error occurred: {str(e)}")  

    def append_purchase_to_guest_details(self):  
        try:  
            # Open file in append mode  
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

            # Reset all booking-related lists  
            self.reset_booking_data()  

        except Exception as e:  
            messagebox.showerror("File Write Error", f"Could not save purchase details: {str(e)}")  

    def reset_booking_data(self):  
        # Reset all booking-related lists and variables  
        guest_detail.name.clear()  
        guest_detail.number.clear()  
        guest_detail.age.clear()  
        ticket.flightclass.clear()  
        ticket.ticket_prices.clear()  
        ticket.total_price = 0  
        luggage_meal.luggage_list.clear()  
        luggage_meal.luggage_prices.clear()  
        luggage_meal.total_luggage_price = 0  
        luggage_meal.meal_list.clear()  
        luggage_meal.meal_prices.clear()  
        luggage_meal.total_meal_price = 0


def main():  
    root = tk.Tk()  
    app = VelociFlyApp(root)  
    root.mainloop()  

if __name__ == "__main__":  
    main()
