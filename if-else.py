print("Welcome to the Rollercoaster!")

# Get user height
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    # Get age and calculate ticket price
    age = int(input("What is your age? "))
    if age > 18:
        bill = 100
        print("Adult tickets are ₹100.")
    elif age < 13:
        bill = 50
        print("Child tickets are ₹50.")
    else:
        bill = 70
        print("Teen tickets are ₹70.")
    
    # Ask for photo option
    wants_photo = input("Do you want a photo taken? (Y/N): ").strip().upper()
    if wants_photo == "Y":
        bill += 20
    
    # Output total bill
    print(f"Your final bill is ₹{bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
