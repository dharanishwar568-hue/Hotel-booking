print("===============")
print("WELCOME TO GAYA HOTEL")
print("================")

print("Room types")

print("1.standard(1 bathroom)---1000 rupees")
print("2.high class(1 ac room and 1 attached washroom with tv facilities)----3500 rupees")
print("3.deluxe class(like a tent house with central ac and 3 bathrooms)---20000 rupees")

choice=int(input("enter yoyr choice (1-3):"))

name=input("enter your name:")
days_of_living=int(input("enter your days_of_leaving:"))

room_type=input("enter your room_type:")

if choice == 1:

    print("standard room is available")
    price=1000

elif choice == 2:

    print("high class room is available")

    price=3500

elif choice == 3:

    print("deluxe room is available")
    price=10000

total = price*days_of_living
print("=====HOTEL ROOM BILL DETAILS======")
print("Name of customer:",name)
print("Number of days living:",days_of_living)
print("ROOM TYPE:",room_type)
print("Total bill:",total)