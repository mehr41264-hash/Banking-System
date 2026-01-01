#"Banking System"
print('Welcome to the bank "XYZ" ')

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
def user_menu_call():
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
        if user_menu == "exit":
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
            username, password, pin, initial_deposit = data.split(",")
            userdata.append((username, password, pin, initial_deposit))

#Creating the signup function for the new users
class Signup():
    def __init__(self, username, password, pin, initial_deposit):
        self.username = username
        self.password = password
        self.pin = pin
        self.initial_deposit = initial_deposit

#Creating logic for the user's input for the signup using a function
def signup():
    while True:
        username = input("Enter your username: ").lower().strip()
        if any(username == user[0] for user in userdata):
            print("Username already exists try another one")
            continue
        elif username == "":
            print("Username must not be empty")
            continue
        break
    password = input("Enter your password: ")
    while True:
        if password == "":
            print("Password must not be empty")
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
        file.write(f"{username},{password},{pin},{initial_deposit}\n")

    #Printing the message after successful signup
    print("Account was created successfully")
    #Now calling the class as everything is defined now completly.
    signup_user = Signup(username, password, pin, initial_deposit)
    #Showing the input to the user after their account creation
    print(f"Your Username is {signup_user.username}")
    print(f"Your Password is {signup_user.password}")
    print(f"Your PIN is {signup_user.pin}")
    print(f"Your Initial Deposit is {signup_user.initial_deposit}$")

#Calling the menu function for the signup option
if user == "signup":
    if signup():
        user_menu_call()

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
        for user, password, pin, initial_deposit in userdata:
            if user == username_login:
                if password == password_login:
                    print("Login Successfull")
                    return True
                else:
                    print("Password didn't matched")
                break
#Calling the menu function login for the login option
if user == "login":
    if login() == True:
        user_menu_call()

#Using the exit function at the initial point of the bank
if user == "exit":
    print("Thankyou for using XYZ Bank")
