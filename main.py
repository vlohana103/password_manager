



##### Create
def create():
    while True:
        website_name = input("Name of website?\n")
        user = input("What is the Username or e-mail address?\n")
        password = input("Please input the password\n")
        password_manager[website_name] = (user, password)
        
        ask = input("Would you like to add another log(press q to quit)?\n")
        if ask.lower() == "q":
            print("Thanks for using the Password Manager!")
            break

##### Read
def read():
    i = 0
    for website_name, (user, password) in password_manager.items():
        print(f"Password Manager Log {i}: {website_name} -> {user}, {password}")
        i += 1

##### Update

##### Delete
def delete():
    pass


print("Welcome to the Password Manager!")

while True:
    menu_options = input("Press '1' to add a Password Log,\nPress '2' to view log\nPress '3' to exit\n")
    password_manager = {}

    # Create
    if menu_options == '1':
        create()

    # Read
    elif menu_option == '2':
        read()

    elif menu_options == '3':
        print("Thank you for using the Password Manager. Bye!")
        break


    else:
        print("Invalid Input")