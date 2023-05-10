
items_in_stock = {
    'hourly': 13,
    'daily': 9,
    'weekly': 20
    }

items_rented = {
    'hourly': 0,
    'daily': 0,
    'weekly': 0
    }

class MyBikeShop:
    def __init__(self, items_in_stock):
        self.items_in_stock = items_in_stock
        self.total_cost = 0
        self.revenue = 0
        self.items_rented = items_rented

    def display_stock(self):
        print("Today we have bikes in stock:")
        for key, value in self.items_in_stock.items():
            print(key.title(), value)
        print("Bike rent costs $5 per hour, $20 per day, $60 per week")

    def rent_bike_hourly(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['hourly']:
            print("We don't have enough bikes in stock for hourly rental.")
            return
        rent_time = int(input("For how many hours do you want to rent your bike(s)?"))
        print("Congratulations, you rented", rent_number, 'bikes on an hourly basis.')
        self.items_in_stock['hourly'] -= rent_number
        self.total_cost = rent_number * 5 * rent_time

        self.items_rented['hourly'] += rent_number


    def rent_bike_daily(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['daily']:
            print("We don't have enough bikes in stock for daily rental.")
            return
        rent_time = int(input("For how many days do you want to rent your bike(s)?"))
        print("Congratulations, you rented", rent_number, 'bikes on a daily basis.')
        self.items_in_stock['daily'] -= rent_number
        self.total_cost = rent_number * 20 * rent_time

        self.items_rented['daily'] += rent_number



    def rent_bike_weekly(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['weekly']:
            print("We don't have enough bikes in stock for weekly rental.")
            return
        rent_time = int(input("For how many weeks do you want to rent your bike(s)?"))
        print("Congratulations, you rented", rent_number, 'bikes on a weekly basis.')
        self.items_in_stock['weekly'] -= rent_number
        self.total_cost = rent_number * 60 * rent_time


        self.items_rented['weekly'] += rent_number

    def return_bike(self, rent_type, return_number):
        if rent_type not in self.items_in_stock:
            print("Invalid rent type.")
            return

        if return_number <= 0:
            print("Sorry, wrong number. Choose more than 0 bikes.")
            return

        self.items_in_stock[rent_type] += return_number
        print("You have returned", return_number, 'bikes on', rent_type, "basis")
        if 3 <= rent_number <= 5:
            self.total_cost *= 0.7
            print("It's your lucky day! You can have 30% discount ")
        print("Your bill: $", int(self.total_cost))
        self.revenue += self.total_cost

    def display_revenue(self):
        print("Total revenue:", int(self.revenue))


bike_shop = MyBikeShop(items_in_stock)

while True:
    print("********************************")
    print("Bike Rental Shop")
    print("Choose one of the options: ")
    print("1. Display available bikes")
    print("2. Rent a bike")
    print("3. Return a bike")
    print("4. Display shop revenue")
    print("5. Exit")
    print("********************************")
    user_choice = int(input("Enter your choice (1-5): "))

    if user_choice == 1:
        bike_shop.display_stock()
    elif user_choice == 2:
        rent_type = input("Enter rental type (hourly/daily/weekly): ")
        rent_number = int(input("How many bikes do you want to rent? "))

        if rent_type == "hourly":
            bike_shop.rent_bike_hourly(rent_number)
        elif rent_type == "daily":
            bike_shop.rent_bike_daily(rent_number)
        elif rent_type == "weekly":
            bike_shop.rent_bike_weekly(rent_number)
        else:
            print("Invalid rental type.")

    elif user_choice == 3:
        return_type = input("Enter return type (hourly/daily/weekly): ")
        return_number = int(input("How many bikes do you want to return? "))

        if return_type == "hourly" and return_number > (items_in_stock['hourly']+rent_number-items_rented['hourly']):
            print("You can't return more bikes than rented hourly.")
        elif return_type == "daily" and return_number > (items_in_stock['daily']+rent_number-items_rented['daily']):
            print("You can't return more bikes than rented daily.")
        elif return_type == "weekly" and return_number > (items_in_stock['weekly']+rent_number-items_rented['weekly']):
            print("You can't return more bikes than rented weekly.")
        else:
            bike_shop.return_bike(return_type, return_number)
    elif user_choice == 4:
        bike_shop.display_revenue()
    elif user_choice == 5:
        break
    else:
        print("Invalid input. Please enter a number from 1 to 5.")
