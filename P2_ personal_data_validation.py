"""
A program to ask user to input personal data for an application.
Program to ensure user input is correct using defensive programming.
Checking for name, age, email, number and address. 
"""

# Welcome Message
print("-" * 50)
print("\nWelcome to the application process! \n\
Please enter your personal data as prompted\n")
print("-" * 50)

# Check first name is alphabetical characters only
while True:
    first_name = input("Please enter your first name: ")  
    if first_name.isalpha():
          break
    else:
        print("Sorry, first name not valid. Please try again.")

# Check last name is alphabetical characters only     
while True:
    last_name = input("Please enter your last name: ")
    if last_name.isalpha():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        print(f"Congratulations {full_name} on starting your application!\n")
        break
    else:
        print("Sorry, last name not valid. Please try again.")


# Check age is numerical and between 0 and 116
while True:
    try:
        user_age = int(input("Please enter your age: "))
        if user_age >= 0 and user_age <=116:  
            print(f"Thank you for entering your age as {user_age}.\n")
            break
        else:
            print("Age is not in valid range. Please try again.")
    except ValueError:
        print("Age does not contain digits. Please try again.")


# Check if '@' and '.' present in entry to show correct email address
while True:
    user_email = input("Please enter your email: ")
    if "@" in user_email and "." in user_email:
        print(f"Thank you for entering your email as {user_email.lower()}\n")
        break   
    else:
        print("Not a valid email address. Please try again.")

# Check phone number has correct number of digits and is numerical
while True:    
    phone_number = input("Please enter your phone number (no spaces or hyphens): ")
    if len(phone_number) == 11 and phone_number.isdigit():
        print(f"Thank you for entering {phone_number} as your phone number.\n")
        break
    else:
        print("Not a valid phone number.  Please try again.")

# Exit Message showing details input
print("-" * 50)
print(f"Thank you for entering your details: \nFull name: {full_name}\n\
Age: {user_age} \nEmail: {user_email} \nNumber: {phone_number}")
print("-" * 50)
