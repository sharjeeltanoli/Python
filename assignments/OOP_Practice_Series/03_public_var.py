class Car:
   
    def __init__ (self, brand: str):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting")

if __name__ == "__main__":

    # Creating an instance of the Car class
    car1: Car = Car("Toyota")

    # Accessing the public variable
    print(car1.brand)

    # Accessing the public method
    car1.start()