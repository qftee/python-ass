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
        with open("ppes.txt", "a") as inven_details_f_read:
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

