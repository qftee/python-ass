import datetime


def main_menu():
    pass


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def check_file():
    user_list = []
    supplier_list = []
    inventory_list = []
    hospital_list = []
    supplier = True
    inventory = True
    # Open and read the inventory file.
    try:
        with open("hospital.txt", "r") as hospital_file:
            hospital_file.seek(0)  # Reset the file pointer to the beginning
            for line in hospital_file:
                hospital_list.append(line.strip())

    except FileNotFoundError:
        with open("suppliers.txt", "a") as supp_data:
            # supp_info(supplier_list)
            supp_data.write("")

    try:
        with open("suppliers.txt", "r") as supp_file:
            if not supp_file.read():  # Check if the file is empty
                supplier = False
            else:
                supp_file.seek(0)  # Reset the file pointer to the beginning
                for line in supp_file:
                    supplier_list.append(line.strip())

    except FileNotFoundError:
        with open("suppliers.txt", "a") as supp_data:
            # supp_info(supplier_list)
            supp_data.write("")
            supplier = False

    try:
        with open("ppe.txt", "r") as ppe_file:
            if not ppe_file.read():
                inventory = False
            else:
                ppe_file.seek(0)
                for line in ppe_file:
                    inventory_list.append((line.strip()))

    except FileNotFoundError:
        with open("ppe.txt", "a") as ppe_data:
            inventory = False
            opening_cover()
            main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory)

    try:
        with open("users.txt", "r") as user_file:
            user_data = user_file.read
            if user_data == '':
                add_user(user_list)
            for line in user_file:
                line = line.strip().strip(":")
                user_list.append(line)
        # create a empty file

    except FileNotFoundError:
        with open("users.txt", "w") as user_data:
            user_data.write(' ')
            add_user(user_list)
    opening_cover()
    main_login_page(user_list, supplier_list, inventory_list, hospital_list, supplier, inventory)


def initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list):
    print("You're In Initial Creation Now")
    while True:
        supp_exist = False
        item_exist = False
        item_code = input("Enter the item code: ").strip().upper()
        item_name = input("Enter the item name: ").strip().upper()
        item_last_supply_date = date_time()
        item_last_distribute_date = date_time()
        item_supp_name = input("Enter the item supplier name: ").strip().upper()
        item_supp_code = input("Enter the item supplier code: ").strip().upper()
        supp_contact_number = input("Enter the phone number of the supplier: ").strip()
        supp_email = input("Enter the e-mail of the supplier: ").strip()
        item_details = f'{item_code},{item_name},{item_supp_code},100,{item_last_supply_date},{item_last_distribute_date}'.strip()
        supp_details = f'{item_supp_code},{item_supp_name},{supp_contact_number},{supp_email},{item_last_supply_date}'.strip()
        # will be empty after rerun the loop

        with open("suppliers.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for convert in lines:
            supp_detail = convert.replace("\n", "").split(",")
            if item_supp_code == supp_detail[0] and item_supp_name == supp_detail[1]:
                supp_exist = True

        with open('ppe.txt', 'r') as read_inventory:
            lines = read_inventory.readlines()
        for convert in lines:
                item_detail = convert.replace("\n", "").split(",")
                if item_code == item_detail[0] and item_name == item_detail[1]:
                    item_exist = True

            # xxx=true
            # for check, if xxx = true, else xxx = false
        if supp_exist and not item_exist:
            with open("ppe.txt", "a") as ppe_data:
                # inven_list.append(item_details)
                ppe_data.write(item_details + "\n")
            print("Supplier Exist, Add Inventory Only")
        elif item_exist and not supp_exist:
            with open('suppliers.txt','a') as supp_f:
                supp_f.write(supp_details + "\n")
            print("Inventory Exist, Add Supplier Only")
        elif not supp_exist and not item_exist:
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

        def get_choice():
            choice = input("Did you finish input the details of the inventory (y/n)?")
            if choice == "y":
                if user_login and staff_login:
                    print("Successfully entered staff page.")
                    staff_menu(user_list, supplier_list, inventory_list, hospital_list)
                elif user_login and admin_login:
                    print("Successfully entered admin page.")
                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif choice == "n":
                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)
            else:
                print('Invalid Input!,Type Again!')
                get_choice()

        get_choice()



def opening_cover():
    print("=" * 35)
    print("        Department Of Health       ")
    print("  Inventory Management System For  ")
    print("Personal Protective Equipment (PPE)")
    print("=" * 35)


def main_login_page(user_list, supplier_list, inventory_list, supplier, inventory, hospital_list):

    user_login = False
    admin_login = False
    staff_login = False
    print('Login Page')
    print('-'*30)
    user_id = input("Enter your user ID: ").strip().lower()
    user_pw = input("Enter your password: ").strip()

    for i in user_list:
        user_info = i.strip("\n").split(":")
        if user_id == user_info[0] and user_pw == user_info[2]:
            user_login = True
            break

    if user_login:
        if not supplier or not inventory:
            if user_info[3] == "admin":
                admin_login = True

                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)

            elif user_info[3] == "staff":
                staff_login = True

                initial_creation(user_login, admin_login, staff_login, user_list, supplier_list, inventory_list, hospital_list)
        else:
            if user_info[3] == "admin":
                print("Successfully entered admin page.")
                admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

            elif user_info[3] == "staff":
                print("Successfully entered staff page.")
                staff_menu(user_list, supplier_list, inventory_list, hospital_list)
    else:
        print("Logged in unsuccessful..")
        print('Please Type Again')
        main_login_page(user_list, supplier_list, inventory_list, supplier, inventory, hospital_list)


def admin_main_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print('Admin Menu')
        print('='*30)
        print("1.  User")
        print("2.  Supplier")
        print("3.  Hospital")
        print("4.  Inventory")
        print("5.  Search Features")
        choice = input("Enter your choice: ")
        if choice == '1':
            admin_user_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            admin_supplier_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            admin_hospital_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)
        else:
            print("Sorry I don't Understand, please type again")
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Inventory Supply(+)")
        print("2.  Inventory Distribute(-)")
        print("3.  Modify Inventory Data")
        print("4.  Summary Inventory")
        print("5.  Search Inventory")
        print("6.  Delete Inventory")
        print("7.  Main Menu")
        print("8.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)
        if choice == '1':
            supply(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            distribute(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            display_inventory_list(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '5':
            search_item(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '6':
            delete_item(inventory_list)

        elif choice == '7':
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '8':
            exit()

        else:
            print("Sorry I Don't Understand, Please Type Again")
            admin_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)



def admin_supplier_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Add Supplier")
        print("2.  Delete Supplier")
        print("3.  Modify Supplier Data")
        print("4.  Supplier Summary")
        print("5.  Search Supplier")
        print("6.  Main Menu")
        print("7.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)


def admin_hospital_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Add Hospital")
        print("2.  Delete Hospital")
        print("3.  Modify Hospital Data")
        print("4.  Hospital Summary")
        print("5.  Search Hospital")
        print("6.  Main Menu")
        print("7.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)


def admin_user_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Add user")
        print("2.  Delete user")
        print("3.  Modify User")
        print("4.  Search User")
        print("5.  Main Menu")
        print("6.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)
        # temp_list = []
        # with open("users.txt", "r") as user_f:
        #     lines = user_f.readlines()
        #     for line in lines:
        #         line = line.strip().split(":")
        #         temp_list.append(line)
        # user_list = temp_list
        # print(user_list)
        if choice == "1":
            add_user(user_list)

        if choice == "2":
            delete_user(user_list)

        if choice == "3":
            modify_user(user_list)

        if choice == "4":
            search_user(user_list)

        if choice == "5":
            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

        if choice == "6":
            exit()

def search_function(user_list, supplier_list, inventory_list, hospital_list):
    print("Search Page")
    print("1. Search user")
    print("2. Search items")
    print("3. Search user")
    print("4. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        search_user(user_list)

    if choice == "2":
        search_items(inventory_list)


def add_user(user_list):
    same_ID = False
    while True:
        print("Add user page.")
        user_ID = input("Enter the user ID: ")
        user_name = input("Enter the user name: ")
        user_pw = input("Enter the user password: ")
        user_type = input("Choose the type of user (admin / staff): ")
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type).lower()
        # user_list.append(user_details)
        with open("users.txt", "a") as user_f:
            print(user_list)
            for i in range(len(user_list)):
                print(user_ID)
                print(user_list[i][0])
                if user_ID == user_list[i][0]:
                    print("User ID have been used, please change another.")
                    # ask = input("Did you finish add new user (y/n)?")
                    # print("---" * 30)
                    # if ask == "y":
                    #     break
                    # if ask == "n":
                    #     continue
                    # ask = input("Did you finish add new user (y/n)?")
                    # print("---" * 30)
                    # if ask == "y":
                    #     break
                    # if ask == "n":
                    #     continue

                else:
                    user_f.write(user_details + "\n")
        ask = input("Did you finish add new user (y/n)?")
        print("---" * 30)

        if ask == "y":
            user_list.append(user_details)
            break
        if ask == "n":
            user_list.append(user_details)
            continue


def modify_user(user_list):
    # print modify menu
    print("Modify Page")
    print("1. Change User ID")
    print("2. Change User Name")
    print("3. Change User Password")
    print("4. Change User Type")
    # user need to do a option
    choice = input("Enter your choice: ")
    # if the option is 1, will do a change name
    if choice == "1":
        print("Change User ID Page")
        print('='*30)
        search_userID = input("Enter the user id you want to search:")
        with open("users.txt", "w") as user_f:
            for i in user_list:
                # print(i)
                print(i)
                if search_userID == i[0]:
                    print("Old user name: ", i[1])
                    new_id = input("Enter Your New User Name: ")
                    # i[1] = new_name
                    i[1] = new_id
                    print("Name Change Successful.....")
                    # join ":" into the file to separate it.
                    # user_f.write(":".join(user_list[i]) + "\n")

                    user_f.write(":".join(i) + "\n")

                    print(user_list)
                # for i in range(len(user_list)):
                else:
                    user_f.write(":".join(i) + "\n")
        return

    if choice == "2":
        print("Change user password.")
        search_userID = input("Enter the userID you want to search: ")
        with open("users.txt", "w") as user_f:
            for i in user_list:
                if search_userID == i[0]:
                    old_pw = input("Enter your old password: ")
                    if old_pw == i[2]:
                        new_pw = input("Enter your new password: ")
                        i[2] = new_pw
                        # user_list = temp_list
                        print("Password change successful....")
                        user_f.write(":".join(i) + "\n")
                    else:
                        user_f.write(":".join(i) + "\n")
                else:
                    user_f.write(":".join(i) + "\n")

    if choice == "3":
        print("Change user Type.")
        search_userID = input("Enter the userID you want to search: ")
        with open("users.txt", "w") as user_f:
            for i in user_list:
                if search_userID == i[0]:
                    print("The user type for this user ID is: ", i[3])
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
                    print("The userID does not match and the user type cannot be changed.")
                    user_f.write(":".join(i) + "\n")


def search_user(user_list):
    userfound = False
    print("Search user page")
    print(user_list)
    search_userID = input("Enter the user ID you want to search: ")
    print(user_list)
    with open("users.txt", "r") as user_read:
        # read = user_read.read()
        for i in user_list:
            if search_userID == i[0]:
                userfound = True
                if userfound:
                    print("User ID: ", i[0])
                    print("User name: ", i[1])
                    print("User password: ", i[2])
                    print("User Type: ", i[3])
                    print("————" * 30)
                    break
                else:
                    print("The user was not found. Please try again.")
                break


def search_items(inventory_list):
    print("Search items page")
    search_item_code = input("Enter the items code you want to search: ")
    for i in range(len(inventory_list)):
        if search_item_code == inventory_list[i][0]:
            print("Item code: ", inventory_list[i][0])
            print("Item name: ", inventory_list[i][1])
            print("Item quantity: ", inventory_list[i][2])
            print("Item supplier: ", inventory_list[i][3])
            print("Item supplier code: ", inventory_list[i][4])
            break

        else:
            print("This item was not found.")
            return


def supp_info(supplier_list):
    print("Supplier information page.")
    print("1. Add supplier")
    print("2. Modify supplier")
    print("3. Delete supplier")
    print("4. Back")
    choice = input("Enter your choice: ")
    with open("suppliers.txt", "r") as supp_f:
        for line in supp_f:
            supp_data = line.strip().split(",")
            supplier_list.append(supp_data)
    if choice == "1":
        add_supp()

    if choice == "2":
        modify_supp(supplier_list)

    if choice == "3":
        delete_supp(supplier_list)

    if choice == "4":
        return


def add_supp():
    with open("suppliers.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    num = 4 - len(allrec)
    while num != 0:
        print("Add new supplier")
        print(allrec)
        supp_code = input("Enter the supplier code: ")
        supp_name = input("Enter the name of supplier:")
        supp_phonenum = input("Enter the phone number of the supplier: ")
        supp_mail = input("Enter the mail box of the supplier: ")
        last_supply_date = date_time()
        supp_details = f'{supp_code},{supp_name},{supp_phonenum},{supp_mail},{last_supply_date}'
        num = num - 1
        # if supp_code != rec[0]:
        # else:
        # print("Supplier have been taken")
        choice = input("Did you finish input the details of the inventory (y/n)?")
        if choice == "y":
            break

        if choice == "n":
            with open("suppliers.txt", "a") as file:
                file.write(supp_details + "\n")
    print("supplier full")


def modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list):
    print("Modify Inventory Page")
    print('=' * 30)
    item_change = input('Item code:').upper().strip()
    count = 0
    item_found = False
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[2]}    Supply Code:{items[3]}    '
                    f'Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item You Need To edit? Y/N:').upper().strip()
                if confirm == 'Y':
                    item_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        supply(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= 6 and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    supply(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    pass

    if item_found:
        print("1. Change Item Code")
        print("2. Change Item Name")
        print("3. Change Item's Supplier Code")
        print("4. Back")
        choice = input("Enter your choice: ")
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                if item.startswith(item_change):
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
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
                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

                        with open('supplier.txt','r') as supplier_f:
                            for supplier in supplier_f:
                                count += 1
                                if supplier.startswith(new_supplier_code):
                                    supplier_found = True
                                    item_info[2] = new_code
                                elif not supplier.startswith(new_supplier_code) and count >= 4:
                                    print("Sorry The Supplier You Type Haven't Register")
                                    admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

                    item_info[0] = new_code
                    print(f'After Update...\n'
                          f'Item Code:{item_info[0]}   Item Name:{item_info[1]}   Item Quantity:{item_info[3]}    '
                          f'Last Supply Date:{item_info[5]}\n')
                    print('Item Successfully Updated!')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)


def modify_supp(supplier_list):
    print("Modify Supplier Page")
    print('='*30)
    print("1. Change Supplier Code")
    print("2. Change Supplier Name")
    print("3. Change Supplier Phone Number")
    print("4. Change Supplier E-mail")
    print("5. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Change supplier code page")
        search_supp_code = input("Enter the supplier code you want to search:")
        # user_list.clear()
        with open("suppliers.txt", "w") as supp_f:
            for i in range(len(supplier_list)):
                if search_supp_code == supplier_list[i][0]:
                    print("Old supplier code: ", supplier_list[i][0])
                    new_code = input("Enter your new supplier code: ")
                    supplier_list[i][0] = new_code
                    print("Code change successful..")
                    # join ":" into the file to separate it.
                    supp_f.write(":".join(supplier_list[i]) + "\n")
                    break
                else:
                    supp_f.write(":".join(supplier_list[i]) + "\n")

        # print("Change supplier code page")
        # search_supp_code = input("Enter the supplier code you want to search: ")
        # with open("suppliers.txt","r") as supp_f:
        #     for i in range(len(supp_list)):
        #         if search_supp_code == supp_list[i][0]:
        #             print("Old supplier code is: ",supp_list[0][1])
        #             new_supp_code = int(input("Enter the new supplier code: "))
        #             supp_list[i][0] = new_supp_code
        #             supp_f.write(supp_list[i][0])

    if choice == "2":
        print("Change supplier name page")
        search_supp_code = input("Enter the supplier code you want to search: ")
        with open("suppliers.txt", "w") as supp_f:
            for i in range(len(supplier_list)):
                if search_supp_code == supplier_list[i][0]:
                    print("the name of this supplier is ", supplier_list[i][1])
                    new_name = input("Enter the name you want to change: ")
                    supplier_list[i][1] = new_name
                    print("Name change successful....")
                    supp_f.write(":".join(supplier_list[i]) + "\n")
                    break
                else:
                    supp_f.write(":".join(supplier_list[i]) + "\n")
        # print("Change supplier name page")
        # search_supp_code = input("Enter the supplier code you want to search: ")
        # with open("suppliers.txt","r") as supp_f:
        #     for i in range(len(supp_list)):
        #         if search_supp_code == supp_list[i][0]:
        #             print("the name of this supplier is ",supp_list[i][1])
        #             new_name = input("Enter the name you want to change: ")
        #             supp_list[i][1] = new_name
        #             supp_f.write(supp_list[i][1])
        #             print("New name have change successful !!")

    if choice == "3":
        supp_info(supplier_list)


def delete_supp(supplier_list):
    print("Delete Supplier Page")
    search_supp_code = input("Enter the supplier code you want to delete: ")
    with open("suppliers.txt", "w") as supp_f:
        for i in range(len(supplier_list)):
            if search_supp_code == supplier_list[i][0]:
                print("Supplier Deleted")
                break

            else:
                # 利用join function来把list 变成string
                supp_f.write(":".join(supplier_list[i]) + "\n")

def delete_hospital(hospital_list):
    print("Delete Hospital Page")
    search_hospital_code = input("Enter the hospital code you want to delete: ")
    with open("hospital.txt", "w") as supp_f:
        for i in range(len(hospital_list)):
            if search_hospital_code == hospital_list[i][0]:
                print("Supplier Deleted")
                break

            else:
                supp_f.write(":".join(hospital_list[i]) + "\n")


def delete_user(user_list):
    print("Delete User Page")
    search_user_ID = input("Enter the user id you want to search: ")
    with open("users.txt", "w") as user_f:
        for i in range(len(user_list)):
            if search_user_ID == user_list[i][0]:
                print("User Deleted")
                break
            else:
                user_f.write(":".join(user_list[i]) + "\n")
    # print("Delete user page")
    # search_userID = input("Enter the user id you want to search: ")
    # with open("users.txt","r") as user_f:
    #     for i in range(len(user_list)):
    #         if search_userID == user_list[i][0]:
    #             print("User deleted")
    #
    #         else:
    #             user_f.write(user_list)


def delete_item(inventory_list):
    print('Delete Item Page')
    item_code = input("Enter the user id you want to search: ")
    with open("ppe.txt", "w") as inventory_f:
        for i in range(len(inventory_list)):
            if item_code == inventory_list[i][0]:
                print("User Deleted")
                break
            else:
                inventory_f.write(":".join(inventory_list[i]) + "\n")


def staff_menu(user_list, supplier_list, inventory_list, hospital_list):
    print("Staff Menu")
    print("1. Inventory In")
    print("2. Inventory Out")
    print("3. Summary Inventory")
    print("4. Search Items")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        supply(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "2":
        distribute(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "3":
        display_inventory_list(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "4":
        search_item(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "5":
        exit()


def supply(user_list, supplier_list, inventory_list, hospital_list):
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    item_found = False
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[2]}    Supply Code:{items[3]}'
                    f'    Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        supply(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        supply(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= 6 and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    supply(user_list, supplier_list, inventory_list, hospital_list)
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
                    with open('transaction.txt', 'a') as trans:
                        trans.write(f'{"supply"}'
                                    f',{item_code},{item_supplier},{item_info[2]},{quantity_changes},{date_time()}\n')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)
    choice = input('Continue Add Item? Y/N').strip().upper()
    if choice == 'Y':
        supply(user_list, supplier_list, inventory_list, hospital_list)
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def distribute(user_list, supplier_list, inventory_list, hospital_list):
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    item_found = False
    with open('ppe.txt', 'r') as file_line:
        line = len(file_line.readlines())
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
            if items.startswith(item_change):
                items = items.strip().split(',')
                print(f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[2]}    '
                      f'Last Distribute Date:{items[5]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        distribute(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= 6 and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    distribute(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    pass
    if item_found:
        hospital_code = input('Please Type The Hospital Code:')
        hospital_code = hospital_code.upper().strip()
        hospital_found = False
        with open('hospital.txt', 'r') as check:
            for hospitals_line in check:
                if hospitals_line.startswith(hospital_code):
                    hospitals_line = hospitals_line.strip().split(',')
                    print(f'Hospital Code:{hospitals_line[0]}   Hospital Name:{hospitals_line[1]}   '
                          f'Last Distribute Date:{hospitals_line[3]}\n')
                    confirm = input('Is This Hospital Detail Correct? Y/N:')
                    if confirm.upper().strip() == 'Y':
                        hospital_found = True
                        continue
                    elif confirm.upper().strip() == 'N':
                        confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                        if confirm2.strip() == '1':
                            distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirm2.strip() == '2':
                            admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    if item_found and hospital_found:
        with open('ppe.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('ppe.txt', 'w') as edit_quantity:
            for item in lines:
                if item.startswith(item_change):
                    print(item)
                    item_info = item.strip().split(',')
                    item_code, item_name, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                    item_quantity = int(item_info[3])
                    check_again = input(f'The remaining quantity is "{item_quantity}" boxes,'
                                        f'\nAre you sure want to distribute ? \nYes(Y)  No(N)\n>')
                    if check_again.upper() == 'Y':
                        quantity_changes = int(input('Quantity(Boxes):'))
                        item_info[3] = str(item_quantity - quantity_changes)
                        item_info[5] = date_time()
                        print(f'After Update...\n'
                              f'Item Code:{item_code}   Item Name:{item_name}   Item Quantity:{item_info[3]}    '
                              f'Last Distribute Date:{item_info[5]}\n')
                        print('Item Successfully Updated!')
                        with open('transaction.txt', 'a') as trans:
                            trans.write(f'{"distribute"}'
                                        f',{item_code},{hospital_code},{item_info[2]},{quantity_changes},{date_time()}\n')
                    elif check_again.upper() == 'N':
                        print('Item Update Failed!')

                    edit_quantity.write(','.join(item_info) + "\n")
                else:
                    edit_quantity.write(item)
    choice = input('Continue Distribute Item? Y/N').strip().upper()
    if choice == 'Y':
        distribute(user_list, supplier_list, inventory_list, hospital_list)
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def display_inventory_list(user_list, supplier_list, inventory_list, hospital_list):
    all_record = []
    count = 0
    with open('ppe.txt', 'r') as list:
        for line in list:
            all_record.append(line.strip().split(','))
        for x in range(len(all_record) - 1):
            for y in range(x, len(all_record)):
                if int(all_record[x][3]) > int(all_record[y][3]):
                    temp = all_record[x]
                    all_record[x] = all_record[y]
                    all_record[y] = temp
    for i in range(len(all_record)):
        print(
            f'Item Code:{all_record[i][0]}           Item Name:{all_record[i][1]}           Supplier Code:{all_record[i][2]}            Quantity:{all_record[i][3]} boxes \n'
            f'Last Supply Date:{all_record[i][4]}         Last Distribute Date:{all_record[i][5]}\n')
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def less_25(user_list, supplier_list, inventory_list, hospital_list):
    with open('ppe.txt', 'r') as check:
        for line in check:
            item = line.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item
            if int(item_quantity) < 25:
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity}\n")
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def search_item(user_list, supplier_list, inventory_list, hospital_list):
    temporary = []
    item_search = input('Enter Item Code:')
    with open('ppe.txt', 'r') as file:
        for line in file:
            item = line.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item
            if item_search.upper().strip() == item_code.strip():
                print(f'The Available Quantity for {item_code} is {item_quantity} boxes\n')

    choice = input('Continue Search Item? Y/N').strip().upper()
    if choice == 'Y':
        search_item(user_list, supplier_list, inventory_list, hospital_list)
    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def track_filter_date(user_list, supplier_list, inventory_list, hospital_list):
    s_or_d_or_b = input('\nPlease Enter Filter Type:\n'
                        '"s" Supply\n'
                        '"d" Distribute\n'
                        '"b" Both\n> ')
    if s_or_d_or_b.lower().strip() not in ['s', 'd', 'b']:
        print("\nPlease Type In The Correct Format !\n")
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            main_menu()
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
            main_menu()

    with open('transaction.txt', "r") as file:
        for line in file:
            transaction_details = line.strip().split(',')
            s_or_d, item_code, supplier_code, remaining_quantity, quantity_change, date_change = transaction_details
            date_change = datetime.datetime.strptime(date_change, '%a %b %d %X %Y')
            if s_or_d_or_b == 's':
                if s_or_d.strip() == 'supply':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                              f'\nDate:{date_change}\n')
            elif s_or_d_or_b == 'd':
                if s_or_d.strip() == 'distribute':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                              f'\nDate:{date_change}\n')
            elif s_or_d_or_b == 'b':
                if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                    print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                          f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                          f'\nDate:{date_change}\n')

    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        admin_main_menu(user_list, supplier_list, inventory_list, hospital_list)


check_file()