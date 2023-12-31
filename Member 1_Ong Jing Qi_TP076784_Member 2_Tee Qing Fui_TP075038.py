import datetime


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def check_file():
    # Initialize empty lists to store data from different files.
    user_list = []
    supplier_list = []
    inventory_list = []
    hospital_list = []
    # Initialize flags for supplier and inventory existence.
    supplier = True
    inventory = True
    try:
        with open("hospital.txt", "r") as hospital_file:
            hospital_file.seek(0)  # Reset the file pointer to the beginning
            for line in hospital_file:
                hospital_list.append(line.strip())

    except FileNotFoundError:
        # If the file doesn't exist, create an empty one.
        with open("hospital.txt", "a") as hospital_data:
            hospital_data.write("")
    # Try to open and read the suppliers file.
    try:
        with open("suppliers.txt", "r") as supp_file:
            if not supp_file.read(): # Check if the file is empty
                supplier = False
            else:
                supp_file.seek(0)  # Reset the file pointer to the beginning
                for line in supp_file:
                    supplier_list.append(line.strip())

    except FileNotFoundError:
        # If the file doesn't exist, create an empty one and set supplier flag to False.
        with open("suppliers.txt", "a") as supp_data:
            # supp_info(supplier_list)
            supp_data.write("")
            supplier = False
    # Try to open and read the inventory file.
    try:
        with open("ppe.txt", "r") as ppe_file:
            if not ppe_file.read():
                inventory = False
            else:
                ppe_file.seek(0)
                for line in ppe_file:
                    inventory_list.append((line.strip()))

    except FileNotFoundError:
    # If the file doesn't exist, create an empty one and set inventory flag to False.
        with open("ppe.txt", "a") as ppe_file:
            ppe_file.write(' ')
            inventory = False
            main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory)
    # Try to open and read the users file.
    try:
        with open("users.txt", "r") as user_file:
            user_data = user_file.read
            # If the file is empty, call the add_user function.
            if user_data == '':
                add_user(user_list, supplier_list, inventory_list, hospital_list)
            else:
                for line in user_file:
                    line = line.strip().split(":")
                    user_list.append(line)

    # If the file doesn't exist, create an empty one and call add_user function.
    except FileNotFoundError:
        with open("users.txt", "w") as user_data:
            user_data.write(' ')
            add_user(user_list, supplier_list, inventory_list, hospital_list)
    # Call opening_cover and main_login_page functions.
    main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory)


def initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list):
    # Print a message indicating that the user is in the Initial Creation section.
    print("You're In Initial Creation Now")
    while True:
        supp_exist = False  # Initialize a flag to check if the supplier exists.
        item_exist = False  # Initialize a flag to check if the item exists.
        # Collect information about the item from the user.
        item_code = input("Enter the item code: ").strip().upper()
        item_name = input("Enter the item name: ").strip().upper()
        item_last_supply_date = date_time()
        item_last_distribute_date = date_time()
        item_supp_name = input("Enter the item supplier name: ").strip().upper()
        item_supp_code = input("Enter the item supplier code: ").strip().upper()
        supp_contact_number = input("Enter the phone number of the supplier: ").strip()
        supp_email = input("Enter the e-mail of the supplier: ").strip()
        # Create details strings for the item and supplier.
        item_details = f'{item_code},{item_name},{item_supp_code},100,{item_last_supply_date},{item_last_distribute_date}'.strip()
        supp_details = f'{item_supp_code},{item_supp_name},{supp_contact_number},{supp_email},{item_last_supply_date}'.strip()
        # Check if the supplier exists in the suppliers file.
        with open("suppliers.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for convert in lines:
            supp_detail = convert.replace("\n", "").split(",")
            if item_supp_code == supp_detail[0] and item_supp_name == supp_detail[1]:
                supp_exist = True
        # Check if the item exists in the inventory file.
        with open('ppe.txt', 'r') as read_inventory:
            lines = read_inventory.readlines()
        for convert in lines:
                item_detail = convert.replace("\n", "").split(",")
                if item_code == item_detail[0] and item_name == item_detail[1]:
                    item_exist = True

        # Handle different cases based on whether the supplier and item exist.
        if supp_exist and not item_exist:
            # Add the item to the inventory.
            with open("ppe.txt", "a") as ppe_data:
                ppe_data.write(item_details + "\n")
            print("Supplier Exist, Add Inventory Only")

        elif item_exist and not supp_exist:
            # Add the supplier to the suppliers file.
            with open('suppliers.txt','a') as supp_f:
                supp_f.write(supp_details + "\n")
            print("Inventory Exist, Add Supplier Only")
        elif not supp_exist and not item_exist:
            # Add both supplier and item.
            if len(lines) < 4:
                with open("ppe.txt", "a") as ppe_data:
                    # inven = item_details.strip().split(":")
                    ppe_data.write(item_details + "\n")
                    # inven_list.append(item_details)
                with open("suppliers.txt", "a") as supp_f:
                    # supp = supp_details.strip().split(":")
                    supp_f.write(supp_details + "\n")
                    # supp_list.append(supp_details)
            elif len(lines) >= 4:
                print("Supplier full")
        elif supp_exist and item_exist:
            print('Sorry,The Supplier And Item You Input Already Exist.')

        # Define a function to get user's choice to continue or finish.
        def get_choice():
            choice = input("Did you finish input the details of the inventory (y/n)?")
            if choice == "y":
                if user_login and staff_login:
                    print("Successfully entered staff page.")
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                elif user_login and admin_login:
                    print("Successfully entered admin page.")
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif choice == "n":
                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)
            else:
                print('Invalid Input!,Type Again!')
                get_choice()

        get_choice()


def main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory):
    # Print a header for the system.
    print("=" * 35)
    print("        Department Of Health       ")
    print("  Inventory Management System For  ")
    print("Personal Protective Equipment (PPE)")
    print("=" * 35)
    # Initialize login flags.
    user_login = False
    admin_login = False
    staff_login = False
    print('Login Page')
    print('-'*30)
    # Prompt user for user ID and password.
    user_id = input("Enter your user ID: ").strip().lower()
    user_pw = input("Enter your password: ").strip()

    # Check user credentials against the user list.
    with open('users.txt','r') as users:
        for user_info in users:
            user_info = user_info.strip().split(":")
            if user_id == user_info[0] and user_pw == user_info[2]:
                user_login = True
                break

    if user_login:
        # If user is successfully logged in:
        if not supplier or not inventory:
            # If supplier or inventory is missing:
            if user_info[3] == "admin":
                # If the user is an admin, go to initial creation mode.
                admin_login = True
                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)
            elif user_info[3] == "staff":
                # If the user is staff, go to initial creation mode.
                staff_login = True
                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)
        else:
            # If both supplier and inventory are available:
            if user_info[3] == "admin":
                # If the user is an admin, go to admin main menu.
                print("Successfully entered admin page.")
                admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

            elif user_info[3] == "staff":
                # If the user is staff, go to staff main menu.
                print("Successfully entered staff page.")
                staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    else:
        # If login was unsuccessful, let user to login again.
        print("Logged in unsuccessful..")
        print('Please Type Again')
        main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory)


def admin_main_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the admin menu repeatedly
    while True:
        print('Admin Menu')
        print('='*30)
        print("1.  User")
        print("2.  Supplier")
        print("3.  Hospital")
        print("4.  Inventory")
        print("5.  Search Features")
        choice = input("Enter your choice: ")
        # Based on user's choice, call respective functions or display error message.
        if choice == '1':
            admin_user_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            admin_supplier_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            admin_hospital_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            search_function(user_list, supplier_list, inventory_list, hospital_list)
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I don't Understand, please type again")
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def admin_user_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the user menu.
    while True:
        print("1.  Add user")
        print("2.  Delete user")
        print("3.  Modify User")
        print("4.  Summary User")
        print("5.  Main Menu")
        print("6.  Exit")
        # Get user's choice.
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or take appropriate action.
        if choice == "1":
            add_user(user_list, supplier_list, inventory_list, hospital_list)

        if choice == "2":
            delete_user(user_list)

        if choice == "3":
            modify_user(user_list, supplier_list, inventory_list, hospital_list)

        if choice == "4":
            user_summary(user_list, supplier_list, inventory_list, hospital_list)

        if choice == "5":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        # If the choice is not recognized, display an error message.
        if choice == "6":
            exit()


def admin_supplier_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the supplier menu.
    while True:
        print("1.  Add Supplier")
        print("2.  Delete Supplier")
        print("3.  Modify Supplier Data")
        print("4.  Supplier Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        # Get user's choice.
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or take appropriate action.
        if choice == '1':
            add_supp(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            delete_supp()

        elif choice == '3':
            modify_supp(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            supplier_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '6':
            exit()
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I Don't Understand, Please Type Again")
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def admin_hospital_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the hospital menu.
    while True:
        print("1.  Add Hospital")
        print("2.  Delete Hospital")
        print("3.  Modify Hospital Data")
        print("4.  Hospital Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        # Get user's choice.
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or take appropriate action.
        if choice == '1':
            add_hospital(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            delete_hospital()

        elif choice == '3':
            modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            hospital_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '6':
            exit()
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I Don't Understand, Please Type Again")
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the inventory menu repeatedly.
    while True:
        print("1.  Inventory Supply(+)")
        print("2.  Inventory Distribute(-)")
        print("3.  Modify Inventory Data")
        print("4.  Summary Inventory")
        print("5.  Delete Inventory")
        print("6.  Add New Inventory")
        print("7.  Inventory Quantity < 25")
        print("8.  Main Menu")
        print("9.  Exit")
        # Get user's choice
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or display error message.
        if choice == '1':
            supply(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            distribute(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            inventory_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            delete_item()

        elif choice == '6':
            add_inventory(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '7':
            less_25(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '8':
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '9':
            exit()
        # If the choice is not recognized, display an error message
        else:
            print("Sorry I Don't Understand, Please Type Again")
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_function(user_list, supplier_list, inventory_list, hospital_list):
    # Display the search page menu.
    print("Search Page")
    print("1. Search User")
    print("2. Search Items")
    print("3. Search Supplier")
    print("4. Search Hospital")
    print("5. Transaction Record")
    # Get user's choice.
    choice = input("Enter your choice: ")
    # Based on user's choice, call respective search functions.
    if choice == "1":
        search_user(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "2":
        search_items(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "3":
        search_supplier(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "4":
        search_hospital(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "5":
        track_filter_date(user_list, supplier_list, inventory_list, hospital_list)

    print('==' * 30)


def add_user(user_list, supplier_list, inventory_list, hospital_list):
    same_ID = False  # Flag to check if user ID already exists.
    while True:
        print("Add user page.")
        print('=='*30)
        user_ID = input("Enter the user ID: ").strip()
        user_name = input("Enter the user name: ").strip()
        user_pw = input("Enter the user password: ").strip()
        user_type = input("Choose the type of user (admin / staff): ").lower().strip()
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type)
        # Check if the user ID already exists.
        with open("users.txt", "r") as user_f, open("users.txt", "a") as user_append:
            for list in user_f:
                list = list.strip().split(':')
                if user_ID == list[0]:
                    same_ID = True
                    print("User ID Have Been Used, Please Change Another.")
                    continue

                elif not same_ID:
                    user_append.write(user_details + "\n")
                    ask = input("Did you finish add new user (y/n)?").lower().strip()
                    print("---" * 30)

                    if ask == "y":
                        user_list.append(user_details)
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

                    elif ask == "n":
                        user_list.append(user_details)
                        add_user(user_list, supplier_list, inventory_list, hospital_list)


def delete_user(user_list):
    # Display delete user page.
    print("Delete User Page")
    # Prompt for the user ID to be deleted.
    search_user_ID = input("Enter the user id you want to delete: ").strip()
    # Open the users.txt file for writing.
    with open("users.txt", "w") as user_f:
        # Iterate through the user list.
        for i in range(len(user_list)):
            if search_user_ID == user_list[i][0]:
                # If the user ID matches, do not write it to the file (effectively deleting it)
                print("User Deleted")
                print('-'*30)
            else:
                # If the user ID does not match, write it to the file.
                user_f.write(":".join(user_list[i]) + "\n")


def modify_user(user_list, supplier_list, inventory_list, hospital_list):
    # Display modify menu options.
    print("Modify Page")
    print("1. Change User ID")
    print("2. Change User Name")
    print("3. Change User Password")
    print("4. Change User Type")
    # Prompt user for choice.
    choice = input("Enter your choice: ")
    # Option to change user ID.
    if choice == "1":
        print("Change User ID Page")
        print('='*30)
        count = 0
        search_userID = input("Enter the user id you want to search:")
        with open('users.txt', 'r') as file_line, open("users.txt", "w") as user_f:
            lines = file_line.readlines()
            line = len(lines)
        #with open("users.txt", "w") as user_f:
            for i in file_line:
                i = i.strip().split(":")
                print(i)

            if search_userID == i[0]:
                print("Old UserID:", i[0])
                new_id = input("Enter Your New User Name: ")
                # i[1] = new_name
                i[0] = new_id
                print("Name Change Successful.....")
                # join ":" into the file to separate it.
                # user_f.write(":".join(user_list[i]) + "\n")

                user_f.write(":".join(i) + "\n")

                print(user_list)
            # for i in range(len(user_list)):
            elif count >= line and search_userID != i[0]:
                print('The UserID Not Exist')
                user_f.write(":".join(i) + "\n")
            else:
                user_f.write(":".join(i) + "\n")
        return
    if choice == "2":
        # Option to change user name.
        count = 0
        print("Change user Name.")
        search_userID = input("Enter the userID you want to edit: ")
        with open('users.txt', 'r') as file_line:
            line = len(file_line.readlines())
        with open("users.txt", "w") as user_f:
            for i in user_list:
                if search_userID == i[0]:
                    print('Old Name:', i[1])
                    new_name = input("Enter New User Name: ")
                    i[1] = new_name
                    print("Name change successful....")
                    user_f.write(":".join(i) + "\n")
                elif count >= line and search_userID != i[0]:
                    print('The UserID Not Exist')
                    user_f.write(":".join(i) + "\n")
                else:
                    user_f.write(":".join(i) + "\n")

    if choice == "3":
        # Option to change user password.
        print("Change user password.")
        count = 0
        search_userID = input("Enter the userID you want to edit: ")
        with open('users.txt', 'r') as file_line:
            line = len(file_line.readlines())
        with open("users.txt", "w") as user_f:
            for i in user_list:
                count += 1
                if search_userID == i[0]:
                    new_pw = input("Enter your new password: ")
                    i[2] = new_pw
                    # user_list = temp_list
                    print("Password change successful....")
                    user_f.write(":".join(i) + "\n")
                elif count >= line and search_userID != i[0]:
                    print('The UserID Not Exist')
                    user_f.write(":".join(i) + "\n")
                else:
                    user_f.write(":".join(i) + "\n")

    if choice == "4":
        # Option to change user type.
        print("Change user Type.")
        search_userID = input("Enter the userID you want to edit: ")
        count = 0
        with open('users.txt', 'r') as file_line:
            line = len(file_line.readlines())
        with open("users.txt", "w") as user_f:
            for i in user_list:
                count += 1
                if search_userID == i[0]:
                    print("The user type for this user ID is:", i[3])
                    confirm = input('Are You Sure Need To Change? (Y/N): ').upper().strip()
                    if confirm == 'Y':
                        if i[3] == "staff":
                            new_type = "admin"
                            i[3] = new_type
                            user_f.write(":".join(i) + "\n")
                            print("User type change successfully to admin....")

                        elif i[3] == "admin":
                            new_type = "staff"
                            i[3] = new_type
                            user_f.write(":".join(i) + "\n")
                            print("User type change successfully to staff....")
                    else:
                        print('User Type Change Failed')
                        user_f.write(":".join(i) + "\n")
                elif count >= line and search_userID != i[0]:
                    print("The userID does not match and the user type cannot be changed.")
                    user_f.write(":".join(i) + "\n")
                else:
                    user_f.write(":".join(i) + "\n")


def user_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Display a summary of user information.
    with open('users.txt', 'r') as read_users:
        for line in read_users:
            line = line.strip().split(':')
            print(f'UserID:{line[0]}     User Name:{line[1]}     User Password:{line[2]}        '
                  f'User Type:{line[3]} \n ')
    # Prompt user for choice: go back to main menu or exit.
    choice = input('1.Main Menu\n2.Exit').strip()
    # Return to main admin menu.
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Exit the program.
    if choice == '2':
        exit()
        # Return to main admin menu.
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def add_supp(user_list, supplier_list, inventory_list, hospital_list):
    # Initialize a flag to check if the supplier already exists.
    supp_exist = False
    # Read all records from the suppliers file.
    with open("suppliers.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    # Calculate the number of available slots for new suppliers.
    num = 4 - len(allrec)
    # Check if the supplier list is full.
    if num == 0:
        print("Supplier Full")
    # Continue adding new suppliers if there are available slots.
    while num != 0:
        print("Add New Supplier")
        print('==' * 30)

        # Get supplier details from user input.
        supp_code = input("Enter The Supplier Code: ").strip().upper()
        supp_name = input("Enter The Name Of Supplier:").strip().upper()
        supp_phone_number = input("Enter The Phone Number Of The Supplier: ").strip()
        supp_mail = input("Enter The Email  Of The Supplier: ").strip()
        last_supply_date = date_time()
        supp_details = f'{supp_code},{supp_name},{supp_phone_number},{supp_mail},{last_supply_date}'
        num = num - 1

        # Check if the new supplier already exists in the records.
        with open("suppliers.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for convert in lines:
            supp_detail = convert.replace("\n", "").split(",")
            if supp_code == supp_detail[0] and supp_name == supp_detail[1]:
                supp_exist = True
        # Handle cases where the supplier already exists or not.
        if supp_exist:
            print('Supplier Exist')
        elif not supp_exist:
            print(f'Supplier Code:{supp_code}   Supplier Name:{supp_name}   Supplier Phone Number:{supp_phone_number}    '
                  f'Supply Email:{supp_mail}    Last Supply Date:{last_supply_date}\n')
            confirm = input('Are You Sure You Want To Add This Supplier? (Y/N)').upper().strip()
            if confirm == 'Y':
                with open('suppliers.txt', 'a') as supp_f:
                    supp_f.write(supp_details)
                    print('Supplier Added')

            else:
                print('Supplier Add Failed')
        # Ask if the user wants to add another supplier.
        choice = input("Add Another Supplier (y/n):").lower().strip()
        if choice == "n":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            add_supp(user_list, supplier_list, inventory_list, hospital_list)


def delete_supp():
    # Display delete supplier page.
    print('Delete Supplier Page')
    # Get supplier code from user input.
    supp_code = input("Enter Supplier Code : ").upper().strip()

    # Read all lines from the suppliers file.
    with open("suppliers.txt", "r") as file:
        lines = file.readlines()

    # Open the suppliers file for writing.
    with open("suppliers.txt", "w") as supplier_f:
        for line in lines:
            # Write all lines except the one starting with the specified supplier code.
            if not line.startswith(supp_code):
                supplier_f.write(line)

    print("Supplier Deleted")


def modify_supp(user_list, supplier_list, inventory_list, hospital_list):
    # Display modification options for suppliers.
    print("Modify Supplier Page")
    print('=' * 30)

    # Get the supplier code from user input.
    supplier_code = input('Supplier Code:').upper().strip()
    count = 0
    supplier_found = False
    # Count total lines in the suppliers file.
    with open('suppliers.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Search for the supplier by code.
    with open('suppliers.txt', 'r') as check:
        for supplier in check:
            count += 1
            # If supplier found, display information and ask for confirmation.
            if supplier.startswith(supplier_code):
                supplier = supplier.strip().split(',')
                print(
                    f'Supplier Code:{supplier[0]}   Supplier Name:{supplier[1]}   Supplier Phone Number:{supplier[2]}    Supply Email:{supplier[3]}    '
                    f'Last Supply Date:{supplier[4]}\n')
                confirm = input('Is This Supplier You Need To edit? Y/N:').upper().strip()
                # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                if confirm == 'Y':
                    supplier_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If count exceeds total lines and supplier not found, give options to retry or return to main menu.
            elif count >= line and not supplier_found:
                print('Supplier Not Found')
                confirm3 = input('1. Type Again\n2. Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # If supplier found, display modification options.
    if supplier_found:
        print("1. Change Supplier Code")
        print("2. Change Supplier Name")
        print("3. Change Supplier Email")
        print("4. Change Supplier Phone Number")
        choice = input("Enter your choice: ")
        # Read all lines in the suppliers file.
        with open('suppliers.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()
        # Open the suppliers file for writing.
        with open('suppliers.txt', 'w') as edit_quantity:
            for suppliers in lines:
                if suppliers.startswith(supplier_code):
                    supplier_info = suppliers.strip().split(',')
                    # Handle different modification options
                    if choice == '1':
                        sup_code = input('Please Type New Supplier Code:').upper().strip()
                        supplier_info[0] = sup_code
                    elif choice == '2':
                        sup_name = input('Please Type New Supplier Name:').upper().strip()
                        supplier_info[1] = sup_name
                    elif choice == '3':
                        sup_email = input('Please Type New Email:').strip()
                        supplier_info[3] = sup_email
                    elif choice == '4':
                        sup_number = input('Please Type New Phone Number:').strip()
                        supplier_info[2] = sup_number

                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        edit_quantity.write(','.join(supplier_info) + "\n")
                        modify_supp(user_list, supplier_list, inventory_list, hospital_list)

                    # Print updated information and write it back to the file.
                    print(f'After Update...\n'
                          f'Supplier Code:{supplier_info[0]}   Supplier Name:{supplier_info[1]}   Supplier Phone Number:{supplier_info[2]}     Supplier Email:{supplier_info[3]}    '
                          f'Last Supply Date:{supplier_info[4]}\n')
                    print('Supplier Info Successfully Changed!')
                    edit_quantity.write(','.join(supplier_info) + "\n")

                else:
                    # If supplier not found, write it back to the file.
                    edit_quantity.write(suppliers)


def supplier_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Open and read the supplier file
    with open('suppliers.txt', 'r') as read_supplier:
        for line in read_supplier:
            # Extract supplier details from each line
            line = line.strip().split(',')
            # Print supplier information
            print(f'Supplier Code:{line[0]}     Supplier Name:{line[1]}     Supplier Phone Number:{line[2]} '
                  f'Supplier Email:{line[3]}      Last Supply Date:{line[4]} ')
    # Ask for user's choice
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def add_hospital(user_list, supplier_list, inventory_list, hospital_list):
    hosp_exist = False
    # Read all records from the hospital file.
    with open("hospital.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    num = 4 - len(allrec)
    if num == 0:
        print('Hospital Full')
    while num != 0:
        print("Add Hospital Page")
        print('==' * 30)

        # Get hospital details from user input.
        hospital_code = input("Enter the hospital code: ").upper().strip()
        hospital_name = input("Enter the name of hospital:").upper().strip()
        hospital_email = input("Enter the Email of the hospital: ").strip()
        hospital_phone_number = input("Enter the phone number of the hospital: ").strip()
        last_distribute_date = date_time()

        # Format hospital details for writing to file.
        hospital_details = f'{hospital_code},{hospital_name},{hospital_phone_number},{hospital_email},{last_distribute_date}'
        num = num - 1
        with open("hospital.txt", "r") as read_hosp:
            lines = read_hosp.readlines()
        for convert in lines:
            hosp_detail = convert.replace("\n", "").split(",")
            if hospital_code == hosp_detail[0] and hospital_name == hosp_detail[1]:
                hosp_exist = True
        if hosp_exist:
            print('Hospital already exist')
        elif not hosp_exist:
            print(f'Hospital Code:{hospital_code}   Hospital Name:{hospital_name}   Hospital Phone Number:{hospital_phone_number}    Hospital Email:{hospital_email}')
            confirm = input('Are You Sure To Add This Hospital? (Y/N): ').upper().strip()
            if confirm == 'Y':
                print('Hospital Added')
                with open("hospital.txt", "a") as file:
                    file.write(hospital_details + "\n")
            else:
                print('Hospital Adding Fail....')
        # Ask if the user wants to add another hospital.
        choice = input(" Add Another Hospital?(y/n): ")
        if choice == "n":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            add_hospital(user_list, supplier_list, inventory_list, hospital_list)


def delete_hospital():
    # Display delete hospital page.
    print('Delete Hospital Page')
    # Get hospital code from user input.
    hospital_code = input("Enter Hospital Code : ").upper().strip()
    # Read all lines from the hospital file.
    with open("hospital.txt", "r") as file:
        lines = file.readlines()
    # Open the hospital file for writing.
    with open("hospital.txt", "w") as hospital_f:
        for line in lines:
            # Write all lines except the one starting with the specified hospital code.
            if not line.startswith(hospital_code):
                hospital_f.write(line)

    print("Hospital Deleted")


def modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list):
    # Display modification options for hospitals.
    print("Modify Hospital Page")
    print('=' * 30)
    # Get the hospital code from user input.
    hospital_code = input('Hospital Code:').upper().strip()
    count = 0
    hospital_found = False
    # Count total lines in the hospital file.
    with open('hospital.txt', 'r') as file_line:
        line = len(file_line.readlines())

    # Search for the hospital by code.
    with open('hospital.txt', 'r') as check:
        for hospitals in check:
            count += 1
            # If hospital found, display information and ask for confirmation.
            if hospitals.startswith(hospital_code):
                hospitals = hospitals.strip().split(',')
                print(
                    f'Hospital Code:{hospitals[0]}   Hospital Name:{hospitals[1]}   Hospital Phone Number:{hospitals[3]}       Hospital Email:{hospitals[2]}'
                    f'Last Distribute Date:{hospitals[4]}\n')
                confirm = input('Is This Hospital Information You Need To edit? Y/N:').upper().strip()
                # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                if confirm == 'Y':
                    hospital_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If count exceeds total lines and hospital not found, give options to retry or return to main menu.
            elif count >= line and not hospital_found:
                print('Hospital Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    # If hospital found, display modification options.
    if hospital_found:
        print("1. Change Hospital Code")
        print("2. Change Hospital Name")
        print("3. Change Hospital Email")
        print("4. Change Hospital Phone Number")
        print("5. Back")
        choice = input("Enter your choice: ")
        # Read all lines in the hospital file.
        with open('hospital.txt', 'r') as check_lines:
            lines = check_lines.readlines()
        # Open the hospital file for writing.
        with open('hospital.txt', 'w') as hospital_f:
            for hospital in lines:
                if hospital.startswith(hospital_code):
                    hospital_info = hospital.strip().split(',')
                    # Handle different modification options.
                    if choice == '1':
                        new_code = input('Please Type The New Hospital Code:').upper().strip()
                        hospital_info[0] = new_code
                    elif choice == '2':
                        new_hospital_name = input('Please Type The New Hospital Name:').upper().strip()
                        hospital_info[1] = new_hospital_name
                    elif choice == '3':
                        new_email = input('Please Type The New Hospital Email:').upper().strip()
                        hospital_info[2] = new_email
                    elif choice == '4':
                        new_phone_number = input('Please Type The New Hospital Number:').upper().strip()
                        hospital_info[3] = new_phone_number
                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                    # Print updated information and write it back to the file.
                    print(f'After Update...\n'
                          f'Hospital Code:{hospital_info[0]}   Hospital Name:{hospital_info[1]}   Hospital Email:{hospital_info[2]}    '
                          f'Hospital Phone Number:{hospital_info[3]}      Last Supply Date:{hospital_info[4]}\n')
                    print('Item Successfully Updated!')
                    hospital_f.write(','.join(hospital_info) + "\n")

                else:
                    # If hospital not found, write it back to the file.
                    hospital_f.write(hospital)
    # Return to the main menu.
    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def hospital_summary(user_list, supplier_list, inventory_list, hospital_list):
        # Open and read the hospital file
        with open('hospital.txt', 'r') as read_hospital:
            for line in read_hospital:
                # Extract hospital details from each line
                line = line.strip().split(',')
                # Print hospital information
                print(f'Hospital Code:{line[0]}     Hospital Name:{line[1]}     Hospital Phone Number:{line[2]}'
                      f'Hospital Email:{line[3]}      Last Distribute Date:{line[4]} ')
        # Ask for user's choice
        choice = input('1.Main Menu\n2.Exit\nEnter Your Choice:').strip()
        if choice == '1':
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        if choice == '2':
            exit()

        else:
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def supply(user_list, supplier_list, inventory_list, hospital_list):
    # Display supply page header.
    print('Supply Page')
    print('==' * 30)
    # Get item code from user input and clean it.
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    item_found = False
    # Get the total number of lines in the inventory file.
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Check each line in the inventory file.
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            # If the line starts with the specified item code.
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}    Supplier Code:{items[2]}'
                    f'    Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                # If user confirms the item details
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    # If user chooses to type the item code again.
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        supply(user_list, supplier_list, inventory_list, hospital_list)
                        # If user chooses to return to the main menu.
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If the item is not found and we've checked all lines.
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                # If user chooses to type the item code again.
                if confirm3.strip() == '1':
                    supply(user_list, supplier_list, inventory_list, hospital_list)
                # If user chooses to return to the main menu.
                elif confirm3.strip() == '2':
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                else:
                    print("Sorry I Don't Understand")
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if item_found:
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                    item_quantity = int(item_info[3])
                    quantity_changes = int(input('Quantity(Boxes):'))
                    item_info[3] = str(item_quantity + quantity_changes)
                    item_info[5] = date_time()
                    print(f'After Update...\n'
                          f'Item Code:{item_code}   Item Name:{item_name}   Item Quantity:{item_info[3]}    '
                          f'Last Supply Date:{item_info[5]}\n')
                    print('Item Successfully Updated!')
                    with open('suppliers.txt', 'r') as file:
                        lines = file.readlines()
                    # Update the supplier's last supply date.
                    with open('suppliers.txt', 'w') as file:
                        for sup in lines:
                            if sup.startswith(item_supplier):
                                sup = sup.strip().split(',')
                                sup[4] = date_time()
                                file.write(','.join(sup) + '\n')
                            else:
                                file.write(sup)
                    # Log the transaction.
                    with open('transaction.txt', 'a') as trans:
                        trans.write(f'{"supply"}'
                                    f',{item_code},{item_supplier},{item_info[3]},{quantity_changes},{date_time()}\n')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)
    # Ask user if they want to continue adding items.
    choice = input('Continue Add Item? Y/N:').strip().upper()
    if choice == 'Y':
        supply(user_list, supplier_list, inventory_list, hospital_list)
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def distribute(user_list, supplier_list, inventory_list, hospital_list):
    # Display distribute page header.
    print('Distribute Page')
    print('=='*30)
    # Get item code from user input and clean it.
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    count2 = 0
    item_found = False
    # Get the total number of lines in the inventory and hospital files.
    with open('ppe.txt', 'r') as file_line, open('hospital.txt', 'r') as hospital_file:
        line = len(file_line.readlines())
        hospital = len(hospital_file.readlines())
    # Check each line in the inventory file.
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            # If the line starts with the specified item code.
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}    '
                      f'Last Distribute Date:{items[5]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                # If user confirms the item details.
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    # If user chooses to type the item code again.
                    if confirm2.strip() == '1':
                        distribute(user_list, supplier_list, inventory_list, hospital_list)
                    # If user chooses to return to the main menu.
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If the item is not found and we've checked all lines
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                # If user chooses to type the item code again.
                if confirm3.strip() == '1':
                    distribute(user_list, supplier_list, inventory_list, hospital_list)
                # If user chooses to return to the main menu.
                elif confirm3.strip() == '2':
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    if item_found:
        hospital_code = input('Please Type The Hospital Code:')
        hospital_code = hospital_code.upper().strip()
        hospital_found = False
        # Check each line in the hospital file.
        with open('hospital.txt', 'r') as check:
            for hospitals_line in check:
                count2 += 1
                # If the line starts with the specified hospital code.
                if hospitals_line.startswith(hospital_code):
                    hospitals_line = hospitals_line.strip().split(',')
                    print(f'Hospital Code:{hospitals_line[0]}   Hospital Name:{hospitals_line[1]}   '
                          f'Last Distribute Date:{hospitals_line[4]}\n')
                    confirm = input('Is This Hospital Detail Correct? Y/N:')
                    # If user confirms the hospital details.
                    if confirm.upper().strip() == 'Y':
                        hospital_found = True
                        continue
                    elif confirm.upper().strip() == 'N':
                        confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                        # If user chooses to type the hospital code again.
                        if confirm2.strip() == '1':
                            distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirm2.strip() == '2':
                            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                # If the hospital is not found and we've checked all lines.
                elif not hospital_found and count2 >= hospital:
                    print('Hospital Not Found')
                    confirm4 = input('1. Type Again\n2.Return To Main Menu\n>')
                    # If user chooses to type the hospital code again.
                    if confirm4.strip() == '1':
                        distribute(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm4.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if item_found and hospital_found:
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                lines = item
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                    quantity_changes = int(input('Quantity(Boxes):'))
                    item_quantity = int(item_info[3])
                    int(item_quantity)
                    new_quantity = item_quantity - quantity_changes
                    # If the quantity to distribute is more than available.
                    if new_quantity <= 0:
                        print(f'The available quantity is {item_quantity} boxes, not enough to distribute.')
                        confirmation = input('1.Retype\n2.Main Menu\n>')
                        # If user chooses to retype the quantity.
                        if confirmation == '1':
                            edit_quantity.write(','.join(item_info) + "\n")
                            distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirmation == '2':
                            edit_quantity.write(','.join(item_info) + "\n")
                            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    else:
                        item_info[3] = str(item_quantity - quantity_changes)
                        item_info[5] = date_time()
                        print(f'After Update...\n'
                              f'Item Code:{item_code}   Item Name:{item_name}   Item Quantity:{item_info[3]}    '
                              f'Last Distribute Date:{item_info[5]}\n')
                        print('Item Successfully Updated!')
                        # Log the transaction.
                        with open('transaction.txt', 'a') as trans:
                            trans.write(f'{"distribute"}'
                                        f',{item_code},{hospital_code},{item_info[3]},{quantity_changes},{date_time()}\n')
                        # Update the hospital's last distribute date.
                        with open('hospital.txt', 'r') as file:
                            lines = file.readlines()

                        with open('hospital.txt', 'w') as file:
                            for hos in lines:
                                if hos.startswith(hospital_code):
                                    hos = hos.strip().split(',')
                                    hos[4] = date_time()
                                    file.write(','.join(hos) + '\n')
                                else:
                                    file.write(hos)
                    edit_quantity.write(','.join(item_info) + "\n")
                else:
                    edit_quantity.write(item)
    choice = input('Continue Distribute Item? Y/N').strip().upper()
    if choice == 'Y':
        distribute(user_list, supplier_list, inventory_list, hospital_list)
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list):
            # Display modification options for inventory items.
            print("Modify Inventory Page")
            print('=' * 30)
            # Get the item code from user input.
            item_change = input('Item code:').upper().strip()
            count = 0
            item_found = False
            # Count total lines in the inventory file.
            with open('ppe.txt', 'r') as file_line:
                line = len(file_line.readlines())
            # Search for the item by code.
            with open('ppe.txt', 'r') as check:
                for items in check:
                    count += 1
                    # If item found, display information and ask for confirmation.
                    if items.startswith(item_change):
                        items = items.strip().split(',')
                        print(
                            f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[2]}    Supply Code:{items[3]}    '
                            f'Last Supply Date:{items[4]}\n')
                        confirm = input('Is This Item You Need To edit? Y/N:').upper().strip()
                        # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                        if confirm == 'Y':
                            item_found = True
                            continue
                        elif confirm == 'N':
                            confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                            if confirm2.strip() == '1':
                                modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                            elif confirm2.strip() == '2':
                                admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    # If count exceeds total lines and item not found, give options to retry or return to main menu.
                    elif count >= line and not item_found:
                        print('Items Not Found')
                        confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                        if confirm3.strip() == '1':
                            modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirm3.strip() == '2':
                            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

            # If item found, display modification options.
            if item_found:
                print("1. Change Item Code")
                print("2. Change Item Name")
                print("3. Change Item's Supplier Code")
                print("4. Back")
                choice = input("Enter your choice: ")
                # Read all lines in the inventory file.
                with open('ppe.txt', 'r') as edit_quantity:
                    lines = edit_quantity.readlines()
                # Open the inventory file for writing.
                with open('ppe.txt', 'w') as edit_quantity:
                    for item in lines:
                        if item.startswith(item_change):
                            item_info = item.strip().split(',')
                            # Handle different modification options.
                            if choice == '1':
                                new_code = input('Please Type Your New Item Code:').upper().strip()
                                item_info[0] = new_code
                            elif choice == '2':
                                new_name = input('Please Type Your New Item Name:').upper().strip()
                                item_info[1] = new_name
                            elif choice == '3':
                                supplier_found = False
                                count = 0
                                new_supplier_code = input(
                                    'Please Type The New Item Supplier Item Code:').upper().strip()
                                # Search for the new supplier code in the suppliers file.
                                with open('suppliers.txt', 'r') as supplier_f:
                                    for supplier in supplier_f:
                                        count += 1

                                        # If found, update the item's supplier code.
                                        if supplier.startswith(new_supplier_code):
                                            supplier_found = True
                                            item_info[2] = new_supplier_code
                                        # If not found and count exceeds total lines, give an error message.
                                        elif not supplier_found and count >= line:
                                            print("Sorry The Supplier You Type Haven't Register")
                                            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                            else:
                                print("Sorry I Dont Understand , Please Type Again.")
                                admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                            # Print updated information and write it back to the file.
                            print(f'After Update...\n'
                                  f'Item Code:{item_info[0]}   Item Name:{item_info[1]}   Item Quantity:{item_info[3]}     Supply Code:{item_info[2]}    '
                                  f'Last Supply Date:{item_info[5]}\n')
                            print('Item Successfully Updated!')
                            edit_quantity.write(','.join(item_info) + "\n")

                        else:
                            # If item not found, write it back to the file.
                            edit_quantity.write(item)


def inventory_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Initialize an empty list to store all records.
    all_record = []
    count = 0
    # Read the 'ppe.txt' file and populate the all_record list.
    with open('ppe.txt', 'r') as list:
        for line in list:
            all_record.append(line.strip().split(','))
        # Sort the records based on quantity in ascending order.
        for x in range(len(all_record) - 1):
            for y in range(x, len(all_record)):
                if int(all_record[x][3]) > int(all_record[y][3]):
                    temp = all_record[x]
                    all_record[x] = all_record[y]
                    all_record[y] = temp
    # Print the inventory summary.
    for i in range(len(all_record)):
        print(
            f'Item Code:{all_record[i][0]}           Item Name:{all_record[i][1]}           Supplier Code:{all_record[i][2]}        Quantity:{all_record[i][3]} boxes \n'
            f'Last Supply Date:{all_record[i][4]}         Last Distribute Date:{all_record[i][5]}\n')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def delete_item():
    # Display delete item page.
    print('Delete Item Page')
    # Get item code from user input.
    item_code = input("Enter Item Code : ").upper().strip()
    # Read all lines from the inventory file
    with open("ppe.txt", "r") as file:
        lines = file.readlines()
    # Open the inventory file for writing.
    with open("ppe.txt", "w") as inventory_f:
        for line in lines:
            # Write all lines except the one starting with the specified item code.
            if not line.startswith(item_code):
                inventory_f.write(line)

    print("Item Deleted")


def add_inventory(user_list, supplier_list, inventory_list, hospital_list):
    item_exist = False
    supplier_found = False
    # Get the total number of lines in the suppliers file.
    with open('suppliers.txt', 'r') as file_line:
        supp_line = len(file_line.readlines())
    # Read all records from the inventory file.
    with open("ppe.txt", "r") as file:
        allrec = []
        for read in file:
            rec = read.strip().split(",")
            allrec.append(rec)
    print("Add New Inventory Page")
    print('==' * 30)
    # Prompt for item details.
    item_code = input("Enter the item code: ").upper().strip()
    item_name = input("Enter the name of item:").upper().strip()
    item_supplier_code = input("Enter the item supplier code: ").upper().strip()
    item_last_supply_date = date_time()
    item_last_distribute_date = date_time()
    item_details = f'{item_code},{item_name},{item_supplier_code},100,{item_last_supply_date},{item_last_distribute_date}'.strip()
    # Check if the supplier code is registered.
    with open('suppliers.txt', 'r') as supplier_f:
        count = 0
        for supplier in supplier_f:
            count += 1
            if supplier.startswith(item_supplier_code):
                supplier_found = True
                continue
            elif not supplier_found and count >= supp_line:
                print('Sorry,The Supplier You Type Not Registered,Please Type Again')
                admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                break
    # Check if the item already exists.
    with open("ppe.txt", "r") as read_ppe:
        lines = read_ppe.readlines()
    for convert in lines:
        item_detail = convert.replace("\n", "").split(",")
        if item_code == item_detail[0] and item_name == item_detail[1]:
            item_exist = True
    if item_exist:
        print('Item already exist')
    # Add the item if it doesn't exist.
    elif not item_exist:
        print(
            f'Item Code:{item_code}   Item Name:{item_name}    Item Supplier Code:{item_supplier_code}')
        confirm = input('Are You Sure To Add This Item? (Y/N): ').upper().strip()
        if confirm == 'Y':
            print('Item Added')
            with open("ppe.txt", "a") as file:
                file.write(item_details + "\n")
        else:
            print('Item Adding Fail....')
    # Ask if the user wants to add another item.
    choice = input(" Add Another Item?(y/n): ")
    if choice == "n":
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    elif choice == "y":
        add_inventory(user_list, supplier_list, inventory_list, hospital_list)


def less_25(user_list, supplier_list, inventory_list, hospital_list):
    count = 0
    item_less_25 = False
    # Read the 'ppe.txt' file.
    with open('ppe.txt', 'r') as check:
        line = len(check.readlines())
        check.seek(0)
        # Iterate through the items.
        for item in check:
            count += 1
            item_info = item.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item_info
            # If the quantity is less than 25 boxes.
            if int(item_quantity) < 25:
                item_less_25 = True
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity} boxes\n")
    # If all items have been checked and none have less than 25 boxes.
    if count >= line and not item_less_25:
        print('All The Items In our Inventory Is More Than 25 Boxes')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_user(user_list, supplier_list, inventory_list, hospital_list):
    # Display search user page.
    print("\nSearch User Page")
    print('==' * 30)
    # Prompt for the user ID to be searched.
    search_user_code = input("Search User ID: ").upper().strip()
    found = False
    # Flag to indicate if user is found.

    # Iterate through user list.
    for user_info in user_list:
        if search_user_code == user_info[0]:
            # If user is found, display their information.
            found = True
            print("User ID: ", user_info[0])
            print("User Name: ", user_info[1])
            print("User User Password: ", user_info[2])
            print("User Type: ", user_info[3])
            break

    if not found:
        print("\nUser Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_hospital(user_list, supplier_list, inventory_list, hospital_list):
    # Display search hospital page.
    print("\nSearch Hospital Page")
    print('==' * 30)
    # Prompt for the hospital code to be searched.
    search_hospital_code = input("Search Hospital Code: ").upper().strip()
    found = False
    # Flag to indicate if hospital is found.

    # Iterate through hospital list.
    for hospital in hospital_list:
        hospital_details = hospital.split(',')
        if search_hospital_code == hospital_details[0]:
            # If hospital is found, display its information.
            found = True
            print("Hospital Code: ", hospital_details[0])
            print("Hospital Name: ", hospital_details[1])
            print("Hospital Phone Number: ", hospital_details[2])
            print("Hospital Email: ", hospital_details[3])
            print("Last Distribute Date: ", hospital_details[4])
            break

    if not found:
        print("\nHospital Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_supplier(user_list, supplier_list, inventory_list, hospital_list):
    # Display search supplier page.
    print("\nSearch Supplier Page")
    print('==' * 30)

    # Prompt for the supplier code to be searched.
    search_supplier_code = input("Search Supplier Code:").upper().strip()
    # Flag to indicate if supplier is found.
    found = False
    # Iterate through supplier list.
    for supplier in supplier_list:
        supplier_details = supplier.split(',')
        if search_supplier_code == supplier_details[0]:
            # If supplier is found, display its information.
            found = True
            print("Supplier Code: ", supplier_details[0])
            print("Supplier Name: ", supplier_details[1])
            print("Supplier Phone Number: ", supplier_details[2])
            print("Supplier Email: ", supplier_details[3])
            print("Last Supply Date: ", supplier_details[4])
            break

    if not found:
        print("\nSupplier Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_items(user_list, supplier_list, inventory_list, hospital_list):
    # Display search items page.
    print("\nSearch Items Page")
    print('==' * 30)
    # Prompt for the item code to be searched.
    search_item_code = input("Search Item Code: ").upper().strip()
    # Flag to indicate if item is found.
    found = False
    # Iterate through inventory list.
    for item in inventory_list:
        item_details = item.split(',')
        if search_item_code == item_details[0]:
            # If item is found, display its information.
            found = True
            print("Item Code: ", item_details[0])
            print("Item Name: ", item_details[1])
            print("Item Supplier Code: ", item_details[2])
            print("Item Quantity: ", item_details[3])
            print("Last Supply Date: ", item_details[4])
            print("Last Distribute Date: ", item_details[5])
            break

    if not found:
        print("\nItem Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def track_filter_date(user_list, supplier_list, inventory_list, hospital_list):
    # Prompt the user to choose between supply, distribute, or both.
    s_or_d_or_b = input('\nPlease Enter Filter Type:\n'
                        '"s" Supply\n'
                        '"d" Distribute\n'
                        '"b" Both\n> ')
    # Check if the input is valid, otherwise ask again or return to the main menu.
    if s_or_d_or_b.lower().strip() not in ['s', 'd', 'b']:
        print("\nPlease Type In The Correct Format !\n")
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Try to get valid start and end dates from the user.
    try:
        start_date_input = input('\nPlease Enter Start Date with the format "yyyy mm dd"\n>')
        end_date_input = input('\nPlease Enter End Date with the format "yyyy mm dd"\n>')
        start_date = datetime.datetime.strptime(start_date_input, "%Y %m %d")
        end_date = datetime.datetime.strptime(end_date_input, "%Y %m %d")
    except:
        print('Sorry,I Dont Understand!\n Please Type with the format "yyyy mm dd" Ex:2023 10 01\n')
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Open the transaction file and process the records.
    with open('transaction.txt', "r") as file:
        for line in file:
            transaction_details = line.strip().split(',')
            s_or_d, item_code, supplier_code, remaining_quantity, quantity_change, date_change = transaction_details
            date_change = datetime.datetime.strptime(date_change, '%a %b %d %X %Y')
            # Check if the transaction matches the user's choice and date range.
            if s_or_d_or_b == 's':
                if s_or_d.strip() == 'supply':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'Type:{s_or_d}     Item Code:{item_code}       SupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                              f'        Date:{date_change}\n{"=="*30}')
            elif s_or_d_or_b == 'd':
                if s_or_d.strip() == 'distribute':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'Type:{s_or_d}       Item Code:{item_code}       SupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                              f'        Date:{date_change}\n{"=="*30}')
            elif s_or_d_or_b == 'b':
                if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                    print(f'Type:{s_or_d}       Item Code:{item_code}       SupplierCode:{supplier_code}'
                          f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                          f'        Date:{date_change}\n{"=="*30}')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_main_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the staff menu repeatedly
    while True:
        print('Staff Menu')
        print('=' * 30)
        print("1.  Supplier")
        print("2.  Hospital")
        print("3.  Inventory")
        print("4.  Search Features")
        choice = input("Enter your choice: ")
        # Based on user's choice, call respective functions or display error message.
        if choice == '1':
            staff_supplier_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            staff_hospital_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            staff_search_function(user_list, supplier_list, inventory_list, hospital_list)
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I don't Understand, please type again")
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_supplier_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the supplier menu.
    while True:
        print("1.  Add Supplier")
        print("2.  Delete Supplier")
        print("3.  Modify Supplier Data")
        print("4.  Supplier Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        # Get user's choice.
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or take appropriate action.
        if choice == '1':
            staff_add_supp(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            staff_delete_supp()

        elif choice == '3':
            staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            staff_supplier_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '6':
            exit()
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_hospital_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the hospital menu.
    while True:
        print("1.  Add Hospital")
        print("2.  Delete Hospital")
        print("3.  Modify Hospital Data")
        print("4.  Hospital Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        # Get user's choice.
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or take appropriate action.
        if choice == '1':
            staff_add_hospital(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            staff_delete_hospital()

        elif choice == '3':
            staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            staff_hospital_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '6':
            exit()
        # If the choice is not recognized, display an error message.
        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list):
    # Loop for displaying the inventory menu repeatedly.
    while True:
        print("1.  Inventory Supply(+)")
        print("2.  Inventory Distribute(-)")
        print("3.  Modify Inventory Data")
        print("4.  Summary Inventory")
        print("5.  Delete Inventory")
        print("6.  Add New Inventory")
        print("7.  Inventory Quantity < 25")
        print("8.  Main Menu")
        print("9.  Exit")
        # Get user's choice
        choice = input("Enter your choice: ")
        print("==" * 30)
        # Based on user's choice, call respective functions or display error message.
        if choice == '1':
            staff_supply(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            staff_distribute(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            staff_inventory_summary(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            staff_delete_item()

        elif choice == '6':
            staff_add_inventory(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '7':
            staff_less_25(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '8':
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '9':
            exit()
        # If the choice is not recognized, display an error message
        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_function(user_list, supplier_list, inventory_list, hospital_list):
    # Display the search page menu.
    print("Search Page")
    print("1. Search Items")
    print("2. Search Supplier")
    print("3. Search Hospital")
    print("4. Transaction Record")
    print("5. Main menu ")
    print("6. Exit ")
    # Get user's choice.
    choice = input("Enter your choice: ")
    # Based on user's choice, call respective search functions.
    if choice == "1":
        staff_search_items(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "2":
        staff_search_supplier(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "3":
        staff_search_hospital(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "4":
        staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "5":
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '6':
        exit()


    print('==' * 30)


def staff_add_supp(user_list, supplier_list, inventory_list, hospital_list):
    # Initialize a flag to check if the supplier already exists.
    supp_exist = False
    # Read all records from the suppliers file.
    with open("suppliers.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    # Calculate the number of available slots for new suppliers.
    num = 4 - len(allrec)
    # Check if the supplier list is full.
    if num <= 0:
        print("Supplier Full")
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Continue adding new suppliers if there are available slots.
    while num >= 0:
        print("Add New Supplier")
        print('==' * 30)
        # Get supplier details from user input.
        supp_code = input("Enter The Supplier Code: ").strip().upper()
        supp_name = input("Enter The Name Of Supplier:").strip().upper()
        supp_phone_number = input("Enter The Phone Number Of The Supplier: ").strip()
        supp_mail = input("Enter The Email  Of The Supplier: ").strip()
        last_supply_date = date_time()
        supp_details = f'{supp_code},{supp_name},{supp_phone_number},{supp_mail},{last_supply_date}\n'
        num = num - 1
        # Check if the new supplier already exists in the records.
        with open("suppliers.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for convert in lines:
            supp_detail = convert.replace("\n", "").split(",")
            if supp_code == supp_detail[0] and supp_name == supp_detail[1]:
                supp_exist = True
        # Handle cases where the supplier already exists or not.
        if supp_exist:
            print('Supplier Exist')
        elif not supp_exist:
            print(
                f'Supplier Code:{supp_code}   Supplier Name:{supp_name}   Supplier Phone Number:{supp_phone_number}    '
                f'Supply Email:{supp_mail}    Last Supply Date:{last_supply_date}\n')
            confirm = input('Are You Sure You Want To Add This Supplier? (Y/N)').upper().strip()
            if confirm == 'Y':
                with open('suppliers.txt', 'a') as supp_f:
                    supp_f.write(supp_details)
                    print('Supplier Added')

            else:
                print('Supplier Add Failed')
        # Ask if the user wants to add another supplier
        choice = input("Add Another Supplier (y/n):").lower().strip()
        if choice == "n":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            staff_add_supp(user_list, supplier_list, inventory_list, hospital_list)


def staff_delete_supp():
    # Display delete supplier page.
    print('Delete Supplier Page')
    # Get supplier code from user input.
    supp_code = input("Enter Supplier Code : ").upper().strip()
    # Read all lines from the suppliers file.
    with open("suppliers.txt", "r") as file:
        lines = file.readlines()
    # Open the suppliers file for writing.
    with open("suppliers.txt", "w") as supplier_f:
        for line in lines:
            # Write all lines except the one starting with the specified supplier code.
            if not line.startswith(supp_code):
                supplier_f.write(line)

    print("Supplier Deleted")


def staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list):
    # Display modification options for suppliers.
    print("Modify Supplier Page")
    print('=' * 30)
    # Get the supplier code from user input.
    supplier_code = input('Supplier Code:').upper().strip()
    count = 0
    supplier_found = False
    # Count total lines in the suppliers file.

    with open('suppliers.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Search for the supplier by code.
    with open('suppliers.txt', 'r') as check:
        for supplier in check:
            count += 1
            # If supplier found, display information and ask for confirmation.
            if supplier.startswith(supplier_code):
                supplier = supplier.strip().split(',')
                print(
                    f'Supplier Code:{supplier[0]}   Supplier Name:{supplier[1]}   Supplier Phone Number:{supplier[2]}    Supply Email:{supplier[3]}    '
                    f'Last Supply Date:{supplier[4]}\n')
                confirm = input('Is This Supplier You Need To edit? Y/N:').upper().strip()
                # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                if confirm == 'Y':
                    supplier_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If count exceeds total lines and supplier not found, give options to retry or return to main menu.
            elif count >= line and not supplier_found:
                print('Supplier Not Found')
                confirm3 = input('1. Type Again\n2. Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # If supplier found, display modification options.
    if supplier_found:
        print("1. Change Supplier Code")
        print("2. Change Supplier Name")
        print("3. Change Supplier Email")
        print("4. Change Supplier Phone Number")
        choice = input("Enter your choice: ")
        # Read all lines in the suppliers file.
        with open('suppliers.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()
        # Open the suppliers file for writing.
        with open('suppliers.txt', 'w') as edit_quantity:
            for suppliers in lines:
                if suppliers.startswith(supplier_code):
                    supplier_info = suppliers.strip().split(',')
                    # Handle different modification options
                    if choice == '1':
                        sup_code = input('Please Type New Supplier Code:').upper().strip()
                        supplier_info[0] = sup_code
                    elif choice == '2':
                        sup_name = input('Please Type New Supplier Name:').upper().strip()
                        supplier_info[1] = sup_name
                    elif choice == '3':
                        sup_email = input('Please Type New Email:').strip()
                        supplier_info[3] = sup_email
                    elif choice == '4':
                        sup_number = input('Please Type New Phone Number:').strip()
                        supplier_info[2] = sup_number

                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        edit_quantity.write(','.join(supplier_info) + "\n")
                        staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                    # Print updated information and write it back to the file.
                    print(f'After Update...\n'
                          f'Supplier Code:{supplier_info[0]}   Supplier Name:{supplier_info[1]}   Supplier Phone Number:{supplier_info[2]}     Supplier Email:{supplier_info[3]}    '
                          f'Last Supply Date:{supplier_info[4]}\n')
                    print('Supplier Info Successfully Changed!')
                    edit_quantity.write(','.join(supplier_info) + "\n")

                else:
                    # If supplier not found, write it back to the file.
                    edit_quantity.write(suppliers)


def staff_supplier_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Open and read the supplier file
    with open('suppliers.txt', 'r') as read_supplier:
        for line in read_supplier:
            # Extract supplier details from each line
            line = line.strip().split(',')
            # Print supplier information
            print(f'Supplier Code:{line[0]}     Supplier Name:{line[1]}     Supplier Phone Number:{line[2]}     '
                  f'Supplier Email:{line[3]}      Last Supply Date:{line[4]} ')
    # Ask for user's choice
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_add_hospital(user_list, supplier_list, inventory_list, hospital_list):
    hosp_exist = False
    # Read all records from the hospital file.
    with open("hospital.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    num = 4 - len(allrec)
    if num == 0:
        print('Hospital Full')
    while num != 0:
        print("Add Hospital Page")
        print('==' * 30)
        # Get hospital details from user input.
        hospital_code = input("Enter the hospital code: ").upper().strip()
        hospital_name = input("Enter the name of hospital:").upper().strip()
        hospital_email = input("Enter the Email of the hospital: ").strip()
        hospital_phone_number = input("Enter the phone number of the hospital: ").strip()
        last_distribute_date = date_time()
        # Format hospital details for writing to file.
        hospital_details = f'{hospital_code},{hospital_name},{hospital_phone_number},{hospital_email},{last_distribute_date}'
        num = num - 1
        with open("hospital.txt", "r") as read_hosp:
            lines = read_hosp.readlines()
        for convert in lines:
            hosp_detail = convert.replace("\n", "").split(",")
            if hospital_code == hosp_detail[0] and hospital_name == hosp_detail[1]:
                hosp_exist = True
        if hosp_exist:
            print('Hospital already exist')
        elif not hosp_exist:
            print(
                f'Hospital Code:{hospital_code}   Hospital Name:{hospital_name}   Hospital Phone Number:{hospital_phone_number}    Hospital Email:{hospital_email}')
            confirm = input('Are You Sure To Add This Hospital? (Y/N): ').upper().strip()
            if confirm == 'Y':
                print('Hospital Added')
                with open("hospital.txt", "a") as file:
                    file.write(hospital_details + "\n")
            else:
                print('Hospital Adding Fail....')
        # Ask if the user wants to add another hospital.
        choice = input(" Add Another Hospital?(y/n): ")
        if choice == "n":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            staff_add_hospital(user_list, supplier_list, inventory_list, hospital_list)


def staff_delete_hospital():
    # Display delete hospital page.
    print('Delete Hospital Page')
    # Get hospital code from user input.
    hospital_code = input("Enter Hospital Code : ").upper().strip()
    # Read all lines from the hospital file.
    with open("hospital.txt", "r") as file:
        lines = file.readlines()
    # Open the hospital file for writing.
    with open("hospital.txt", "w") as hospital_f:
        for line in lines:
            # Write all lines except the one starting with the specified hospital code.
            if not line.startswith(hospital_code):
                hospital_f.write(line)

    print("Hospital Deleted")


def staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list):
    # Display modification options for hospitals.
    print("Modify Hospital Page")
    print('=' * 30)
    # Get the hospital code from user input.
    hospital_code = input('Hospital Code:').upper().strip()
    count = 0
    hospital_found = False
    # Count total lines in the hospital file.
    with open('hospital.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Search for the hospital by code.
    with open('hospital.txt', 'r') as check:
        for hospitals in check:
            count += 1
            # If hospital found, display information and ask for confirmation.
            if hospitals.startswith(hospital_code):
                hospitals = hospitals.strip().split(',')
                print(
                    f'Hospital Code:{hospitals[0]}   Hospital Name:{hospitals[1]}   Hospital Phone Number:{hospitals[3]}       Hospital Email:{hospitals[2]}'
                    f'Last Distribute Date:{hospitals[4]}\n')
                confirm = input('Is This Hospital Information You Need To edit? Y/N:').upper().strip()
                # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                if confirm == 'Y':
                    hospital_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If count exceeds total lines and hospital not found, give options to retry or return to main menu.
            elif count >= line and not hospital_found:
                print('Hospital Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    # If hospital found, display modification options.
    if hospital_found:
        print("1. Change Hospital Code")
        print("2. Change Hospital Name")
        print("3. Change Hospital Email")
        print("4. Change Hospital Phone Number")
        print("5. Back")
        choice = input("Enter your choice: ")
        # Read all lines in the hospital file.
        with open('hospital.txt', 'r') as check_lines:
            lines = check_lines.readlines()
        # Open the hospital file for writing.
        with open('hospital.txt', 'w') as hospital_f:
            for hospital in lines:
                if hospital.startswith(hospital_code):
                    hospital_info = hospital.strip().split(',')
                    # Handle different modification options.
                    if choice == '1':
                        new_code = input('Please Type The New Hospital Code:').upper().strip()
                        hospital_info[0] = new_code
                    elif choice == '2':
                        new_hospital_name = input('Please Type The New Hospital Name:').upper().strip()
                        hospital_info[1] = new_hospital_name
                    elif choice == '3':
                        new_email = input('Please Type The New Hospital Email:').upper().strip()
                        hospital_info[2] = new_email
                    elif choice == '4':
                        new_phone_number = input('Please Type The New Hospital Number:').upper().strip()
                        hospital_info[3] = new_phone_number
                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                    # Print updated information and write it back to the file.
                    print(f'After Update...\n'
                          f'Hospital Code:{hospital_info[0]}   Hospital Name:{hospital_info[1]}   Hospital Email:{hospital_info[2]}    '
                          f'Hospital Phone Number:{hospital_info[3]}      Last Supply Date:{hospital_info[4]}\n')
                    print('Item Successfully Updated!')
                    hospital_f.write(','.join(hospital_info) + "\n")

                else:
                    # If hospital not found, write it back to the file.
                    hospital_f.write(hospital)
    # Return to the main menu.
    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_hospital_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Open and read the hospital file
    with open('hospital.txt', 'r') as read_hospital:
        for line in read_hospital:
            # Extract hospital details from each line
            line = line.strip().split(',')
            # Print hospital information
            print(f'Hospital Code:{line[0]}     Hospital Name:{line[1]}     Hospital Phone Number:{line[2]}'
                  f'Hospital Email:{line[3]}      Last Distribute Date:{line[4]} ')
    # Ask for user's choice
    choice = input('1.Main Menu\n2.Exit\nEnter Your Choice:').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_supply(user_list, supplier_list, inventory_list, hospital_list):
    # Display supply page header.
    print('Supply Page')
    print('==' * 30)
    # Get item code from user input and clean it.
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    item_found = False
    # Get the total number of lines in the inventory file.
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Check each line in the inventory file.
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            # If the line starts with the specified item code.
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}    Supplier Code:{items[2]}'
                    f'    Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                # If user confirms the item details
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    # If user chooses to type the item code again.
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_supply(user_list, supplier_list, inventory_list, hospital_list)
                    # If user chooses to return to the main menu.
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If the item is not found and we've checked all lines.
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                # If user chooses to type the item code again.
                if confirm3.strip() == '1':
                    staff_supply(user_list, supplier_list, inventory_list, hospital_list)
                # If user chooses to return to the main menu.
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                else:
                    print("Sorry I Don't Understand")

                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if item_found:
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                    item_quantity = int(item_info[3])
                    quantity_changes = int(input('Quantity(Boxes):'))
                    item_info[3] = str(item_quantity + quantity_changes)
                    item_info[5] = date_time()
                    print(f'After Update...\n'
                          f'Item Code:{item_code}   Item Name:{item_name}   Item Quantity:{item_info[3]}    '
                          f'Last Supply Date:{item_info[5]}\n')
                    print('Item Successfully Updated!')
                    with open('suppliers.txt', 'r') as file:
                        lines = file.readlines()
                    # Update the supplier's last supply date.
                    with open('suppliers.txt', 'w') as file:
                        for sup in lines:
                            if sup.startswith(item_supplier):
                                sup = sup.strip().split(',')
                                sup[4] = date_time()
                                file.write(','.join(sup) + '\n')
                            else:
                                file.write(sup)
                    # Log the transaction.
                    with open('transaction.txt', 'a') as trans:
                        trans.write(f'{"supply"}'
                                    f',{item_code},{item_supplier},{item_info[3]},{quantity_changes},{date_time()}\n')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)
    # Ask user if they want to continue adding items.
    choice = input('Continue Add Item? Y/N:').strip().upper()
    if choice == 'Y':
        staff_supply(user_list, supplier_list, inventory_list, hospital_list)
    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_distribute(user_list, supplier_list, inventory_list, hospital_list):
    # Display distribute page header.
    print('Distribute Page')
    print('==' * 30)
    # Get item code from user input and clean it.
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    count2 = 0
    item_found = False
    # Get the total number of lines in the inventory and hospital files.
    with open('ppe.txt', 'r') as file_line, open('hospital.txt', 'r') as hospital_file:
        line = len(file_line.readlines())
        hospital = len(hospital_file.readlines())
    # Check each line in the inventory file.
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            # If the line starts with the specified item code.
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}    '
                      f'Last Distribute Date:{items[5]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    # If user chooses to type the item code again.
                    if confirm2.strip() == '1':
                        staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                    # If user chooses to return to the main menu.
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If the item is not found and we've checked all lines
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                # If user chooses to type the item code again.
                if confirm3.strip() == '1':
                    staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                # If user chooses to return to the main menu.
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    if item_found:
        hospital_code = input('Please Type The Hospital Code:')
        hospital_code = hospital_code.upper().strip()
        hospital_found = False
        # Check each line in the hospital file.
        with open('hospital.txt', 'r') as check:
            for hospitals_line in check:
                count2 += 1
                # If the line starts with the specified hospital code.
                if hospitals_line.startswith(hospital_code):
                    hospitals_line = hospitals_line.strip().split(',')
                    print(f'Hospital Code:{hospitals_line[0]}   Hospital Name:{hospitals_line[1]}   '
                          f'Last Distribute Date:{hospitals_line[4]}\n')
                    confirm = input('Is This Hospital Detail Correct? Y/N:')
                    # If user confirms the hospital details.
                    if confirm.upper().strip() == 'Y':
                        hospital_found = True
                        continue
                    elif confirm.upper().strip() == 'N':
                        confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                        # If user chooses to type the hospital code again.
                        if confirm2.strip() == '1':
                            staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirm2.strip() == '2':
                            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                # If the hospital is not found and we've checked all lines.
                elif not hospital_found and count2 >= hospital:
                    print('Hospital Not Found')
                    confirm4 = input('1. Type Again\n2.Return To Main Menu\n>')
                    # If user chooses to type the hospital code again.
                    if confirm4.strip() == '1':
                        staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm4.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if item_found and hospital_found:
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                lines = item
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                    quantity_changes = int(input('Quantity(Boxes):'))
                    item_quantity = int(item_info[3])
                    int(item_quantity)
                    new_quantity = item_quantity - quantity_changes
                    # If the quantity to distribute is more than available.
                    if new_quantity <= 0:
                        print(f'The available quantity is {item_quantity} boxes, not enough to distribute.')
                        confirmation = input('1.Retype\n2.Main Menu\n>')
                        # If user chooses to retype the quantity.
                        if confirmation == '1':
                            edit_quantity.write(','.join(item_info) + "\n")
                            staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirmation == '2':
                            edit_quantity.write(','.join(item_info) + "\n")
                            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    else:
                        item_info[3] = str(item_quantity - quantity_changes)
                        item_info[5] = date_time()
                        print(f'After Update...\n'
                              f'Item Code:{item_code}   Item Name:{item_name}   Item Quantity:{item_info[3]}    '
                              f'Last Distribute Date:{item_info[5]}\n')
                        print('Item Successfully Updated!')
                        # Log the transaction.
                        with open('transaction.txt', 'a') as trans:
                            trans.write(f'{"distribute"}'
                                        f',{item_code},{hospital_code},{item_info[3]},{quantity_changes},{date_time()}\n')
                        # Update the hospital's last distribute date.
                        with open('hospital.txt', 'r') as file:
                            lines = file.readlines()

                        with open('hospital.txt', 'w') as file:
                            for hos in lines:
                                if hos.startswith(hospital_code):
                                    hos = hos.strip().split(',')
                                    hos[4] = date_time()
                                    file.write(','.join(hos) + '\n')
                                else:
                                    file.write(hos)
                    edit_quantity.write(','.join(item_info) + "\n")
                else:
                    edit_quantity.write(item)
    choice = input('Continue Distribute Item? Y/N').strip().upper()
    if choice == 'Y':
        staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list):
    # Display modification options for inventory items.
    print("Modify Inventory Page")
    print('=' * 30)
    # Get the item code from user input.
    item_change = input('Item code:').upper().strip()
    count = 0
    item_found = False
    # Count total lines in the inventory file.
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    # Search for the item by code.
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            # If item found, display information and ask for confirmation.
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}  Supply Code:{items[2]}9  '
                    f'Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item You Need To edit? Y/N:').upper().strip()
                # If user confirms, set flag and continue. Otherwise, give options to retry or return to main menu.
                if confirm == 'Y':
                    item_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            # If count exceeds total lines and item not found, give options to retry or return to main menu.
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # If item found, display modification options.
    if item_found:
        print("1. Change Item Code")
        print("2. Change Item Name")
        print("3. Change Item's Supplier Code")
        print("4. Back")
        choice = input("Enter your choice: ")
        # Read all lines in the inventory file.
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()
        # Open the inventory file for writing.
        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    # Handle different modification options.
                    if choice == '1':
                        new_code = input('Please Type Your New Item Code:').upper().strip()
                        item_info[0] = new_code
                    elif choice == '2':
                        new_name = input('Please Type Your New Item Name:').upper().strip()
                        item_info[1] = new_name
                    elif choice == '3':
                        supplier_found = False
                        count = 0
                        new_supplier_code = input('Please Type The New Item Supplier Item Code:').upper().strip()
                        # Search for the new supplier code in the suppliers file.
                        with open('suppliers.txt', 'r') as supplier_f:
                            for supplier in supplier_f:
                                count += 1
                                # If found, update the item's supplier code.
                                if supplier.startswith(new_supplier_code):
                                    supplier_found = True
                                    item_info[2] = new_supplier_code
                                # If not found and count exceeds total lines, give an error message.
                                elif not supplier_found and count >= line:
                                    print("Sorry The Supplier You Type Haven't Register")
                                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    # Print updated information and write it back to the file.
                    print(f'After Update...\n'
                          f'Item Code:{item_info[0]}   Item Name:{item_info[1]}   Item Quantity:{item_info[3]}     Supply Code:{item_info[2]}    '
                          f'Last Supply Date:{item_info[5]}\n')
                    print('Item Successfully Updated!')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    # If item not found, write it back to the file.
                    edit_quantity.write(item)


def staff_inventory_summary(user_list, supplier_list, inventory_list, hospital_list):
    # Initialize an empty list to store all records.
    all_record = []
    count = 0
    # Read the 'ppe.txt' file and populate the all_record list.
    with open('ppe.txt', 'r') as list:
        for line in list:
            all_record.append(line.strip().split(','))
        # Sort the records based on quantity in ascending order.
        for x in range(len(all_record) - 1):
            for y in range(x, len(all_record)):
                if int(all_record[x][3]) > int(all_record[y][3]):
                    temp = all_record[x]
                    all_record[x] = all_record[y]
                    all_record[y] = temp
    # Print the inventory summary.
    for i in range(len(all_record)):
        print(
            f'Item Code:{all_record[i][0]}           Item Name:{all_record[i][1]}           Supplier Code:{all_record[i][2]}     Quantity:{all_record[i][3]} boxes \n'
            f'Last Supply Date:{all_record[i][4]}         Last Distribute Date:{all_record[i][5]}\n')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_delete_item():
    # Display delete item page.
    print('Delete Item Page')
    # Get item code from user input.
    item_code = input("Enter Item Code : ").upper().strip()
    # Read all lines from the inventory file
    with open("ppe.txt", "r") as file:
        lines = file.readlines()
    # Open the inventory file for writing.
    with open("ppe.txt", "w") as inventory_f:
        for line in lines:
            # Write all lines except the one starting with the specified item code.
            if not line.startswith(item_code):
                inventory_f.write(line)

    print("Item Deleted")


def staff_add_inventory(user_list, supplier_list, inventory_list, hospital_list):
    item_exist = False
    supplier_found = False
    # Get the total number of lines in the suppliers file.
    with open('suppliers.txt', 'r') as file_line:
        supp_line = len(file_line.readlines())
    # Read all records from the inventory file.
    with open("ppe.txt", "r") as file:
        allrec = []
        for read in file:
            rec = read.strip().split(",")
            allrec.append(rec)
    print("Add New Inventory Page")
    print('==' * 30)
    # Prompt for item details.
    item_code = input("Enter the item code: ").upper().strip()
    item_name = input("Enter the name of item:").upper().strip()
    item_supplier_code = input("Enter the item supplier code: ").upper().strip()
    item_last_supply_date = date_time()
    item_last_distribute_date = date_time()
    item_details = f'{item_code},{item_name},{item_supplier_code},100,{item_last_supply_date},{item_last_distribute_date}'.strip()
    # Check if the supplier code is registered.
    with open('suppliers.txt', 'r') as supplier_f:
        count = 0
        for supplier in supplier_f:
            count += 1
            if supplier.startswith(item_supplier_code):
                supplier_found = True
                continue
            elif not supplier_found and count >= supp_line:
                print('Sorry,The Supplier You Type Not Registered,Please Type Again')
                staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                break
    # Check if the item already exists.
    with open("ppe.txt", "r") as read_ppe:
        lines = read_ppe.readlines()
    for convert in lines:
        item_detail = convert.replace("\n", "").split(",")
        if item_code == item_detail[0] and item_name == item_detail[1]:
            item_exist = True
    if item_exist:
        print('Item already exist')
    # Add the item if it doesn't exist.
    elif not item_exist:
        print(
            f'Item Code:{item_code}   Item Name:{item_name}    Item Supplier Code:{item_supplier_code}')
        confirm = input('Are You Sure To Add This Item? (Y/N): ').upper().strip()
        if confirm == 'Y':
            print('Item Added')
            with open("ppe.txt", "a") as file:
                file.write(item_details + "\n")
        else:
            print('Item Adding Fail....')
    # Ask if the user wants to add another item.
    choice = input(" Add Another Item?(y/n): ")
    if choice == "n":
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    elif choice == "y":
        staff_add_inventory(user_list, supplier_list, inventory_list, hospital_list)


def staff_less_25(user_list, supplier_list, inventory_list, hospital_list):
    count = 0
    item_less_25 = False
    # Read the 'ppe.txt' file.
    with open('ppe.txt', 'r') as check:
        line = len(check.readlines())
        check.seek(0)
        # Iterate through the items.
        for item in check:
            count += 1
            item_info = item.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item_info
            # If the quantity is less than 25 boxes.
            if int(item_quantity) < 25:
                item_less_25 = True
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity} boxes\n")
    # If all items have been checked and none have less than 25 boxes.
    if count >= line and not item_less_25:
        print('All The Items In our Inventory Is More Than 25 Boxes')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_hospital(user_list, supplier_list, inventory_list, hospital_list):
    # Display search hospital page.
    print("\nSearch Hospital Page")
    print('==' * 30)
    # Prompt for the hospital code to be searched.
    search_hospital_code = input("Search Hospital Code: ").upper().strip()
    found = False
    # Flag to indicate if hospital is found.

    # Iterate through hospital list.
    for hospital in hospital_list:
        hospital_details = hospital.split(',')
        if search_hospital_code == hospital_details[0]:
            # If hospital is found, display its information.
            found = True
            print("Hospital Code: ", hospital_details[0])
            print("Hospital Name: ", hospital_details[1])
            print("Hospital Phone Number: ", hospital_details[2])
            print("Hospital Email: ", hospital_details[3])
            print("Last Distribute Date: ", hospital_details[4])
            break

    if not found:
        print("\nHospital Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_supplier(user_list, supplier_list, inventory_list, hospital_list):
    # Display search supplier page.
    print("\nSearch Supplier Page")
    print('==' * 30)
    # Prompt for the supplier code to be searched.
    search_supplier_code = input("Search Supplier Code:").upper().strip()
    # Flag to indicate if supplier is found.
    found = False
    # Iterate through supplier list.
    for supplier in supplier_list:
        supplier_details = supplier.split(',')
        if search_supplier_code == supplier_details[0]:
            # If supplier is found, display its information.
            found = True
            print("Supplier Code: ", supplier_details[0])
            print("Supplier Name: ", supplier_details[1])
            print("Supplier Phone Number: ", supplier_details[2])
            print("Supplier Email: ", supplier_details[3])
            print("Last Supply Date: ", supplier_details[4])
            break

    if not found:
        print("\nSupplier Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_items(user_list, supplier_list, inventory_list, hospital_list):
    # Display search items page.
    print("\nSearch Items Page")
    print('==' * 30)
    # Prompt for the item code to be searched.
    search_item_code = input("Search Item Code: ").upper().strip()
    # Flag to indicate if item is found.
    found = False
    # Iterate through inventory list.
    for item in inventory_list:
        item_details = item.split(',')
        if search_item_code == item_details[0]:
            # If item is found, display its information.
            found = True
            print("Item Code: ", item_details[0])
            print("Item Name: ", item_details[1])
            print("Item Supplier Code: ", item_details[2])
            print("Item Quantity: ", item_details[3])
            print("Last Supply Date: ", item_details[4])
            print("Last Distribute Date: ", item_details[5])
            break

    if not found:
        print("\nItem Not Found")
    # Prompt user for choice: go back to main menu or exit.
    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list):
    # Prompt the user to choose between supply, distribute, or both.
    s_or_d_or_b = input('\nPlease Enter Filter Type:\n'
                        '"s" Supply\n'
                        '"d" Distribute\n'
                        '"b" Both\n> ')
    # Check if the input is valid, otherwise ask again or return to the main menu.
    if s_or_d_or_b.lower().strip() not in ['s', 'd', 'b']:
        print("\nPlease Type In The Correct Format !\n")
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Try to get valid start and end dates from the user.
    try:
        start_date_input = input('\nPlease Enter Start Date with the format "yyyy mm dd"\n>')
        end_date_input = input('\nPlease Enter End Date with the format "yyyy mm dd"\n>')
        start_date = datetime.datetime.strptime(start_date_input, "%Y %m %d")
        end_date = datetime.datetime.strptime(end_date_input, "%Y %m %d")
    except:
        print('Sorry,I Dont Understand!\n Please Type with the format "yyyy mm dd" Ex:2023 10 01\n')
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    # Open the transaction file and process the records.
    with open('transaction.txt', "r") as file:
        for line in file:
            transaction_details = line.strip().split(',')
            s_or_d, item_code, supplier_code, remaining_quantity, quantity_change, date_change = transaction_details
            date_change = datetime.datetime.strptime(date_change, '%a %b %d %X %Y')
            # Check if the transaction matches the user's choice and date range.
            if s_or_d_or_b == 's':
                if s_or_d.strip() == 'supply':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'Type:{s_or_d}     Item Code:{item_code}       SupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                              f'        Date:{date_change}\n{"==" * 30}')
            elif s_or_d_or_b == 'd':
                if s_or_d.strip() == 'distribute':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'Type:{s_or_d}       Item Code:{item_code}       SupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                              f'        Date:{date_change}\n{"==" * 30}')
            elif s_or_d_or_b == 'b':
                if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                    print(f'Type:{s_or_d}       Item Code:{item_code}       SupplierCode:{supplier_code}'
                          f'\nRemaining Quantity:{remaining_quantity}       Quantity Change:{quantity_change}'
                          f'        Date:{date_change}\n{"==" * 30}')
    # Get user's choice for next action.
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

check_file()
