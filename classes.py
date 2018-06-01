class Bike(object):
    """Model for bikes"""

    number = None
    available = None

    def __init__(self, number, available):
        self.number = number
        self.available = available


class Period(object):
    """Model for rent periods"""

    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Rent(object):
    """Model for single rent, must belong """

    bike = None
    period = None
    
    def __init__(self, bike, period):
        self.bike = bike
        self.period = period

class Promotion(object):
    """Base class for promotions, all promotions must inherit from this class"""

    group = None
    description = None
    

    def __init__(self, group):
        self.group = group

    def is_eligible():
        raise NotImplementedError

    def calculate_price():
        raise NotImplementedError


class FamilyPromotion(Promotion):
    """Family Promotion"""

    description = "\n30%% applicable for groups of 3 to 5 bikes\n"

    def is_eligible(self):
        eligibility = False
        if len(self.group.rents) >= 3 and len(self.group.rents) <= 5:
            eligibility = True

        return eligibility
    def calculate_price(self):
        self.group.calculate_price()
        self.group.discount = self.group.subtotal * 0.3 
        promotion_price = self.group.subtotal - self.group.discount 
        self.group.subtotal = promotion_price


class Group(object):
    """docstring for Group"""

    rents = None
    subtotal = None
    discount = None

    def __init__(self, rents=None):
        self.rents = rents


    def add_rent(self, rent):
        self.rents.append(rent)
        rent.bike.available = False
        
    def remove_rent(self, rent):
        self.rents.remove(rent)
        rent.bike.available = True

    def calculate_price(self):
        price = 0
        for rent in self.rents:
            price += rent.period.price

        self.subtotal = price 

