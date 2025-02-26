# ticket.py

# Create empty list
global flightclass, ticket_prices
flightclass = []
ticket_prices = []

# Initialize the number of tickets to zero
global n
n = 0

# Flight details
Miri = ["[M]iri", 170, "VF2354", "1h 5m", "10:00a.m. - 11:05a.m.", "Non-stop"]
Sibu = ["[S]ibu", 175, "VF3443", "40m", "9:00a.m. - 9:40a.m.", "Non-stop"]
Mukah = ["Mu[K]ah", 200, "VF3465", "1h 5m", "3:00p.m. - 4:05p.m.", "Non-stop"]
Bintulu = ["Bin[T]ulu", 130, "VF7564", "55m", "8:00a.m. - 8:55a.m.", "Non-stop"]
Limbang = ["[L]imbang", 200, "VF5656", "1h 45m", "2:00p.m. - 3:45p.m.", "Non-stop"]
Tanjung_Manis = ["Tan[J]ung_Manis", 122, "VF8544", "45m", "9:30a.m. - 10:15a.m.", "Non-stop"]
Long_Seridan = ["Lon[G]_Seridan", 160, "VF6455", "2h 45m", "12:00p.m. - 2:45p.m.", "Non-stop"]
Bario = ["Ba[R]io", 165, "VF7456", "3h 24m", "8:30a.m. - 11:54a.m.", "Non-stop"]
Long_Sukang = ["L[O]ng_Sukang", 300, "VF1454", "2h 20m", "10:30a.m. - 12:50p.m.", "Non-stop"]
Lawas = ["La[W]as", 250, "VF9456", "2h", "4:00p.m. - 6:00p.m.", "Non-stop"]
Long_Lellang = ["Long_Lell[A]ng", 200, "VF4356", "1h 40m", "8:00a.m. - 9:40a.m.", "Non-stop"]
Long_Semado = ["Long_Sema[D]o", 190, "VF9544", "1h 40m", "9:00a.m. - 10:40a.m.", "Non-stop"]
Marudi = ["Marud[I]", 250, "VF3934", "1h 30m", "11:00a.m. - 12:30p.m.", "Non-stop"]
Mulu = ["M[U]lu", 250, "VF2121", "1h 30m", "7:00a.m. - 8:30a.m.", "Non-stop"]
Ba_Kelalan = ["Ba_K[E]lalan", 220, "VF7024", "1h 40m", "3:30p.m. - 5:10p.m.", "non-stop"]
Long_Akah = ["Long_Aka[H]", 190, "VF5710", "1h 50m", "10:00a.m. - 11:50a.m.", "Non-stop"]
Belaga = ["[B]elaga", 180, "VF3591", "1h", "2:00p.m. - 3:00p.m.", "Non-stop"]
Long_Banga = ["Long_Ba[N]ga", 200, "VF2091", "1h 20m", "8:00a.m. - 9:20a.m.", "Non-stop"]

               
# Set the list of destinations
destination = {
    "M": ["Miri", 170, "VF2354", "1h 5m", "10:00a.m. - 11:05a.m.", "Non-stop"],
    "S": ["Sibu", 175, "VF3443", "40m", "9:00a.m. - 9:40a.m.", "Non-stop"],
    "K": ["Mukah", 200, "VF3465", "1h 5m", "3:00p.m. - 4:05p.m.", "Non-stop"],
    "T": ["Bintulu", 130, "VF7564", "55m", "8:00a.m. - 8:55a.m.", "Non-stop"],
    "L": ["Limbang", 200, "VF5656", "1h 45m", "2:00p.m. - 3:45p.m.", "Non-stop"],
    "J": ["Tanjung_Manis", 122, "VF8544", "45m", "9:30a.m. - 10:15a.m.", "Non-stop"],
    "G": ["Long_Seridan", 160, "VF6455", "2h 45m", "12:00p.m. - 2:45p.m.", "Non-stop"],
    "R": ["Bario", 165, "VF7456", "3h 24m", "8:30a.m. - 11:54a.m.", "Non-stop"],
    "O": ["Long_Sukang", 300, "VF1454", "2h 20m", "10:30a.m. - 12:50p.m.", "Non-stop"],
    "W": ["Lawas", 250, "VF9456", "2h", "4:00p.m. - 6:00p.m.", "Non-stop"],
    "A": ["Long_Lellang", 200, "VF4356", "1h 40m", "8:00a.m. - 9:40a.m.", "Non-stop"],
    "D": ["Long_Semado", 190, "VF9544", "1h 40m", "9:00a.m. - 10:40a.m.", "Non-stop"],
    "I": ["Marudi", 250, "VF3934", "1h 30m", "11:00a.m. - 12:30p.m.", "Non-stop"],
    "U": ["Mulu", 250, "VF2121", "1h 30m", "7:00a.m. - 8:30a.m.", "Non-stop"],
    "E": ["Ba_Kelalan", 220, "VF7024", "1h 40m", "3:30p.m. - 5:10p.m.", "Non-stop"],
    "H": ["Long_Akah", 190, "VF5710", "1h 50m", "10:00a.m. - 11:50a.m.", "Non-stop"],
    "B": ["Belaga", 180, "VF3591", "1h", "2:00p.m. - 3:00p.m.", "Non-stop"],
    "N": ["Long_Banga", 200, "VF2091", "1h 20m", "8:00a.m. - 9:20a.m.", "Non-stop"]}

# Print program name & flight details
def print_start():
    print("~~~~~~~~~~~ VelociFly ~~~~~~~~~~~~\n")
    flight_details = [
        ["Location", "Price(RM)", "Flight Number", "Duration", "Time", "Type"],
        Miri, Sibu, Mukah, Bintulu, Limbang, Tanjung_Manis, Long_Seridan, Bario,
        Long_Sukang, Lawas, Long_Lellang, Long_Semado, Marudi, Mulu, Ba_Kelalan,
        Long_Akah, Belaga, Long_Banga
    ]
    print("~~ Flight Details ~~")
    for row in flight_details:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<15}{row[3]:<11}{row[4]:<25}{row[5]:<15}")

# Ask for destination
def ask_destination():
    """Prompt the user to input the destination alphabet."""
    global destination_key, location
    while True:
        destination_key = input("Where is your flight destination? [Enter alphabet] ").strip().upper()
        if destination_key in destination:
            location = ((destination[destination_key])[0])  # Set location based on the selected destination
            confirm_destination(location)
            break
        else:
            print("Invalid destination. Please check your destination.")

# Confirm flight destination with user
def confirm_destination(destination_shortform):
    global location
    while True:
        confirm_message = f"Confirm {location} as your flight destination? [Enter YES or NO]: "
        confirm_location = input(confirm_message).strip().upper()

        if confirm_location == "NO":
            ask_destination()
            break
        elif confirm_location == "YES":
            break
        else:
            print("\nYour answer should only be YES or NO.")

import ticket
# Print seat availability for the selected destination
def print_seat_availability():
    """Check if the destination exists and print seat availability from the text file."""
    seat_availability_file = "seat_availability.txt"
    global destination_key, location

    while True:
        # Prompt user for destination alphabet
        ask_destination()
        destination_key = destination_key.upper()

        # Fetch seat availability from the text file
        try:
            with open(seat_availability_file, "r") as file:
                lines = file.readlines()

            availability_found = False
            for line in lines:
                if line.strip().lower().startswith(f"destination: {location.lower()}"):
                    availability_found = True
                    print(f"\n~~~~~~~~~~~ Seat Availability for {location} ~~~~~~~~~~~~")
                    for seat_line in lines[lines.index(line) + 1:]:
                        if not seat_line.strip():
                            break
                        print(seat_line.strip())
                    break

            if not availability_found:
                print(f"Error: No seat availability data found for destination {location}.")
            else:
                break

        except FileNotFoundError:
            print(f"Error: {seat_availability_file} not found. Please ensure the file exists.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


def get_destination_key():
    """Retrieve the destination key for the selected destination."""
    global destination_key

    # Ensure destination_key is set
    if not destination_key:
        print("Error: Destination key not set. Please try again.")
        return None

    # Match destination key to its dictionary entry
    for key, value in destination.items():
        if key == destination_key:
            return key

    print("Error: Destination not found in the dictionary.")
    return None

# Check total number of tickets to be purchased
def check_number_ticket():
    global n, seat_availability, location
    if location not in seat_availability:
        print(f"Error: No seat availability data found for destination {destination[destination_key][0]}.")
        return

    seats = seat_availability[location]
    business_seat = seats["business_seat"]
    economy_seat = seats["economy_seat"]

    while True:
        n_input = input("How many tickets (total) do you want to purchase? [Enter the number (integer)]: ")
        try:
            n_input = int(n_input)
        except ValueError:
            print("\nIt should be a number (integer).")
            continue

        total_seats = business_seat + economy_seat

        if n_input == 0:
            print("\nThe total number of tickets cannot be 0.")
        elif n_input <= total_seats:
            n = n_input  # Set the global variable `n`
            break
        elif n_input > total_seats:
            print("\nIt exceeds the number of seats available.")
        else:
            break            

import guest_detail
# Ask user flight class + validation + confirmation + save flight class
def ask_class():
    global seat_availability, location
    seats = seat_availability[location]  # Access seat data for the current destination
    while True:
        CLASS = input("\nFlight class [Enter ECONOMY or BUSINESS]:")        
        if CLASS.strip().upper() == "ECONOMY":
            if seats['economy_seat'] > 0:
                result = guest_detail.confirm (CLASS,"flight class")
                if result == "YES":
                    guest_detail.add_item(flightclass, CLASS.capitalize())
                    break
                elif result == "NO":
                    continue 
            else:
                print("No economy seat available. Please choose business seat.")
                continue
        elif CLASS.strip().upper() == "BUSINESS":
            if seats['business_seat'] > 0:
                result = guest_detail.confirm (CLASS,"flight class")
                if result == "YES":
                    guest_detail.add_item(flightclass, CLASS.capitalize())
                    break
                elif result == "NO":
                    continue
            else:
                print("No business seat available. Please choose economy seat.")
                continue
        else:
            print("\nIt should be either ECONOMY or BUSINESS.")
            continue


#Get the economy price for the chosen destination
def cal_ticket():
    global n
    total_price = 0
    counter4 = 0
    economyp = (destination[destination_key])[1]
    while not counter4 == n:
        #Calculate ticket price based on class and age
        p_ticket = 0
        guest_age = int(guest_detail.get_specific_item_from_list(guest_detail.age, counter4))
        if flightclass[counter4].upper() == "BUSINESS" and (guest_age > 12 and guest_age < 60):
            p_ticket = (1.30 * economyp)  # 130% for business class, age 13-59 
        elif flightclass[counter4].upper() == "BUSINESS" and (guest_age <= 12 or guest_age >= 60):
            p_ticket = (1.26 * economyp)  # 126% for business class, age <= 12 or age>= 60
        elif flightclass[counter4].upper() == "ECONOMY" and (guest_age > 12 and guest_age < 60):  
            p_ticket = economyp  # No discount for economy class, age 13-59
        elif flightclass[counter4].upper() == "ECONOMY" and (guest_age <= 12 or guest_age):
            p_ticket = (0.97 * economyp)  # 97% for economy class, age <= 12 or age>= 60

        #Add the price of this ticket to the total
        total_price += p_ticket

        #Store each ticket price
        ticket_prices.append(p_ticket) 

        #Increment the ticket counter
        counter4 += 1

#Print ticket summary
def print_ticket_summary():
    global location, destination, destination_key
    print("\n~~~~~~~~~~~ VelociFly Ticket Summary ~~~~~~~~~~~")
    print(f"Destination: {destination[destination_key][0]}")
    print(f"Flight Number: {(destination[destination_key])[2]}")
    print(f"Departure Time: {(destination[destination_key])[4]}")
    print(f"Duration: {(destination[destination_key])[3]}")
    print(f"Flight Type: {(destination[destination_key])[5]}")

# Write to text file
def write_seat_availability(filename="seat_availability.txt"):
    """Writes the current seat availability to the file."""
    try:
        with open(filename, "w") as file:
            for destination, seats in seat_availability.items():
                file.write(f"Destination: {destination}\n")
                file.write(f"Business Seat Remaining: {seats['business_seat']}\n")
                file.write(f"Economy Seat Remaining: {seats['economy_seat']}\n")
                file.write("\n")
    except Exception as e:
        print(f"Error writing seat availability file: {e}")

# Read from text file
def read_seat_availability(filename="seat_availability.txt"):
    """
    Reads seat availability from a file and saves it using the full destination name.
    Creates a new file with default values if it doesn't exist.
    """
    global seat_availability

    seat_availability = {}  # Reset to ensure fresh data is loaded
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            current_destination = None

            for line in lines:
                line = line.strip()
                if line.startswith("Destination:"):
                    current_destination = line.split(":")[1].strip()
                    # Use the full destination name as the key
                    seat_availability[current_destination] = {"business_seat": 0, "economy_seat": 0}
                elif line.startswith("Business Seat Remaining:") and current_destination:
                    seat_availability[current_destination]["business_seat"] = int(line.split(":")[1].strip())
                elif line.startswith("Economy Seat Remaining:") and current_destination:
                    seat_availability[current_destination]["economy_seat"] = int(line.split(":")[1].strip())

    except FileNotFoundError:
        print("Seat availability file not found. Creating a default file.")
        create_seat_availability_file(filename)
    except Exception as e:
        print(f"Error reading seat availability file: {e}")
