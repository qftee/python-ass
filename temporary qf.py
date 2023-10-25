import datetime


def main_menu():
    pass


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def open_file():
    user_list = []
    supp_list = []
    inven_list = []
    # Open and read the inventory file.
    try:
        supplier = True
        inventory = True
        with open("suppliers.txt", "r") as supp_file:
            if not supp_file.read():  # Check if the file is empty
                supplier = False
            else:
                supp_file.seek(0)  # Reset the file pointer to the beginning
                for line in supp_file:
                    supp_list.append(line.strip())

        with open("ppe.txt", "r") as ppe_file:
            if not ppe_file.read():
                inventory = False
            else:
                ppe_file.seek(0)
                for line in ppe_file:
                    inven_list.append((line.strip()))

        with open("users.txt", "r") as user_file:
            user_data = user_file.read
            if user_data == '':
                add_user(user_list)
            for line in user_file:
                line = line.strip().strip(":")
                user_list.append(line)
        # create a empty file
        if not supplier or not inventory:
            initial_creation()
        main_login_page(user_list, supp_list, inven_list)

    except FileNotFoundError:
        with open("suppliers.txt", "a") as supp_data:
            # supp_info(supp_list)
            supp_data.write("")

        with open("users.txt", "r") as user_data:
            for line in user_data:
                line = line.strip().split(":")
                user_list.append(line)

        with open("ppe.txt", "a") as ppe_data:
            print("Insert the item details")
            initial_creation()
            main_login_page(user_list, supp_list, inven_list)


def initial_creation():
    print("You're In Initial Creation Now")
    while True:
        supp_exist = False
        item_code = input("Enter the item code: ").strip().upper()
        item_name = input("Enter the item name: ").strip().upper()
        item_last_supply_date = date_time()
        item_last_distribute_date = date_time()
        item_supp_name = input("Enter the item supplier: ").strip().upper()
        item_supp_code = input("Enter the item supplier code: ").strip().upper()
        supp_contact_number = input("Enter the phone number of the supplier: ").strip()
        supp_email = input("Enter the mail box of the supplier: ").strip()
        item_details = f'{item_code}:{item_name}:{item_supp_code}:100:{item_last_supply_date}:{item_last_distribute_date}'
        supp_details = f'{item_supp_code}:{item_supp_name}:{supp_contact_number}:{supp_email}:{item_last_supply_date}'
        # will be empty after rerun the loop

        with open("suppliers.txt", "r") as read_supp:
            suppliers_quantity = read_supp.readlines()
        for i in suppliers_quantity:
            i = i.replace("\n", "").split(":")
            if item_supp_code == i[0] and item_supp_name == i[1]:
                supp_exist = True

            # xxx=true
            # for check, if xxx = true, else xxx = false
        if supp_exist:
            with open("ppe.txt", "a") as ppe_data:
                # inven_list.append(item_details)
                ppe_data.write(item_details + "\n")
            print("Same supplier, add inventory only")
        elif not supp_exist:
            if len(suppliers_quantity) < 4:
                with open("ppe.txt", "a") as ppe_data:
                    # inven = item_details.strip().split(":")
                    ppe_data.write(item_details + "\n")
                    # inven_list.append(item_details)
                with open("suppliers.txt", "a") as supp_f:
                    # supp = supp_details.strip().split(":")
                    supp_f.write(supp_details + "\n")
                    # supp_list.append(supp_details)
            elif len(suppliers_quantity) >= 4:
                print("Supplier full")

        choice = input("Did you finish input the details of the inventory (y/n)?")
        if choice == "y":
            break
            open_file()
        if choice == "n":
            continue


def main_login_page(user_list, supp_list, inven_list):
    user_login = False
    user_id = input("Enter your user ID: ")
    user_pw = input("Enter your password: ")

    for i in user_list:
        user_info = i.strip("\n").split(":")
        if user_id == user_info[0] and user_pw == user_info[2]:
            user_login = True
            break

    if user_login:
        # user_list[i][3].lower("admin")
        if user_info[3] == "admin":
            print("Successfully entered admin page.")
            admin_menu(user_list, supp_list, inven_list)

        if user_info[3] == "staff":
            print("Successfully entered staff page.")
            staff_menu(inven_list)
        return
    else:
        print("Logged in unsuccessful..")
        return


def admin_menu(user_list, supp_list, inven_list):
    while True:
        print("Admin Menu")
        print("1.  Add user")
        print("2.  Modify User")
        print("3.  Search Function")
        print("4.  Supplier Information")
        print("5.  Delete user")
        print("6.  Inventory In")
        print("7.  Inventory Out")
        print("8.  Summary Inventory")
        print("9.  Search Items")
        print("10. Exit")
        choice = input("Enter your choice: ")
        print("====" * 30)
        temp_list = []
        with open("users.txt", "r") as user_f:
            lines = user_f.readlines()
            for line in lines:
                line = line.strip().split(":")
                temp_list.append(line)
        user_list = temp_list
        print(user_list)
        if choice == "1":
            add_user(user_list)

        if choice == "2":
            modify_user(user_list)

        if choice == "3":
            search_function(user_list, inven_list)

        if choice == "4":
            supp_info(supp_list)

        if choice == "5":
            delete_user(user_list)

        if choice == "6":
            supply()

        if choice == "7":
            distribute()

        if choice == "8":
            display_inventory_list()

        if choice == "9":
            search_quantity()

        if choice == "10":
            exit()


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
    print("1. Change user name")
    print("2. Change user password")
    print("3. Change user Type")
    # user need to do a option
    choice = input("Enter your choice: ")
    # if the option is 1, will do a change name
    if choice == "1":
        print("Change user name page")
        search_userID = input("Enter the user id you want to search:")
        with open("users.txt", "w") as user_f:
            for i in user_list:
                # print(i)
                print(i)
                if search_userID == i[0]:
                    print("Old user name: ", i[1])
                    new_name = input("Enter your new user name: ")
                    # i[1] = new_name
                    i[1] = new_name
                    print("Name change successful..")
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


def search_function(user_list, inven_list):
    print("Search page")
    print("1. Search user")
    print("2. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        search_user(user_list)

    if choice == "2":
        search_items(inven_list)


def search_user(user_list):
    user_found = False
    print("Search user page")
    print(user_list)
    search_userID = input("Enter the user ID you want to search: ")
    print(user_list)
    with open("users.txt", "r") as user_read:
        # read = user_read.read()
        for i in user_list:
            if search_userID == i[0]:
                user_found = True
                if user_found:
                    print("User ID: ", i[0])
                    print("User name: ", i[1])
                    print("User password: ", i[2])
                    print("User Type: ", i[3])
                    print("————" * 30)
                    break
                else:
                    print("The user was not found. Please try again.")
                break


def search_items(inven_list):
    print("Search items page")
    search_item_code = input("Enter the items code you want to search: ")
    for i in range(len(inven_list)):
        if search_item_code == inven_list[i][0]:
            print("Item code: ", inven_list[i][0])
            print("Item name: ", inven_list[i][1])
            print("Item quantity: ", inven_list[i][2])
            print("Item supplier: ", inven_list[i][3])
            print("Item supplier code: ", inven_list[i][4])
            break

        else:
            print("This item was not found.")
            return


def supp_info(supp_list):
    print("Supplier information page.")
    print("1. Add supplier")
    print("2. Modify supplier")
    print("3. Delete supplier")
    print("4. Back")
    choice = input("Enter your choice: ")
    with open("suppliers.txt", "r") as supp_f:
        for line in supp_f:
            supp_data = line.strip().split(":")
            supp_list.append(supp_data)
    if choice == "1":
        add_supp()

    if choice == "2":
        modify_supp(supp_list)

    if choice == "3":
        delete_supp(supp_list)

    if choice == "4":
        return


def add_supp():
    with open("suppliers.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(":")
            allrec.append(rec)
    num = 4 - len(allrec)
    while num != 0:
        print("Add new supplier")
        print(allrec)
        supp_code = input("Enter the supplier code: ")
        supp_name = input("Enter the name of supplier:")
        supp_phonenum = input("Enter the phone number of the supplier: ")
        supp_mail = input("Enter the mail box of the supplier: ")
        supp_details = str(supp_code) + ":" + str(supp_name) + ":" + str(supp_phonenum) + ":" + str(supp_mail)
        num = num - 1
        # if supp_code != rec[0]:
        # else:
        # print("Supplier have been taken")
        choice = input("Did you finish input the details of the inventory (y/n)?")
        if choice == "y":
            break

        if choice == "n":
            with open("supplierss.txt", "a") as file:
                file.write(supp_details + "\n")
    print("supplier full")


def modify_supp(supp_list):
    print("Modify supplier page")
    print("1. Change supplier code")
    print("2. Change supplier name")
    print("3. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Change supplier code page")
        search_supp_code = input("Enter the supplier code you want to search:")
        # user_list.clear()
        with open("suppliers.txt", "w") as supp_f:
            for i in range(len(supp_list)):
                if search_supp_code == supp_list[i][0]:
                    print("Old supplier code: ", supp_list[i][0])
                    new_code = input("Enter your new supplier code: ")
                    supp_list[i][0] = new_code
                    print("Code change successful..")
                    # join ":" into the file to separate it.
                    supp_f.write(":".join(supp_list[i]) + "\n")
                    break
                else:
                    supp_f.write(":".join(supp_list[i]) + "\n")

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
            for i in range(len(supp_list)):
                if search_supp_code == supp_list[i][0]:
                    print("the name of this supplier is ", supp_list[i][1])
                    new_name = input("Enter the name you want to change: ")
                    supp_list[i][1] = new_name
                    print("Name change successful....")
                    supp_f.write(":".join(supp_list[i]) + "\n")
                    break
                else:
                    supp_f.write(":".join(supp_list[i]) + "\n")
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
        supp_info(supp_list)


def delete_supp(supp_list):
    print("Delete the supplier")
    search_supp_code = input("Enter the code you want to search: ")
    with open("suppliers.txt", "w") as supp_f:
        for i in range(len(supp_list)):
            if search_supp_code == supp_list[i][0]:
                print("Supplier deleted")
                break

            else:
                # 利用join function来把list 变成string
                supp_f.write(":".join(supp_list[i]) + "\n")


def delete_user(user_list):
    print("Delete user page")
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


def staff_menu(inven_list):
    print("Staff Menu")
    print("1. Inventory In")
    print("2. Inventory Out")
    print("3. Summary Inventory")
    print("4. Search Items")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        supply()

    if choice == "2":
        distribute()

    if choice == "3":
        display_inventory_list()

    if choice == "4":
        search_quantity()

    if choice == "5":
        exit()


def supply():
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
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[2]}    Supply Code:{items[3]}    '
                    f'Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        supply()
                    elif confirm2.strip() == '2':
                        pass
            elif count >= 6 and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    supply()
                elif confirm3.strip() == '2':
                    pass

    if item_found:
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
                                        f'\nAre you sure want to supply? \nYes(Y)  No(N)\n>')
                    if check_again.upper() == 'Y':
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
                    elif check_again.upper() == 'N':
                        print('Item Update Failed!')

                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)


def distribute():
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
                        distribute()
                    elif confirm2.strip() == '2':
                        main_menu()
            elif count >= 6 and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    distribute()
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
                            distribute()
                        elif confirm2.strip() == '2':
                            main_menu()
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


def display_inventory_list():
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


def less_25():
    with open('ppe.txt', 'r') as check:
        for line in check:
            item = line.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item
            if int(item_quantity) < 25:
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity}\n")


def search_quantity():
    temporary = []
    item_search = input('Enter Item Code:')
    with open('ppe.txt', 'r') as file:
        for line in file:
            item = line.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item
            if item_search.upper().strip() == item_code.strip():
                print(f'The Available Quantity for {item_code} is {item_quantity} boxes\n')


def track_filter_date():
    s_or_d_or_b = input('\nPlease Enter Filter Type:\n'
                        '"s" Supply\n'
                        '"d" Distribute\n'
                        '"b" Both\n> ')
    if s_or_d_or_b.lower().strip() not in ['s', 'd', 'b']:
        print("\nPlease Type In The Correct Format !\n")
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            track_filter_date()
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
            track_filter_date()
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


open_file()