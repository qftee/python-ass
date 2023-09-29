def open_file():
    try:
        #  open and read the users file
        with open("users.txt","r") as user_f:
            user_data = user_f.read()
            # if don't have user data, add user
            if not user_data:
                add_user()
    except:
        print("Users file not found, auto create a file")
        # open the users file
        with open("users.txt","a") as user_f:
            #add user
            add_user()

    try:
        # open and read the inventory file
        with open("ppe.txt","r") as inven_details_f:
            ppe_data = inven_details_f.read()
            #if don't have inventory data
            if not ppe_data:
                initial_creation()
    except:
        print("Inventory file not found, auto create a file")
        # open a inventory file
        with open("ppe.txt","a") as inven_details_f:
            initial_creation()

    try:

        with open("suppliers.txt","r") as supp_f:
            supp_data = supp_f.read()
            if not supp_data:
                supp()
    except:
        print("Suppliers file not found, auto create a file")
        supp_list = []
        with open("suppliers.txt","a") as supp_f:
            supp()
def initial_creation():
    print("you're in initial creation now.")
    while True:
        item_name = input("Enter the item name: ")
        item_code = input("Enter the item code: ")
        item_quantity = 100
        item_supp_name = input("Enter the item supplier: ")
        item_supp_code = input("Enter the item supplier code: ")
        details = str(item_name) + ":" + str(item_code) + ":" + str(item_quantity) + ":" + str(item_supp_name) + ":" + str(item_supp_code) + "\n"
        with open("ppes.txt","a") as inven_details_f_read:
            inven_details_f_read.write(details)
            choice = input("Did you finish input the details of the inventory (y/n)?")
            if choice == "y":
                main_menu()
                break
            if choice == "n":
                continue


def main_menu():
    while True:
        print("Menu")
        choice = input("1. Admin Login \n2. Staff Login \n")
        if choice == "1":
            print("Admin Logged in")
            admin_login()

        if choice == "2":
            print("Staff Logged in")
            staff_login()

def admin_login():
    admin_ID = input("Enter your admin ID: ")
    admin_name = input("Enter your admin name: ")
    admin_pw = input("Enter your password: ")
    admin_type = "admin"
    for i in range(len(user_list[])):
        if i == user_list[i][0]
def admin_menu():
    print("Admin Menu")
    print("1. Add user")
    print("2. Modify user")
    print("3. Search Function")
    print("4. delete user")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()

    if choice == "2":
        modify_user()

    if choice == "3":
        search_function()

    if choice == "4":
        delete_user()

    if choice == "5":
        exit()


def add_user():
    print("Add user page.")


def modify_user():
    print("Modify Page")
    print("1. Change user name")
    print("2. Change user password")
    print("3. Change user Type")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Change user name page")
        search_userID = input("Enter the user id you want to search")
        with open("users.txt", "w") as user_f:
            for i in range(len(user_list)):


def search_function():
    print("Search page")
    print("1. Search user")
    print("2. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Search user page")
        search_userID = input("Enter the user ID you want to search: ")


def delete_user():
    print("Delete user page")
    search_userID = input("Enter the user id you want to search: ")


def staff_menu




def supp():
    print("hi")


# user list
user_list = []

#inventory list
inven_list = []

# supplier list
supp_list = []



open_file()


