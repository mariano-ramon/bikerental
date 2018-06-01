# I'm aware that this was not expected and because of this  
# it has no regard about design or good practices
# I made it just to make sure the model made sense and expose my reasoning behind it

from classes import Bike, Rent, Period, Group, FamilyPromotion
from db import periods, bikes


class Program(object):
    """Main"""
   
    group = None
    bikes = None
    periods = None

    def __init__(self):
        self.init_db()
        self.group = Group()
        self.group.rents = []

    
    def run(self):
        print("Welcome to Bike Rental")
        while self.available_bikes() > 0:

            action_input = input("[a]dd, [u]ndo, [f]inish? ")
            if not self.is_valid_input( action_input, ['a','u','f']):
                continue
            
            if action_input == 'a':
                    
                period_input = input("[h]our, [d]ay, [w]eek? ")
                options = {"h":"hour", "d":"day", "w":"week"}

                if not self.is_valid_input(period_input, ['h','d','w']):
                    continue                

                bike = next(b for b in self.bikes if b.available == True)
                period = next(p for p in self.periods if p.name == options[period_input])

                rent = Rent(bike, period)
                self.group.add_rent(rent)

            if action_input == 'u':
                self.group.remove_rent(self.group.rents[-1])


            self.print_order()

            if action_input == 'f':
                self.group.calculate_price()
                while not self.apply_promotion():
                    edit_input = input("Edit Order? [y]es, [n]o? ")
                    if not self.is_valid_input(edit_input, ["y","n"]):
                        continue

                    if edit_input == "y":
                        break

                    if edit_input == "n":
                        self.print_total()
                        return

                    if not self.group.discount:
                        return

                if self.group.discount:
                    break


        self.print_total()

    def apply_promotion(self):
            prom_proc = False
            action_input = input("Apply family promotion? [y]es, [n]o? ")
            
            if not self.is_valid_input(action_input, ["y","n"]):
                prom_proc = False

            if action_input == 'y':
                promotion = FamilyPromotion(self.group)
                if promotion.is_eligible():
                    promotion.calculate_price()
                    prom_proc = True
                else:
                    print(promotion.description)

            if action_input == 'n':
                self.group.discount = "nil"
                prom_proc = True

            return prom_proc

    def print_total(self):
        if not self.group.discount == ("nil" or None):
            print("\nFamily Discount: {}".format(self.group.discount))
        print("\nTotal Price is ${}\n".format(self.group.subtotal))
                    
        print("Thanks!")


    def print_order(self):
        print("="*40)
        print("\nOrder:")
        for rent in self.group.rents:
            print("Bike for 1 {} : ${}".format(rent.period.name, rent.period.price))
        self.group.calculate_price()
        print("\nAvailable Bikes: {} Subtotal: {}\n".format(self.available_bikes(), self.group.subtotal))
        print("="*40)        

    @staticmethod
    def is_valid_input(value, charlist):
        valid = True
        if value not in charlist:
            print('not a valid option')
            valid = False

        return valid

    def available_bikes(self):
        return sum([bike.available for bike in self.bikes])

    def init_db(self):
        self.bikes = []
        self.periods = []
        for bike in bikes:
            self.bikes.append(Bike(bike['number'],bike['available']))
        for period in periods:
            self.periods.append(Period(period['name'],period['price']))
            
        
        


if __name__ == '__main__':
    try:
       input = raw_input
    except NameError:
       pass
    p = Program()
    p.run()