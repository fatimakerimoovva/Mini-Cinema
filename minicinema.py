from person import *
from mall import *
from film import *
from money import *
print("""
write your personal information:
---------------------------------------
Worker or any employee ? - 1
Normal person ? - 2     
"""
    )

try:
    person_selection = int(input("Your selection: "))
except ValueError:
    exit("Enter Valid Value")
    
if person_selection == 1:
    people = Worker()
    print(people.who())
elif person_selection == 2:
    people = Person()
    print(people.who())
else:
    exit("Wrong Input")
    
mallganclik = Ganclik("Ganclik", 4, 6)
mall28 = Iyirmisekkiz("28may", 5, 8)
mallparkbulvar = ParkBulvar("Sahil", 5, 5)
mallamburan = Amburan("Bilgeh", 3, 5)
malldeniz = Deniz("Bulvar", 7, 9)

print("""
Choose Mall where wanna you go!
--------------------------------
Ganclik Mall - 1
Deniz Mall - 2
28 Mall - 3
Park Bulvar - 4
Amburan Mall - 5     
"""
    )

try:
    mall = int(input("Select Mall: "))
except ValueError:
    exit("Enter Valid Value")
    
if mall == 1:
    mallganclik.working_time()
    print("""
---------------------------
Information about mall
---------------------------
          """)
    mallganclik.information()
elif mall == 2:
    malldeniz.working_time()
    print("""
---------------------------
Information about mall
---------------------------
          """)
    malldeniz.information()
elif mall == 3:
    mall28.working_time()
    print("""
---------------------------
Information about mall
---------------------------
          """)
    mall28.information()
elif mall == 4:
    mallparkbulvar.working_time()
    print("""
---------------------------
Information about mall
---------------------------
          """)
    mallparkbulvar.information()
elif mall == 5:
    mallamburan.working_time()
    print("""
---------------------------
Information about mall
---------------------------
          """)
    mallamburan.information()
else:
    exit("Wrong Input!")


try:
    age = int(input('Yashinizi daxil edin: '))
except ValueError:
    exit()
    
if age > 14:
    print("You can enter to the mall")
else:
    print("cuppulu get evive))")
    exit()

try:
    vaccine = input("Do you have COVID-19 vaccinate? If you have, please enter your information about that and write -Active-: ")
except ValueError:
    exit()

if vaccine == "Active":
    print("Welcome Mall")
else:
    exit()
    
    
print("""
Choose Film what you wanna to watch! Here our films:
-----------------------------------------------------
Kunq-Fu Panda 4 - 1
Madam Web - 2
Avatar - 3
A Quite Place - 4
Lucy - 5
      """)



session1 = Hours('10:00','12:00')
session2 = Hours('14:00','16:00')
session3 = Hours('18:00', '20:00')

film1 = Film("Kunq-Fu Panda-4","Mike MitchellStephanie Stine",2024,"Comedy",122,6.7,[session2,session3],7)
film2 = Film("Madam Web","Clarkson",2024,"Marvel Comics",90,3.7,[session2,session1],8)
film3 = Film("Avatar","Kaes Cameron",2022,"Action, Fantasy",150,7.6,[session1,session3],9)
film4 = Film("A Quite Place","John Krasinski",2018,"Drama, Horror",180,7.5,[session2,session3],8)
film5 = Film("Lucy","Luc Besson",2014,"Action, Thriller",120,6.4,[session1,session2],7)


try:
    choose = int(input("Choose Film: "))

except ValueError:
    exit("Yanlis girish!")

if choose == 1:
    print(film1.show_info())
    film1.year_info()
    film1.duration_info()
    film1.rating_info()
    print("Choose:")
    for i in range(len(film1.hours)):
        print(str(i+1) + ')' + str(film1.hours[i].start_time) + "-" + str(film1.hours[i].end_time))
    a = int(input("Enter your choice: "))
    if a == 1:
        print(f"Your choise for {film1.name}: {str(film1.hours[i-1].start_time)+"-"+str(film1.hours[i-1].end_time)}")
        print(f"Your ticket price for {film1.name}: {film1.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film1)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
    elif a == 2:
        print(f"Your choise for {film1.name}: {str(film1.hours[i].start_time)+"-"+str(film1.hours[i].end_time)}") 
        print(f"Your ticket price for {film1.name}: {film1.price}")  
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film1)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
elif choose == 2:   
    print(film2.show_info())
    film2.year_info()
    film2.duration_info()
    film2.rating_info()
    print("Choose:")
    for i in range(len(film2.hours)):
        print(str(i+1) + ')' + str(film2.hours[i].start_time) + "-" + str(film2.hours[i].end_time))
    a = int(input("Enter your choice: "))
    if a == 1:
        print(f"Your choise for {film2.name}: {str(film2.hours[i-1].start_time)+"-"+str(film2.hours[i-1].end_time)}")
        print(f"Your ticket price for {film2.name}: {film2.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film2)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
    elif a == 2:
        print(f"Your choise for {film2.name}: {str(film2.hours[i].start_time)+"-"+str(film2.hours[i].end_time)}")
        print(f"Your ticket price for {film2.name}: {film2.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film2)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
        
elif choose == 3:
    print(film3.show_info())
    film3.year_info()
    film3.duration_info()
    film3.rating_info()
    print("Choose:")
    for i in range(len(film3.hours)):
        print(str(i+1) + ')' + str(film3.hours[i].start_time) + "-" + str(film3.hours[i].end_time))
    a = int(input("Enter your choice: "))
    if a == 1:
        print(f"Your choise for {film3.name}: {str(film3.hours[i-1].start_time)+"-"+str(film3.hours[i-1].end_time)}")
        print(f"Your ticket price for {film3.name}: {film3.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film3)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
    elif a == 2:
        print(f"Your choise for {film3.name}: {str(film3.hours[i].start_time)+"-"+str(film3.hours[i].end_time)}")
        print(f"Your ticket price for {film3.name}: {film3.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film3)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
elif choose == 4:
    print(film4.show_info())
    film4.year_info()
    film4.duration_info()
    film4.rating_info()
    print("Choose:")
    for i in range(len(film4.hours)):
        print(str(i+1) + ')' + str(film4.hours[i].start_time) + "-" + str(film4.hours[i].end_time))
    a = int(input("Enter your choice: "))
    if a == 1:
        print(f"Your choise for {film4.name}: {str(film4.hours[i-1].start_time)+"-"+str(film4.hours[i-1].end_time)}")
        print(f"Your ticket price for {film4.name}: {film4.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film4)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
    elif a == 2:
        print(f"Your choise for {film4.name}: {str(film4.hours[i].start_time)+"-"+str(film4.hours[i].end_time)}")
        print(f"Your ticket price for {film4.name}: {film4.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film4)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
elif choose == 5:
    print(film5.show_info())
    film5.year_info()
    film5.duration_info()
    film5.rating_info()
    print("Choose:")
    for i in range(len(film5.hours)):
        print(str(i+1) + ')' + str(film5.hours[i].start_time) + "-" + str(film5.hours[i].end_time))
    a = int(input("Enter your choice: "))
    if a == 1:
        print(f"Your choise for {film5.name}: {str(film5.hours[i-1].start_time)+"-"+str(film5.hours[i-1].end_time)}")
        print(f"Your ticket price for {film5.name}: {film5.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film5)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
    elif a == 2:
        print(f"Your choise for {film5.name}: {str(film5.hours[i].start_time)+"-"+str(film5.hours[i].end_time)}")
        print(f"Your ticket price for {film5.name}: {film5.price}")
        print("Do you want to buy ticket? If you want to buy, please write 'Yes' ")
        c = input("Enter your answer:")
        if c == "Yes":
            current_money = int(input("Movcut pulunuzu daxil edin: "))
            my_money = Money(current_money)
            my_money.set_money(film=film5)
            print("Good Luck and be patient, Enjoy the Movie:)")
                
        else:
            exit("Oldu,sagolun!")
else:
    exit("yanlis!")

                  
        





    


    



   
      
      


    
    


    
    

    







      


      
                
                
            