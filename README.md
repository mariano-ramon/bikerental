# Bike Rental

Bike Rental is a simple app to calculate the price of and rental order depending on the time used and apply promotions if applicable. 

Is an object oriented development and uses 3 classes meant to model database tables or documents (Bike, Period, Rent) and two classes that do calculations (Group, Promotion). `db.py` contains the fixed data using python objects mocking a db

Promotion is a base class that defines the properties and methods required for the inheried class to succesfully recalculate the price of a Group and set conditions of application. A Group consists of Rents and en each Rent has a Bike and Period of rental. 

A Group updates its state whenever its method calculate_price is called
Promotion recieves a group in its constructor and checks if eligible before update the group state

# Sample app
there is a sample app just meant to show how this could work, so manteinability or design was not considered. 
You can try it, running the next command on the root dir (works on python 2 and 3)
```python app.py```

# Testing
for running the tests run the next command from the root dir
```python -m unittest tests.test_classes```

