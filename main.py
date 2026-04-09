import json
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# cryptography
load_dotenv()
key = os.getenv("ENCRYPTION_KEY")
cipher = Fernet(key)

def encrypt_pass(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_pass(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()




# loads file
def load_from_file():
    try:
        with open("password_manager.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# saves file
def save_to_file():
    with open("password_manager.json", "w") as f:
        json.dump(password_manager, f)



##### Create
def create():
    while True:
        website_name = input("Name of website?\n")
        user = input("What is the Username or e-mail address?\n")
        password = input("Please input the password\n")

        encrypted_password = encrypt_pass(password)

        password_manager[website_name] = (user, encrypted_password)
        save_to_file()
        
        ask = input("Would you like to add another log (press q to return to main menu)?\n")
        if ask.lower() == "q":
            print("Main Menu")
            break

##### Read
def read():
    i = 1
    for website_name, (user, enc_password) in password_manager.items():
        decrypt_password = decrypt_pass(enc_password)
        print(f"{i}. Password Manager Log: {website_name} -> {user}, {decrypt_password}")
        i += 1
    

##### Update 
def update():
    logs = list(password_manager.keys())
    if not logs:
        print("No log available to update.")
        return

    read()

    try:
        choice = int(input("Enter the number of the log you would like to update\n"))
        if 1 <= choice <= len(logs):
            selected_log = logs[choice - 1]

            print(f"updating log for: {selected_log}")
            new_user = input("New Username/Email: ")
            new_pass = input("New Password: ")

            password_manager[selected_log] = (new_user,encrypt_pass(new_pass))
            save_to_file()

            print("log updated successfully!")
        else:
            print("Invalid number selection.")
    except ValueError:
        print("Please enter a valid number, not text.")
    

##### Delete 
def delete():
    logs = list(password_manager.keys())
    if not logs:
        print("No logs to delete")
        return
    
    read()

    try:
        choice = int(input("Which number log would you like to remove?\n"))

        if 1 <= choice <= len(logs):
            selected_log = logs[choice - 1]
            
            confirm = input(f"Are you sure you want to Delete {selected_log}? (Y/N)\n")
            if confirm.lower() == "y":
                del password_manager[selected_log]
                save_to_file()

                print(f"{selected_log} has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid Number")
    except ValueError:
        print("Please enter a valid number.")


print("Welcome to the Password Manager!")
password_manager = load_from_file()

while True:
    use = input("Press '1' to use the Password Manager\nPress '2' to exit\n")
    if use == '1':
        ###
        menu_options = input("Press '1' to add a Password Log,\nPress '2' to view log\nPress '3' to update log,\nPress '4' to delete a log\nPress '5' to exit\n")

        # Create
        if menu_options == '1':
            create()

        # Read
        elif menu_options == '2':
            read()

        # Update
        elif menu_options == '3':
            update()
        
        # Delete
        elif menu_options == '4':
            delete()

        # Exit
        elif menu_options == '5':    
            print("Thank you for using the Password Manager. Bye!")
            break
        
        # Invalid Input
        else:
            print("Invalid Input")


    elif use == '2':
        print("Exiting ...")
        break
    else:
        print("Invalid Input. Please enter '1' or '2'")