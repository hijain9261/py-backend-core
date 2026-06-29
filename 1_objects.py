class Car:
    total_car_count = 0  ## Class Variable to keep track of total cars
    def __init__(self, model, color, price):  # Constructor
        # model, color, price are Instance Variable
        self.model = model
        self.color = color
        self._price = price
        Car.total_car_count += 1
    
    def display_info(self):   ## Class Method 
        return(f"Model: {self.model}, Color: {self.color}, Price: ${self._price}")

    def startEngine(self):
        return(f"{self.model}🚘 is Started! ")

car1 = Car("Toyato camry", "Red", "$30000") # Creating an instance of the Car class
print("Earlier", car1.display_info())
car1._price = "$28000"  # Modifying the price using the instance variable
print("Updated", car1.display_info())  # Displaying the updated information