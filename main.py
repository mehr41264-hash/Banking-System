#Importing the random module to create the unique account numbers
import random
def unique():
    return ''.join(str(random.randint(0,9)) for _ in range(9))

#Importing the datetime module for the user's transactions, deposits and withdraws
from datetime import datetime

#"Banking System"
print('Welcome to the bank "XYZ" ')

#Creating the balance check function for the user for the option of menu
balance = 0
def balance_check(balance):
    print(f"Your balance is {balance}$")

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
    "1. Deposit Amount" "\n"
    "2. Withdraw Amount" "\n"
    "3. Check Balance" "\n"
    "4. Share Balance" "\n"
    "4. Transaction History" "\n"
    "5. Exit")
    while True:
        user_menu = input("Enter the option: ").lower().strip()
        if user_menu not in ("depositamount", "withdrawamount", "checkbalance", "sharebalance", "transactionhistory", "exit"):
            print("Invalid Action, try again")
            continue
        if user_menu == "checkbalance":
            balance_check(balance)
            continue
        elif user_menu == "depositamount":
            balance = deposit(logged_username, balance)
            continue
        elif user_menu == "withdrawamount":
            balance = withdraw(logged_username, balance)
            continue
        elif user_menu == "sharebalance":
            balance = transfer_amount(logged_username, balance)
        elif user_menu == "transactionhistory":
            transaction_history(logged_username)
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
            username, password, fullname, pin, balance, unique_id = data.split(",")
            pin = int(pin)
            balance = int(balance)
            unique_id = int(unique_id)
            userdata.append((username, password, fullname, pin, balance, unique_id))

#Creating an empty list for the users to see their transactions for deposit and withdraw
transactions = []
with open("/home/mehr-ali/Documents/Banking System/transactionhistory.txt", "r") as file:
    for data in file:
        if data:
            logged_user, amount, time = data.split(",")
            amount = int(amount)
            transactions.append((logged_user, amount, time))

#Creating an empty list for the users to see their transactions for sharing balance
transactions_share = []
with open("/home/mehr-ali/Documents/Banking System/transactionhistoryshare.txt", "r") as file:
    for data in file:
        if data:
            logged_user, amount, account_send, time = data.split(",")
            amount = int(amount)
            account_send = int(account_send)
            transactions_share.append((logged_user, amount, account_send, time))

#Creating the signup function for the new users
class Signup():
    def __init__(self, username, password, fullname, pin, balance, unique_id):
        self.username = username
        self.password = password
        self.pin = pin
        self.balance = balance
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
        balance = int(input("Enter the ammount you want to enter: "))
        if balance < 10:
            print("Minimum amount is 10$")
            continue
        break
    #Adding the input into the file
    with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "a") as file:
        file.write(f"{username},{password},{fullname},{pin},{balance},{unique_id}\n")

    #Printing the message after successful signup
    print("Account was created successfully")
    #time calling the class as everything is defined time completly.
    signup_user = Signup(username, password, fullname, pin, balance, unique_id)
    #Showing the input to the user after their account creation
    print(f"Your Username is {signup_user.username}")
    print(f"Your Password is {signup_user.password}")
    print(f"Your Full Name is {signup_user.fullname}")
    print(f"Your PIN is {signup_user.pin}")
    print(f"Your Initial balance is {signup_user.balance}$")
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
            user, password, fullname, pin, balance, unique_id = user_data
            if user == username_login:
                if password == password_login:
                    print("Login Successfull")
                    return user_data
                else:
                    print("Password didn't matched")
                break

#Creating the balance function to balance ammount in the user's account
def deposit(logged_user, balance):
    time = datetime.now()
    while True:
        amount_input = input("Enter the amount you want to enter in your account: ").strip()
        if amount_input == "":
            print("Amount can't be empty, try again")
            continue
        if not amount_input.isdigit():
            print("Enter the amount in digits")
            continue

        amount = int(amount_input)

        if amount <= 0:
            print("You are Entering wrong amount, try again")
            continue
        break
    balance += amount
    print(f"You entered the amount of {amount}$.Total balance is time {balance}$")
    with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "w") as file:
        for i, user in enumerate(userdata):
            u, p, f, pin, dep, uid = user
            if u == logged_user:
                dep = balance
                userdata[i] = (u, p, f, pin, dep, uid)
            file.write(f"{u},{p},{f},{pin},{dep},{uid}\n")
    with open("/home/mehr-ali/Documents/Banking System/transactionhistory.txt", "a") as file:
        file.write(f"{logged_user},{amount},{time}\n")
        return balance
#Creating the function for the user to withdraw their ammount
def withdraw(logged_user, balance):
    time = datetime.now()
    while True:
        amount_input = input("Enter the amount you want to withdraw: ").strip()
        if amount_input == "":
            print("Amount can't be empty, try again.")
            continue
        if not amount_input.isdigit():
            print("Amount must be in numeric form, try again.")
            continue
        amount = int(amount_input)
        if amount <= 0:
            print("Invalid amount entered, try again.")
            continue
        if amount > balance:
            print("Insufficient Balance, try again")
            continue
        break
    balance -= amount
    print(f"You have withdrawn {amount}$. Remaining balance is {balance}$")
    with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "w") as file:
        for i, user in enumerate(userdata):
            u, p, f, pin, dep, uid = user
            if u == logged_user:
                dep = balance
                userdata[i] = (u, p, f, pin, dep, uid)
            file.write(f"{u},{p},{f},{pin},{dep},{uid}\n")
    with open("/home/mehr-ali/Documents/Banking System/transactionhistory.txt", "a") as file:
        file.write(f"{logged_user},{amount},{time}$\n")
        return balance
    
#Creating a function to send money across different users
def transfer_amount(logged_user, balance):
    time = datetime.now()
    while True:
        account_send = int(input("Enter the account number on which you want to send amount: "))
        if not any(account_send == user[5] for user in userdata):
            print("Account not found, try again")
            continue
        else:
            break
    while True:
        amount_sent = input(f"Enter the amount you want to send to the {account_send}: ")
        if not amount_sent.isdigit():
            print("Amount must be numeric: ")
            continue
        amount = int(amount_sent)
        if amount > balance:
            print("Not Enough Balance, try again")
            continue
        else:
            break
    pin_ok = False
    pin_sent = int(input("Enter your PIN: "))
    for u, p, f, pin, dep, uid in userdata:
        if u == logged_user:
            if pin == pin_sent:
                pin_ok = True
                break
    if not pin_ok:
        print("Wrong PIN")
        return balance
    balance -= amount
    print(f"{amount}$ were sent to the user {account_send}")
    for i, user in enumerate(userdata):
        u, p, f, pin, dep, uid = user
        if u == logged_user:
            userdata[i] = (u, p, f, pin, dep - amount, uid)
        elif uid == account_send:
            userdata[i] = (u, p, f, pin, dep + amount, uid)
    with open("/home/mehr-ali/Documents/Banking System/usersdata.txt", "w") as file:
        for u, p, f, pin, dep, uid in userdata:
            file.write(f"{u},{p},{f},{pin},{dep},{uid}\n")
    with open("/home/mehr-ali/Documents/Banking System/transactionhistoryshare.txt", "a") as file:
        file.write(f"{logged_user},{amount},{account_send},{time}\n")
    print("Transfer Successful")
    return balance

#Creating a function for the users to see their transactions
def transaction_history(logged_user):
    time = datetime.now()
    while True:
        user_history = input("Which history you want to see" "\n"
        "1. Deposit" "\n"
        "2. Withdraw" "\n"
        "3. Share Balance: ").lower()
        if user_history not in ("deposit","withdraw","sharebalance"):
            print("Invalid action, try again")
            continue
        else:
            break
    if user_history == "deposit":
        found = None
        for user, amount, time in transactions:
            if user == logged_user:
                print(f"{user} deposited {amount} at {time}\n")
                found = True
        if not found:
            print("No history of transactions")
    if user_history == "withdraw":
        found = None
        for user, amount, time in transactions:
            if user == logged_user:
                print(f"{user} withdrawn {amount} at {time}\n")
                found = True
        if not found:
            print("No history of transactions")
    if user_history == "sharebalance":
        found = None
        for user, amount, account, time in transactions_share:
            if user == logged_user:
                print(f"{user} sent {amount}$ to {account} at {time}\n")
                found = True
        if not found:
            print("No history of transactions")

#Calling the menu function for the signup option
if user == "signup":
    new_user = signup()
    balance = new_user.balance
    user_menu_call(balance)

#Loading the user's balance ammount into the list also calling the function
elif user == "login":
    logged_user = login()
    if logged_user:
        logged_username = logged_user[0]
        balance = logged_user[4]
        user_menu_call(balance)

#Using the exit function at the initial point of the bank
if user == "exit":
    print("Thankyou for using XYZ Bank")
