#Importing the random module to create the unique account numbers
import random
def unique():
    return ''.join(str(random.randint(0,9)) for _ in range(9))

#"Banking System"
print('Welcome to the bank "XYZ" ')

#Creating the balance check function for the user for the option of menu
balance = 0
def balance_check(balance):
    print(f"Your balance is {balance}")

#Initialization of user's input for Signup/Login
print("Select an option to continue" "\n"
"1. Signup" "\n"
"2. Login" "\n"
"3. Exit")
while True:
    user = input("Enter the option: ").lower().strip()
    if user not in ("signup", "login", "exit"):
        print("Invalid action, try again!")
        continue
    else:
        break

#Creating the menu function for the  users to initialize the menu settings
def user_menu_call(balance):
    print("Select an option to continue" "\n"
    "1. Deposit Ammount" "\n"
    "2. Withdraw Ammount" "\n"
    "3. Check Balance" "\n"
    "4. Share Balance" "\n"
    "5. Exit")
    while True:
        user_menu = input("Enter the option: ").lower().strip()
        if user_menu not in ("depositammount", "withdrawammount", "checkbalance", "sharebalance", "exit"):
            print("Invalid Action, try again")
            continue
        if user_menu == "checkbalance":
            balance_check(balance)
            continue
        elif user_menu == "exit":
            print("Thanks for using XYZ Bank")
            return
        else:
            break

#Creating an empty list which would be called when loading user's data, from the usersdata.txt file
userdata = []
with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "r") as file:
    for data in file:
        data = data.strip()
        if data:
            username, password, fullname, pin, initial_deposit, unique_id = data.split(",")
            pin = int(pin)
            initial_deposit = int(initial_deposit)
            unique_id = int(unique_id)
            userdata.append((username, password, fullname, pin, initial_deposit, unique_id))

#Creating the signup function for the new users
class Signup():
    def __init__(self, username, password, fullname, pin, initial_deposit, unique_id):
        self.username = username
        self.password = password
        self.pin = pin
        self.initial_deposit = initial_deposit
        self.unique_id = unique_id
        self.fullname = fullname

#Creating logic for the user's input for the signup using a function
def signup():
    unique_id = unique()
    while True:
        username = input("Enter your username: ").lower().strip()
        if any(username == user[0] for user in userdata):
            print("Username already exists try another one")
            continue
        elif username == "":
            print("Username must not be empty")
            continue
        break
    while True:
        password = input("Enter your password: ")
        if password == "":
            print("Password must not be empty")
            continue
        break
    while True:
        fullname = input("Enter your Full Name: ")
        if fullname == "":
            print("Fullname can't be empty")
            continue
        break
    while True:
        pin_input = input("Enter the 4 digit PIN: ")
        if not pin_input.isdigit():
            print("PIN must be numeric")
            continue
        elif len(pin_input) != 4:
            print("PIN must be exactly 4 digits")
            continue
        pin = int(pin_input)
        break
    while True:
        print("You have to deposit the ammount for the creation of your account" "\n"
            "Minimum deposit is 10$")
        initial_deposit = int(input("Enter the ammount you want to enter: "))
        if initial_deposit < 10:
            print("Minimum Deposit is 10$")
            continue
        break
    #Adding the input into the file
    with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "a") as file:
        file.write(f"{username},{password},{fullname},{pin},{initial_deposit},{unique_id}\n")

    #Printing the message after successful signup
    print("Account was created successfully")
    #Now calling the class as everything is defined now completly.
    signup_user = Signup(username, password, fullname, pin, initial_deposit, unique_id)
    #Showing the input to the user after their account creation
    print(f"Your Username is {signup_user.username}")
    print(f"Your Password is {signup_user.password}")
    print(f"Your Full Name is {signup_user.fullname}")
    print(f"Your PIN is {signup_user.pin}")
    print(f"Your Initial Deposit is {signup_user.initial_deposit}$")
    print(f"Your Banking ID is {signup_user.unique_id}")
    return signup_user

#Making the Login Function
def login():
    while True:
        username_login = input("Enter your username: ").lower().strip()
        if username_login == "":
            print("Username must not be empty, try again")
            continue
        elif not any(username_login == user[0] for user in userdata):
            print("Username not exist, try again")
            continue
        break
    while True:
        password_login = input("Enter your password: ").strip()
        if password_login == "":
            print("Password must not be empty")
            continue
        for user_data in userdata:
            user, password, fullname, pin, initial_deposit, unique_id = user_data
            if user == username_login:
                if password == password_login:
                    print("Login Successfull")
                    return user_data
                else:
                    print("Password didn't matched")
                break


#Calling the menu function for the signup option
if user == "signup":
    new_user = signup()
    balance = new_user.initial_deposit
    user_menu_call(balance)

#Loading the user's deposit ammount into the list also calling the function
elif user == "login":
    logged_user = login()
    if logged_user:
        balance = logged_user[4]
        user_menu_call(balance)

#Using the exit function at the initial point of the bank
if user == "exit":
    print("Thankyou for using XYZ Bank")
