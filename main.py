



##### Create
def create():
    while True:
        website_name = input("Name of website?\n")
        user = input("What is the Username or e-mail address?\n")
        password = input("Please input the password\n")
        password_manager[website_name] = (user, password)
        
        ask = input("Would you like to add another log(press q to return to main menu)?\n")
        if ask.lower() == "q":
            print("Thanks for using the Password Manager!")
            break

##### Read
def read():
    for website_name, (user, password) in password_manager.items():
        print(f"Password Manager Log: {website_name} -> {user}, {password}")
    

##### Update
def update():
    print(password_manager)
    update_item = input("Which log would you like to update?\n")
    for website_name, (user, password) in password_manager.items():
        confirm = input(f"Are you sure you want to Update {update_item}? (Y/N)\n")
        if confirm.lower() == "n":
            print(f"{update_item} has not been updated")
            break
        elif confirm.lower() == "y":
            print(f"Updating {update_item}.")
            password_manager.update(update_item)
            break
        else:
            print("Invalid Option.")        

##### Delete
def delete():
    print(password_manager)
    remove_item = input("Which log would you like to remove?\n")
    for website_name, (user, password) in password_manager.items():
        confirm = input(f"Are you sure you want to Delete {remove_item}? (Y/N)\n")
        if confirm.lower() == "n":
            print(f"{remove_item} has not been deleted")
            break
        elif confirm.lower() == "y":
            print(f"Deleting {remove_item}.")
            del password_manager[remove_item]
            break
        else:
            print("Invalid Option.")


print("Welcome to the Password Manager!")
password_manager = {}

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