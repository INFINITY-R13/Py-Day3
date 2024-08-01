print("Welcome To The Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18:
        bill= 12
        print("Adult tickets are $12.")
    elif age < 13:
        bill = 5
        print("Child tickets are $5.")      
    else:
         bill = 7  
         print("Teen tickets are $7.")  

    wants_photo = input("Do you want a photo taken? Y or N. ")   
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")    


else:
    print("Sorry, you have to grow taller before you can ride.")
    

