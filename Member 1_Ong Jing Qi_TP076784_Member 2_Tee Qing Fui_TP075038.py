import datetime
def open_file():
    try:
        #  open and read the users file
        with open("users.txt", "r") as user_f:
            user_data = user_f.read()
            # if don't have user data, add user
            if not user_data:
                add_user(user_list)
    except:
        print("Users file not found, auto create a file")
        # open the users file
        with open("users.txt", "a") as user_f:
            # add user
            add_user(user_list)

    try:
        # open and read the inventory file
        with open("ppe.txt", "r") as inven_details_f:
            ppe_data = inven_details_f.read()
            # if don't have inventory data
            if not ppe_data:
                initial_creation()
    except:
        print("Inventory file not found, auto create a file")
        # open a inventory file
        with open("ppe.txt", "a") as inven_details_f:
            initial_creation()

    try:

        with open("suppliers.txt", "r") as supp_f:
            supp_data = supp_f.read()
            if not supp_data:
                supp_info()
    except:
        print("Suppliers file not found, auto create a file")
        # supp_list = []
        with open("suppliers.txt", "a") as supp_f:
            supp_info()


def initial_creation():
    print("you're in initial creation now.")
    while True:
        item_name = input("Enter the item name: ")
        item_code = input("Enter the item code: ")
        item_quantity = 100
        item_supp_name = input("Enter the item supplier: ")
        item_supp_code = input("Enter the item supplier code: ")
        details = str(item_name) + ":" + str(item_code) + ":" + str(item_quantity) + ":" + str(
            item_supp_name) + ":" + str(item_supp_code) + "\n"
        with open("ppe.txt", "a") as inven_details_f_read:
            inven_details_f_read.write(details)
            choice = input("Did you finish input the details of the inventory (y/n)?")
            if choice == "y":
                main_login_page(user_list)
                break
            if choice == "n":
                continue


# def main_menu():
#     while True:
#         print("Menu")
#         choice = input("1. Admin Login \n2. Staff Login \n")
#         if choice == "1":
#             print("Admin Logged in")
#             admin_login()
#
#         if choice == "2":
#             print("Staff Logged in")
#             staff_login()

def main_login_page(user_list):
    user_ID = input("Enter your admin ID: ")

    user_pw = input("Enter your password: ")
    for i in range(len(user_list)):
        if user_ID == len(user_list[i][0]) and user_pw == len(user_list[i][2]):
            return user_list[i]
        else:
            print("Logged in unsuccessful..")
            return


def admin_menu():
    print("Admin Menu")
    print("1. Add user")
    print("2. Modify user")
    print("3. Search Function")
    print("4. Supplier information")
    print("5. Delete user")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user(user_list)

    if choice == "2":
        modify_user()

    if choice == "3":
        search_function(user_list)

    if choice == "4":
        supp_info()

    if choice == "5":
        delete_user()

    if choice == "6":
        exit()


def add_user(user_list):
    while True:
        print("Add user page.")
        user_ID = input("Enter the user ID: ")
        user_name = input("Enter the user name: ")
        user_pw = input("Enter the user password: ")
        user_type = input("Choose the type of user (admin / staff): ")
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type) + "\n"
        with open("users.txt", "a") as user_f:
            user_f.write(user_details)
            ask = input("Did you finish add new user (y/n)?")
            if ask == "y":
                admin_menu()
                break

            if ask == "n":
                continue


def modify_user():
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
            for i in range(len(user_list)):
                if search_userID == user_list[i][0]:
                    print("Old user name: ", user_list[i][1])
                    new_name = input("Enter your new user name: ")
                    user_list[i][1] = new_name
                    print("Name change successful..")
                    # join ":" into the file to separate it.
                    user_f.write(":".join(user_list[i]) + "\n")
                else:
                    user_f.write(":".join(user_list[i]) + "\n")

    if choice == "2":
        print("Change user password.")
        search_userID = input("Enter the userID you want to search: ")
        with open("users.txt", "w") as user_f:
            for i in range(len(user_list)):
                if search_userID == user_list[i][0]:
                    old_pw = input("Enter your old password: ")
                    if old_pw == user_list[i][2]:
                        new_pw = input("Enter your new password: ")
                        user_list[i][2] = new_pw
                        print("Password change successful....")
                        user_f.write(":".join(user_list[i]) + "\n")
                    else:
                        user_f.write(":".join(user_list[i]) + "\n")
                else:
                    user_f.write(":".join(user_list[i]) + "\n")

    if choice == "3":
        print("Change user Type.")
        search_userID = input("Enter the userID you want to search: ")
        with open("users.txt", "w") as user_f:
            for i in range(len(user_list)):
                if search_userID == user_list[i][0]:
                    print("The user type for this user ID is: ", user_list[i][3])
                    if user_list[i][3] == "staff":
                        new_type = "admin"
                        user_list[i][3] = new_type
                        print("User type change successfully to admin....")

                    elif user_list[i][3] == "admin":
                        new_type = "staff"
                        user_list[i][3] = new_type
                        print("User type change successfully to staff....")
                    else:
                        print("User type didn't change.")
                else:
                    print("The userID does not match and the user type cannot be changed.")


def search_function(user_list):
    print("Search page")
    print("1. Search user")
    print("2. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Search user page")
        search_userID = input("Enter the user ID you want to search: ")
        for i in range(len(user_list)):
            if search_userID == user_list[i][0]:
                print("User ID: ", user_list[i][0])
                print("User name: ", user_list[i][1])
                print("User password: ", user_list[i][2])
                print("User Type: ", user_list[i][3])
                break

            else:
                print("The user was not found. Please try again.")
                return

    if choice == "2":
        search_items()


def search_items():
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


def supp_info():
    print("Supplier information page.")
    print("1. Add supplier")
    print("2. Modify supplier")
    print("3. Delete supplier")
    print("4. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        supp_list = []
        add_supp(supp_list)

    if choice == "2":
        modify_supp()

    if choice == "3":
        delete_supp()

    if choice == "4":
        admin_menu()


def add_supp(supp_list):
    print("Add new supplier")
    while True:
        supp_code = input("Enter the supplier code: ")
        supp_name = input("Enter the name of supplier:")


def modify_supp():
    print("Modify supllier page")


def delete_supp():
    print("Delete the supplier")


def delete_user():
    print("Delete user page")
    search_userID = input("Enter the user id you want to search: ")


def staff_menu():
    print("Staff Menu")
    print("1. Inventory In")
    print("2. Inventory Out")
    print("3. Summary Inventory")
    print("4. Search Items")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        inventory_in()

    if choice == "2":
        inventory_out()

    if choice == "3":
        summary_inven()

    if choice == "4":
        search_items()

    if choice == "5":
        exit()


def inventory_in():
    print("Inventory In page")
    search_inven_code = input("Enter the items code for search: ")
    for i in range(len(inven_list)):
        if search_inven_code == inven_list[i][0]:
            print("Old Quantity: ", inven_list[i][2])
            quantity = int(input("Enter the quantity you received: "))
            importer = input("Enter your user ID: ")
            new_quantity = inven_list[i][2] + quantity
            inven_list[i][2] = new_quantity
            print("New Quantity: ", inven_list[i][2])
            print("The person that import the items: ", importer)
            return
        else:
            print("items code didn't found.")
            return


def inventory_out():
    print("hi")


def summary_inven():
    print("hi")


# user list
user_list = []

# inventory list
inven_list = []

# # supplier list
# supp_list = []


open_file()
with open("users.txt", "r") as user_f:
    for user_rec in user_f:
        rec = user_rec.strip().split(":")
        user_list.append(rec)

result = main_login_page(user_list)

while len(result) > 0:
    if len(result) > 0:
        if result[3] == "Admin":
            print("Successfully entered the admin page.")
            print("Main menu")
            print("1. Admin Menu \n 2. Staff Menu")
            ans = input("Enter your choice: ")
            if ans == "1":
                admin_menu()
            if ans == "2":
                staff_menu()

        if result[3] == "Staff":
            print("Successfully entered staff page.")
            staff_menu()


def main_menu():
    pass


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def create_suppliers():
    jqsb = f'JQSB, JQ Sdn.Bhd, MS,FS, {date_time()}'
    qfsb = f'QFSB, QF Sdn Bhd, GL,HC, {date_time()}'
    pysb = f'PYSB, PY Sdn Bhd, GW,SC, {date_time()}'
    with open('suppliers.txt', 'w') as create_supplier:
        create_supplier.write(jqsb + '\n')
        create_supplier.write(qfsb + '\n')
        create_supplier.write(pysb + '\n')


try:
    with open('suppliers.txt', 'r') as supplier:
        check_suppliers_available = supplier.read()
        if check_suppliers_available == '':
            create_suppliers()
except FileNotFoundError:
    create_suppliers()


def create_hospitals():
    sphs = f'SPHS, Sungai Pal Hospital, MS,FS, {date_time()}'
    mwhs = f'MWHS, Mou Wish Hospital, GL,HC, {date_time()}'
    cshs = f'CSHS, Cyber Science Hospital, GW,SC, {date_time()}'
    with open('hospital.txt', 'w') as create_hospital:
        create_hospital.write(sphs + '\n')
        create_hospital.write(mwhs + '\n')
        create_hospital.write(cshs + '\n')


try:
    with open('hospital.txt', 'r') as hospital:
        check_hospital_available = hospital.read()
        if check_hospital_available == '':
            create_hospitals()
except FileNotFoundError:
    create_hospitals()


def create_items():
    hc = f'HC,QFSB,100,{date_time()},{date_time()}'
    fs = f'FS,JQSB,100,{date_time()},{date_time()}'
    ms = f'MS,JQSB,100,{date_time()},{date_time()}'
    gl = f'GL,QFSB,100,{date_time()},{date_time()}'
    gw = f'GW,PYSB,100,{date_time()},{date_time()}'
    sc = f'SC,PYSB,100,{date_time()},{date_time()}'
    with open('ppe.txt', 'w') as create_item:
        create_item.write(hc + '\n')
        create_item.write(fs + '\n')
        create_item.write(ms + '\n')
        create_item.write(gl + '\n')
        create_item.write(gw + '\n')
        create_item.write(sc + '\n')


def update_inventory():
    try:
        how_to_manage = int(input('"1" Supply \n"2" Distribute \n"3" Main Menu \n>'))
        if how_to_manage == 1:
            supply_or_distribute('supply')

        elif how_to_manage == 2:
            supply_or_distribute('distribute')

        elif how_to_manage == 3:
            main_menu()

            print("Sorry, I don't understand")
            update_inventory()
    except Exception as e:
        print("An error occurred:", e)


def supply_or_distribute(s_or_d):
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    item_found = False
    with open('ppe.txt', 'r') as edit_quantity:
        lines = edit_quantity.readlines()
        code_quantity = len(lines)

    with open('ppe.txt', 'w') as edit_quantity:
        for item in lines:
            count += 1
            if item.startswith(item_change):
                item_found = True
                print(item)
                item_info = item.strip().split(',')
                item_code, item_supplier, item_quantity, last_supply_date, last_distribute_date = item_info
                item_quantity = int(item_info[2])
                check_again = input(f'The remaining quantity is "{item_quantity}" boxes,\n'
                                    f'Are you sure want to {"add" if s_or_d == "supply" else "distribute"} '
                                    f'it ? \nYes(Y)  No(N)\n>')
                quantity_changes = int(input('Quantity(Boxes):'))
                if check_again.upper() == 'Y':
                    item_info[2] = str(item_quantity + quantity_changes) if s_or_d == 'supply' else str(
                        item_quantity - quantity_changes)
                    item_info[3 if s_or_d == 'supply' else 4] = date_time()
                    print('Item Successfully Updated!')
                    with open('transaction.txt', 'a') as trans:
                        trans.write(f'{"supply" if s_or_d == "supply" else "distribute"}'
                                    f',{item_code},{item_supplier},{item_info[2]},{quantity_changes},{date_time()}\n')
                elif check_again.upper() == 'N':
                    print('Item Update Failed!')

                edit_quantity.write(','.join(item_info) + "\n")

            else:
                edit_quantity.write(item)
                if count == code_quantity and item_found:
                    break
                if count == code_quantity and not item.startswith(item_change):
                    print('Item Not Found!')


def display_inventory_quantity():
    all_record = []
    with open('ppe.txt', 'r') as list:
        for line in list:
            all_record.append(line.strip().split(','))
    for x in range(len(all_record)-1):
        for y in range(x, len(all_record)):
            if all_record[x][0] > all_record[y][0]:
                temp = all_record[x]
                all_record[x] = all_record[y]
                all_record[y] = temp
    for i in range(len(all_record)):
        print(f'{all_record[i][0]}: Available Quantity:{all_record[i][2]} boxes ')


def less_25():
    with open('ppe.txt', 'r') as check:
        for line in check:
            item = line.strip().split(',')
            item_code, item_name, item_quantity, last_supply_date, last_distribute_date = item
            if int(item_quantity) < 25:
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity}\n")


def search_quantity():
    temporary = []
    item_search = input('Enter Item Code:')
    with open('ppe.txt', 'r') as file:
        for line in file:
            item = line.strip().split(',')
            item_code, item_name, item_quantity, last_supply_date, last_distribute_date = item
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
                    if start_date <= date_change <= end_date+datetime.timedelta(days=1):
                        print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                              f'\nDate:{date_change}\n')
            elif s_or_d_or_b == 'd':
                if s_or_d.strip() == 'distribute':
                    if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                        print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                              f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                              f'\nDate:{date_change}\n')
            elif s_or_d_or_b =='b':
                if start_date <= date_change <= end_date + datetime.timedelta(days=1):
                    print(f'\nType:{s_or_d}\nItem Code:{item_code}\nSupplierCode:{supplier_code}'
                          f'\nRemaining Quantity:{remaining_quantity}\nQuantity Change:{quantity_change}'
                          f'\nDate:{date_change}\n')



track_filter_date()









