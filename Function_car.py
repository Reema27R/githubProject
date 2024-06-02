import random
from datetime import datetime

class Car:
    def __init__(self, car_no, available, capacity):
        self.car_no = car_no
        self.available = available
        self.capacity = capacity

    def display_car_info(self):
        print(f"Car No: {self.car_no}, Available: {self.available}, Capacity: {self.capacity}")

    def get_car_no(self):
        return self.car_no

    def get_capacity(self):
        return self.capacity

class Booking:
    def __init__(self):
        self.passenger_name = input("Enter name: ")
        self.car_no = int(input("Enter car number: "))
        

    def is_available(self, bookings, cars):
        capacity = 0
        for car in cars:
            if car.get_car_no() == self.car_no:
                capacity = car.get_capacity()
                break
        else:
            print("Car not found")
            return False

        booked = sum(1 for b in bookings if b.car_no == self.car_no and b.date == self.date)
        return booked < capacity

def generate_otp(length):
    print("Generating OTP")
    print("Your OTP:", end=' ')
    numbers = "0123456789"
    otp = ''.join(random.choice(numbers) for _ in range(length))
    return otp

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if not validation_func(user_input):
            print("Invalid input, please enter again!")
        else:
            return user_input
