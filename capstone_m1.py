#---------------------------------------------------------------------------------------------------------

# list
cars = [{'No.': 1,'LP.' : 'B1234UIA', 'Name' : 'RAZE', 'Status' : 'IN-USED', 'Rp/Day' : 100000},
        {'No.': 2,'LP.' : 'L3416TKU', 'Name' : 'FORTUNER', 'Status' : 'READY', 'Rp/Day' : 150000},
        {'No.': 3, 'LP.' : 'H888STU', 'Name' : 'FERRARI', 'Status' : 'READY', 'Rp/Day' : 200000},
        {'No.': 4, 'LP.' : 'H878KUU', 'Name' : 'FERRARI', 'Status' : 'READY', 'Rp/Day' : 250000},
        {'No.': 5, 'LP.' : 'B7654KIA', 'Name' : 'RAZE', 'Status' : 'READY', 'Rp/Day' : 120000}] 

#table cars 
def view_cars(): # menampilkan daftar table dengan for loop
    print()
    print("==================================================================")
    print("                          AVAILABLE CARS            ")
    print("==================================================================")
    print("{:<10}{:<15} {:<15} {:<15} {:<10}".format('No.','LP.', 'Name', 'Status', 'Rp/Day'))
    print("------------------------------------------------------------------")
    for car in cars: # looping list 'cars' 
        print("{:<9} {:<15} {:<15} {:<15} Rp. {:<10},-".format(car['No.'],car['LP.'], car['Name'], car['Status'], car['Rp/Day'])) 
    print("==================================================================") 
    
# submenu add cars : choice 1
def cars_data():
    view_cars()
    return sub_menu_view_cars()


# sub menu view : choice 3
def find_car(nama_mobil): 
    found_cars = [] # Membuat list untuk menyimpan mobil dengan nama yang sama
    
    for car in cars:
        if car['Name'] == nama_mobil:
            found_cars.append(car) # Menambahkan mobil dengan nama yang sama ke dalam list
    
    if len(found_cars) == 0: # Jika tidak ditemukan mobil dengan nama yang sama
        print("Car name '{}' not found. Please try again.".format(nama_mobil))
        print()
        return sub_menu_view_cars()
    
    print("Found {} car(s) with name '{}'".format(len(found_cars), nama_mobil))
    
    for car in found_cars: # Menampilkan informasi mobil
        print()
        print("No.        : ", car['No.'])
        print("LP.        : ", car['LP.'])
        print("Name       : ", car['Name'])
        print("Status     : ", car['Status'])
        print("Rp/Day     :  Rp. {},-".format(car['Rp/Day']))
    
    return sub_menu_view_cars()

#submenu view : choice 2
def find_number(nomor_mobil):
    view_cars()
    for car in cars: # looping untuk mencari index yang sama di list 'cars'
        if car['No.'] == nomor_mobil:
            print()
            print("No.        : ", car['No.'])
            print("LP.        : ", car['LP.'])
            print("Name       : ", car['Name'])
            print("Status     : ", car['Status'])
            print("Rp/Day     :  Rp. {},-".format(car['Rp/Day']))
            return sub_menu_view_cars()
    print("Car name '{}' not found. Please try again.".format(nomor_mobil)) # jika tidak ketemu maka akan memprint ini dan kembali ke sub menu view cars
    print()
    return sub_menu_view_cars()

# nambah mobil ke list
def add_car():
    while True: # pake while biar trus ngulang kalo input salah
            print("\n-----Update Selection-----")
            print("1. Add car information to the list")
            print("2. Back to main menu")
            choice = input('Enter choice: ')
            
            if choice == '1': # lanjut ke add jika 1
                if not cars:
                    No = 1 
                else:
                    No = cars[-1]["No."] + 1
                
                
                LP = (input("Enter LP.: ")).upper()
                if len(LP) <= 8 and LP[0].isalpha() and LP[1].isnumeric() and LP[-2:-1].isalpha(): # isnumeric gbs
                    pass
                else:
                    print('\nThe format you entered is incorret. Please try again.')
                    return add_car()
            

                nama = input("Enter Name: ").upper()
                if nama.isalpha():
                    pass
                else:
                    print('The format you entered is incorret. Please try again.')
                    return add_car()
                
                avail = input("Enter Availability (IN-USED/READY): ").upper()
                if avail == 'IN-USED' or avail=='READY':
                    pass
                else:
                    print('The format you entered is incorret. Please try again.')
                    return add_car()
                
                Rp = (input("Enter Rp/Day: "))
                if Rp.isnumeric():
                    pass
                else:
                    print('The format you entered is incorret. Please try again.')
                    return add_car()
                
                car = {"No." : No,'LP.': LP, 'Name': nama, 'Status': avail, 'Rp/Day': Rp}
                
                print()
                print("Please confirm to add the following car to the list:")
                print("No.        : ", car['No.'])
                print("LP.        : ", car['LP.'])
                print("Name       : ", car['Name'])
                print("Status     : ", car['Status'])
                print("Rp/Day     :  Rp. {},-".format(car['Rp/Day']))

                while True:
                    confirm = input("Are you sure you want to add this car to the list? (y/n): ")
                    if confirm.lower() == 'y':
                        cars.append(car)
                        print("Car added successfully.")
                        break
                    elif confirm.lower() == 'n':
                        print("Car not added to the list.")
                        break
                    else:
                        print("Invalid format. Please try again.")
            elif choice == '2':
                menu()
            else:
                print("Invalid choice. Please try again.") 

def update_car():
    while True:
            print("\n-----Update Selection-----")
            print("1. Choose car information to update")
            print("2. Back to main menu")

            choice = input('Enter choice: ')
            
            if choice == '1':
                view_cars()
                choice = input("Enter car number to update: ")
                if choice.isnumeric():
                    choice = int(choice)
                    if len(cars) == choice-1:
                    #
                        for car in cars:
                            if choice == car['No.']:
                                break
                        else:
                            print("Car no.'{}' not found. Please try again.".format(choice))
                            return update_car()
                else:
                    print("Invalid format. Please try again.")
                    return update_car()
                
                
                car = cars[choice - 1]
                while True:
                    print("\n-------------Update Selection--------------")
                    print("1. Car Name")
                    print("2. License Plate")
                    print("3. Status")
                    print("4. Rp/day")
                    print("5. Back to main menu")
                    print("========================================")
                    
                    choice = input("Enter choice: ")
                    
                    if choice == "1":
                        car_name = input(f"Enter new car Name (current: {car['Name']}): ").upper() or car["Name"]
                        if car_name.isalpha():
                            while True:
                                confirm = input("Are you sure you want to update this new car Name to the list? (y/n): ")
                                if confirm.lower() == 'y':
                                    car['Name'] = car_name                                    
                                    print("Car updated successfully.")
                                    break
                                elif confirm.lower() == 'n':
                                    print("Car not updated to the list.")
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                        else:
                            print('The format you entered is incorret. Please try again.')
                            continue


                    elif choice == "2":
                        car_LP = input(f"Enter new License Plate (current: {car['LP.']}): ").upper() or car["LP."]
                        if len(car_LP) <= 8 and car_LP[0].isalpha() and car_LP[1].isnumeric() and car_LP[-2:-1].isalpha(): # isnumeric gbs
                            while True:
                                confirm = input("Are you sure you want to update this new License Plate to the list? (y/n): ")
                                if confirm.lower() == 'y':
                                    car['LP.'] = car_LP                                    
                                    print("Car updated successfully.")
                                    break
                                elif confirm.lower() == 'n':
                                    print("Car not updated to the list.")
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                        else:
                            print('\nThe format you entered is incorret. Please try again.')
                            continue
                        
                    elif choice == "3":
                        car_status = input(f"Enter new Availability [READY / IN-USED] (current: {car['Status']}): ").upper() or car["Status"]
                        if car_status == 'IN-USED' or car_status=='READY':
                            while True:
                                confirm = input("Are you sure you want to update this new Status to the list? (y/n): ")
                                if confirm.lower() == 'y':
                                    car['Status'] = car_status                                    
                                    print("Car updated successfully.")
                                    break
                                elif confirm.lower() == 'n':
                                    print("Car not updated to the list.")
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                        else:
                            print('The format you entered is incorret. Please try again.')
                            continue
                        
                    elif choice == "4":
                        new_price = input(f"Enter new Rp/Day (current: {car['Rp/Day']}): ")
                        if new_price.isnumeric():
                            while True:
                                confirm = input("Are you sure you want to update this new Price to the list? (y/n): ")
                                if confirm.lower() == 'y':
                                    car["Rp/Day"] = int(new_price)
                                    print("Car updated successfully.")
                                    break
                                elif confirm.lower() == 'n':
                                    print("Car not updated to the list.")
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                        else:
                            print('The format you entered is incorret. Please try again.')
                            continue
                                 
                                    
                    elif choice == "5":
                        menu()
                        
                    else:
                        print("========================================")
                        print("Invalid choice. Please try again.")
                        update_car()
                    
                    
            elif choice == '2':
                menu()
            else:
                print("Invalid choice. Please try again.") 

# ngapus 1 kolom
def delete_car():
    while True:
            print("\n-----Delete Selection-----")
            print("1. Choose car information to delete")
            print("2. Back to main menu")
            choice = input('Enter choice: ')
            if choice == '1':
                view_cars()
                nama_nomor_mobil = input("Enter car number or name: ").upper()
                found_cars = []
                for car in cars:
                    if str(car['No.']) == (nama_nomor_mobil) or car['Name'] == nama_nomor_mobil: # dijadiin string dl "no."
                        found_cars.append(car)
                        if len(found_cars) > 1:
                            print("Multiple cars with the same name or number were found:")
                            for car in found_cars:
                                print()
                                print("No.        : ", car['No.'])
                                print("LP.        : ", car['LP.'])
                                print("Name       : ", car['Name'])
                                print("Status     : ", car['Status'])
                                print("Rp/Day     :  Rp. {},-".format(car['Rp/Day']))

                            print()
                            confirm_delete = input("Do you want to delete all the cars above? (y/n): ").lower()
                            if confirm_delete == 'n':
                                return delete_car()
                        
                            elif confirm_delete == 'y':
                                for car in found_cars:
                                    if nama_nomor_mobil.isalpha():
                                        cars.remove(car)
                                        # print("Car with Name '{}' has been deleted.".format(car['Name']))
                                    else:
                                        cars.remove(int(car))
                                        # print("Car with No. '{}' and Name '{}' has been deleted.".format(car['No.'], car['Name']))
                                if nama_nomor_mobil.isalpha():
                                    print("Car with Name '{}' has been deleted.".format(car['Name']))
                                else:
                                    print("Car with No. '{}' and Name '{}' has been deleted.".format(car['No.'], car['Name']))

                            else:
                                print('Invalid format. Please choose "y" or "n".')           
                if not found_cars:
                    print("Car '{}' not found. Please try again.".format(nama_nomor_mobil))
                    return delete_car()

                if len(found_cars) == 1:
                    car = found_cars[0]
                    print()
                    print("No.        : ", car['No.'])
                    print("LP.        : ", car['LP.'])
                    print("Name       : ", car['Name'])
                    print("Status     : ", car['Status'])
                    print("Rp/Day     :  Rp. {},-".format(car['Rp/Day']))
                    confirm_delete = input("Are you sure you want to delete the car below? (y/n): ").lower()
                    if confirm_delete != 'y':
                        
                        return delete_car()
                    else:
                        cars.remove(car)
                        print("Car No. '{}' has been deleted.".format(car['No.']))


                # update the numbers of cars after the deleted car
                for i in range(len(cars)):
                    if cars[i]['No.'] == i+1:
                        continue
                    else:
                        cars[i]['No.'] = i+1
            elif choice == '2':
                menu()
            else:
                print("Invalid choice. Please try again.") 

# menu utama
def menu():
    while True:
        print("\n============MAIN MENU============")
        print()
        print("1. View cars") #done
        print("2. Add car") # done
        print("3. Update car") # done
        print("4. Delete car") # done
        print("5. Exit") # done
        print('========================================')
        choice = input("Enter choice: ")
        if choice == '1':
            sub_menu_view_cars()
        elif choice == '2':
            add_car()
        elif choice == '3':
            update_car()
        elif choice == '4':
            delete_car()
        elif choice == '5':
            while True:
                choice_exit = input("Are you sure you want to exit the application? (y/n): ")
                if choice_exit.lower() == 'y':
                    print()
                    print('========================================')
                    print('Thank you for using this application. Goodbye.')
                    print('========================================')
                    exit() 
                elif choice_exit.lower() == 'n':
                    menu()
                else:
                    print('========================================')
                    print("Invalid format. Please enter 'y' or 'n'.")
        else:
            print('========================================')
            print("Invalid choice. Please try again.")



#sub menuu
def sub_menu_view_cars():
    print("\n-----View cars-----")
    print()
    print("1. View all cars")
    print("2. Find a car by number")
    print("3. Find a car by name")
    print("4. Back to Main Menu")
    print('========================================')
    choice = input("Enter choice: ")


    if choice == '1':
        cars_data()
    elif choice == '2':
        print()
        nomor_mobil = (input("Enter car number: "))
        if nomor_mobil.isnumeric():
            nomor_mobil= int(nomor_mobil)
            find_number(nomor_mobil)
        else:
            print("Invalid format. Please try again.")
            return sub_menu_view_cars() 

    elif choice == '3':
        print()
        nama_mobil = input("Enter car name: ").upper()
        if nama_mobil.isalpha():
            find_car(nama_mobil)
        else:
            print("Invalid format. Please try again.")  
            return sub_menu_view_cars() 
    elif choice == '4':
        print()
        menu()
    else:
        print()
        print('Invalid choice. Please try again.')
        sub_menu_view_cars()




menu()



