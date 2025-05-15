class BikeRental:
    def _init_(self):
        self.stock = 10  

    def display_bikes(self):
        print(f"Total bikes available for rent: {self.stock}")

    def rent_bike_hourly(self, n):
        if n <= 0:
            print("Number of bikes should be more than zero.")
            return None
        elif n > self.stock:
            print(f"Sorry! Only {self.stock} bikes are available.")
            return None
        else:
            self.stock -= n
            print(f"You have rented {n} bike(s) on hourly basis.")
            return n

    def return_bike(self, n, hours):
        self.stock += n
        bill = hours * 10 * n
        print(f"Thanks for returning the bike(s). Total bill is: ₹{bill}")


rental = BikeRental()

while True:
    print("\n--- Welcome to Bike Rental System ---")
    print("1. Display available bikes")
    print("2. Rent bike on hourly basis (₹10/hour)")
    print("3. Return bike")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        rental.display_bikes()

    elif choice == '2':
        bikes = int(input("How many bikes would you like to rent? "))
        rental.rent_bike_hourly(bikes)

    elif choice == '3':
        bikes = int(input("How many bikes are you returning? "))
        hours = int(input("How many hours did you keep the bike(s)? "))
        rental.return_bike(bikes, hours)

    elif choice == '4':
        print("Thank you for using the Bike Rental System!")
        break

    else:
        print("Invalid input! Please enter a number from 1 to 4.")