"""
A program to ask user to input personal data for an application.
Program to ensure user input is correct using defensive programming.
Checking for name, age, email, number and address. 
"""
# loop for error, what if no name put in
# ? FANCY - show user input at end, ask if correct or want to change any item ??
# ? Probably too much ? a is this correct? Y/N hmmmm

print("-" * 50)
print("\nWelcome to the application process! \n\
Please enter your personal data as prompted\n")
print("-" * 50)

# Check first and last name is alphabetical characters only
while True:
    first_name = input("Please enter your first name: ")  
    if first_name.isalpha():
          break
    else:
        print("Sorry, first name not valid. Please try again.")
        
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
        if user_age > 0 and user_age <=116:  
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
        print(f"Thank you for entering your email as {user_email}\n")
        break   
    else:
        print("Not a valid email address. Please try again.")  


# Check phone number has correct number of digits and is numerical
# ??  CAN I DO THIS REMOVING SPACES OR HYPENS?????
while True:    
    phone_number = input("Please enter your phone number (no spaces or hyphens): ")
    if len(phone_number) == 11 and phone_number.isdigit():
        print(f"Thank you for entering {phone_number} as your phone number.\n")
        break
    else:
        print("Not a valid phone number.  Please try again.")

print("-" * 50)
print(f"Thank you for entering your details: \nFull name: {full_name}\n\
Age: {user_age} \nEmail: {user_email} \nNumber: {phone_number}")
print("-" * 50)




# # DOB???
# while True:
#     date_dob = input("What date are you born? XX : ")
#     if date_dob.isdigit():
#         date_dob = int(date_dob)
#         if date_dob > 0 and date_dob <= 31:
#             print(f"Thanks for your date of birth")
#             break
#         else:
#             print("Not in range 0-31. Please try again.")
#     else:
#         print("Not a valid numerical entry. Please try again.")

# while True:
#     month_dob = input("What month are you born? XX : ")
#     if month_dob.isdigit():
#         month_dob = int(month_dob)
#         if month_dob > 0 and month_dob <= 12:
#             print(f"Thanks for your month of birth")
#             break
#         else:
#             print("Not in range 0-12. Please try again.")
#     else:
#         print("Not a valid numerical entry. Please try again.")

# while True:
#     year_dob = input("What month are you born? XXXX : ")
#     if year_dob.isdigit():
#         year_dob = int(year_dob)
#         if year_dob > 1906 and year_dob <= 2024:
#             print(f"Thanks for your month of birth")
#             break
#         else:
#             print("Not in range. Please try again.")
#     else:
#         print("Not a valid numerical entry. Please try again.")

# print(f"Thank you for entering your DOB as {date_dob}/{month_dob}/{year_dob}")


# how the feck do you check that??  
# house name or number, street, town, county, postcode
# show and ask if correct. if not try again.
# address = [house_num, street, town, county, postcode]
# address = input("Please enter your address: ")



# male/female/other???

# is there any other personal data to collect??

