from Function_car import Car, Booking, generate_otp, get_valid_input

def main():
    cars = [
        Car(1, True, 2),
        Car(2, False, 4),
        Car(3, True, 3),
        Car(4, True, 7)
    ]
    
    bookings = []
    mini_bookings = 0 

    for car in cars:
        car.display_car_info()

    while True:
        try:
            user_opt = int(input("Enter 1 to book and 2 to exit: "))
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
            continue
        
        if user_opt == 1:
            print("         CAR MODEL       ")
            print("Mini - 2 seats")
            print("Sedan - 4 seats")
            print("Suv - 3 seats")
            print("Prime - 7 seats")
            print("***********************************************")
            car_choice = input("WHICH CAR DO YOU WANT? ").capitalize()
            

            if car_choice == "Mini":
                if mini_bookings < 2:
                    print("Id: 7834")
                    print("DRIVER NAME: Arun is available")
                    print("NUMBER: 7689054321")
                    print("AGE: 33")
                    print("***********************************************")
                    mini_bookings += 1
                else:
                    print("Sorry, Mini car can only be booked twice.")
                    continue
            elif car_choice == "Sedan":
                 if mini_bookings < 3:
                      print("DRIVER NAME: Arawind")
                      print("NUMBER: 9667725375")
                      print("AGE: 32")
                      print("***********************************************")
                      mini_bookings += 1
                 else:
                      print("Sorry, Sedan car can only be booked more than 3.")
                      continue
            elif car_choice == "Suv":
                 if mini_bookings < 4:
                      print("DRIVER NAME: Arun Mozhi")
                      print("NUMBER: 7689047895")
                      print("AGE: 21")
                      print("***********************************************")
                      mini_bookings += 1
                 else:
                      print("Sorry, Suv car can only be booked more than 4")
                      continue
                      
            elif car_choice == "Prime":
                 if mini_bookings < 5:
                      print("DRIVER NAME: Kamal")
                      print("NUMBER: 765678321")
                      print("AGE: 34")
                      print("***********************************************")
                      mini_bookings += 1
                 else:
                      print("Sorry, Prime car can only be booked mnore than 5.")
                      continue

                      
            else:
                print("SORRY INVALID CHOICE")
                exit(0)

            def validate_phone(phone):
                return phone.isdigit() and len(phone) == 10

            phone = get_valid_input("Enter your phone number: ", validate_phone)

            booking = Booking()
            if booking.is_available(bookings, cars):
                 bookings.append(booking)
                 print("Your booking is confirmed")
                 otp_length = 10
                 otp = generate_otp(otp_length)
                 print(otp)
                 distance = float(input("Enter distance: "))
                 if distance < 5:
                      amount = 150
                 else:
                      distance1 = distance - 5
                      amount = distance1 * 10
                      print(f"Amount: {amount}")
                      print("Booking is confirmed")
            
        elif user_opt == 2:
             break
        else:
             print("Invalid choice")
                 

if __name__ == "__main__":
    main()
