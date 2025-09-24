class Car:
   
    # Task 1
    # Define a class named Car with attributes: make, model, year
    
    def __init__(self, make, model, year):
        # Initialize the attributes of the Car instance
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print information about the car in the specified format
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Porsche, Model: Targa, Year: 2029
# Create an instance of the Car class
my_car = Car("Porsche", "Targa", 2029)

# Call the describe_car method on the instance
my_car.describe_car()
