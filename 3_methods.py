class MyClass:

    my_var = 100

    def __init__(self, name: str, time: str):  # dunder methods or magic methods
        self.name = name  # instance variable
        self.time = time  # instance variable
    
    def __str__(self):  # This method is called when you print the object, it should return a string representation of the object
        return f"MyClass(name={self.name}, time={self.time})"

    @classmethod
    def _change_value(cls, new_value):  # class method 
        cls.my_var = new_value  # class variables must be portected so that other dev can not change it directly 

    @staticmethod
    def fact(n: int): # static method 
        if n <= 1:
            return n
        else:
            return n*MyClass.fact(n-1)
        
    
    
obj1 = MyClass("Alice", "10:00")
obj2 = MyClass("Sandy", "19:00")

print("Object 1:", obj1)  # Calling __str__ method
print("Object 2:", obj2)  # Calling __str__ method

print("Earlier 1", obj1.my_var)  # Accessing class variable using instance
print("Earlier 2", obj2.my_var)  # Accessing class variable using instance

obj1._change_value(200)  # Changing class variable using one instance
print("Updated 1", obj1.my_var)  # Accessing updated class variable using first instance        
print("Updated 2", obj2.my_var)  # Accessing class variable using another instance
  
print("Factorial of 5 is:", MyClass.fact(5))  # Calling static method without creating an instance
