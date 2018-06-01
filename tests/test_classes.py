# run python -m unittest tests.test_classes on parent directory

import unittest
from classes import FamilyPromotion, Group, Bike, Period, Rent


bikes = []
periods = []

def setUpModule():
    for bike in range(1,8):
        bikes.append(Bike(1,True))
    for period in (("A",2), ("B",4), ("C",8)):
        periods.append(Period(period[0],period[1]))


def tearDownModule():
    pass


class TestGroup(unittest.TestCase):

    def test_calculate_price_1(self):
        rents = [Rent(bikes[0],periods[0]),
                 Rent(bikes[1],periods[0])]
        group = Group(rents)
        group.calculate_price()
        self.assertEqual(4, group.subtotal)
        

    def test_calculate_price_2(self):
        rents = [Rent(bikes[0],periods[2])]
        group = Group(rents)
        group.calculate_price()
        self.assertEqual(8, group.subtotal)



class TestFamilyPromotion(unittest.TestCase):

    def test_calculate_price(self):
        rents = [Rent(bikes[0],periods[0]),
                 Rent(bikes[1],periods[2])]
        group = Group(rents)
        family_promotion = FamilyPromotion(group)
        family_promotion.calculate_price()
        self.assertEqual(7, group.subtotal)
        

    def test_is_eligible_1(self):
        rents = []
        for n in range(2):
            rents.append(Rent(bikes[n], periods[0]))

        group = Group(rents)
        family_promotion = FamilyPromotion(group)
        self.assertEqual(False, family_promotion.is_eligible())
        


    def test_is_eligible_2(self):
        rents = []
        for n in range(4):
            rents.append(Rent(bikes[n], periods[0]))
        group = Group(rents)
        family_promotion = FamilyPromotion(group)
        self.assertEqual(True, family_promotion.is_eligible())


    def test_is_eligible_3(self):
        rents = []
        for n in range(6):
            rents.append(Rent(bikes[n], periods[0]))
        group = Group(rents)
        family_promotion = FamilyPromotion(group)
        self.assertEqual(False, family_promotion.is_eligible())
        


if __name__ == '__main__':
    unittest.main()
