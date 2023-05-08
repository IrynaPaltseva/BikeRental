print("Bike Rental Shop")
print("1. Display available bikes")
print("2. Rent a bike")
print("3. Return a bike")
print("4. Display shop revenue")
print("5. Exit")


class MyBikeShop:
    def __init__(self, items_in_stock):
        self.items_in_stock = items_in_stock
        self.total_cost = 0

    def display_stock(self):
        print("Today we have bikes is stock:")
        for key, value in self.items_in_stock.items():
            print(key.title(), value)

    def rent_bike_hourly(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['hourly']:
            print("We don't have enough bikes in stock for hourly rental")
            return

        else:
            print("Congratulations, you rented", rent_number, 'bikes on hourly basis')
            self.items_in_stock['hourly'] -= rent_number
            self.total_cost += rent_number*5

    def rent_bike_daily(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['daily']:
            print("We don't have enough bikes in stock for daily rental")
            return

        else:
            print("Congratulations, you rented", rent_number, 'bikes on daily basis')
            self.items_in_stock['daily'] -= rent_number
            self.total_cost += rent_number * 20

    def rent_bike_weekly(self, rent_number):
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if rent_number > self.items_in_stock['weekly']:
            print("We don't have enough bikes in stock for daily rental")
            return

        else:
            print("Congratulations, you rented", rent_number, 'bikes on weekly basis')
            self.items_in_stock['weekly'] -= rent_number
            self.total_cost += rent_number * 60

    def rent_bike_discount(self, rent_number):
        discount = False
        if rent_number <= 0:
            print('Sorry, wrong number. Choose more than 0 bikes.')
            return

        if 3 <= rent_number >= 5:
            discount = True
        return discount

    def total_cost(self, discount):
        if discount:
            self.total_cost = self.total_cost*0.7


user_choice = int(input("Enter your choice (1-5): "))

items_in_stock = {
    'hourly': 11,
    'daily': 9,
    'weekly': 20
    }

rent_number = int(input("How many bikes do you want to rent? "))