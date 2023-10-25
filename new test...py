def open_file():
    user_list = []
    supp_list = []
    inven_list = []
    # Open and read the inventory file.
    try:
        with open("suppliers.txt", "r") as supp_f:
            for line in supp_f:
                supp_list.append(line)

        with open("ppes.txt", "r") as inven_f:
            inven_f = inven_f.readline()
            for line in inven_f:
                inven_list.append(line)
            if not inven_f:
                initial_creation()

        with open("users.txt", "r") as user_f:
            for line in user_f:
                line = line.strip().strip(":")
                user_list.append(line)
        # create a empty file
        main_login_page(user_list, supp_list, inven_list)


    except FileNotFoundError:
        with open("supplierss.txt", "a") as supp_f:
            # supp_info(supp_list)
            supp_f.write("")
            pass

        with open("users.txt", "r") as user_f:
            for line in user_f:
                line = line.strip().split(":")
                user_list.append(line)

        with open("ppes.txt", "a") as inven_f:
            print("Insert the item details")
            initial_creation()
            main_login_page(user_list, supp_list, inven_list)


def initial_creation():
    print("you're in initial creation now.")
    while True:
        supp_name = False
        supp_code = False
        item_code = input("Enter the item code: ")
        item_name = input("Enter the item name: ")
        item_supp_name = input("Enter the item supplier: ")
        item_supp_code = input("Enter the item supplier code: ")
        supp_phonenum = input("Enter the phone number of the supplier: ")
        supp_mail = input("Enter the mail box of the supplier: ")
        item_details = str(item_code) + ":" + str(item_name) + ":100:" + str(item_supp_name) + ":" + str(item_supp_code)
        supp_details = str(item_supp_code) + ":" + str(item_supp_name) + ":" + str(supp_phonenum) + ":" + str(supp_mail)
        # will be empty after rerun the loop

        with open("supplierss.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for i in lines:
            i = i.replace("\n", "").split(":")
            if item_supp_code == i[0] and item_supp_name == i[1]:
                supp_name = True
                supp_code = True

            # xxx=true
            # for check, if xxx = true, else xxx = false
        if supp_code == True and supp_name == True:
            with open("ppes.txt", "a") as inven_f:
                # inven_list.append(item_details)
                inven_f.write(item_details + "\n")
            print("Same supplier, add inventory only")


        elif supp_name == False and supp_code == False:
            if len(lines) < 4:
                with open("ppes.txt", "a") as inven_f:
                    # inven = item_details.strip().split(":")
                    inven_f.write(item_details + "\n")
                    # inven_list.append(item_details)
                with open("supplierss.txt", "a") as supp_f:
                    # supp = supp_details.strip().split(":")
                    supp_f.write(supp_details + "\n")
                    # supp_list.append(supp_details)


            elif len(lines) >= 4:
                print("Supplier full")

        choice = input("Did you finish input the details of the inventory (y/n)?")
        if choice == "y":
            break
        if choice == "n":
            continue

def main_login_page(user_list, supp_list, inven_list):
    userLogin = False
    user_ID = input("Enter your user ID: ")
    user_pw = input("Enter your password: ")

    for i in user_list:
        a=i.strip("\n").split(":")
        if user_ID == a[0] and user_pw == a[2]:
            userLogin = True
            break

    if userLogin == True:
        # user_list[i][3].lower("admin")
        if a[3] == "admin":
            print("Successfully entered admin page.")
            admin_menu(user_list, supp_list, inven_list)

        if a[3] == "staff":
            print("Successfully entered staff page.")
            staff_menu(inven_list)

    else:
        print("Logged in unsuccessful..")
        print('Please Type Again')
        main_login_page(user_list, supp_list, inven_list)

def admin_menu(user_list, supp_list, inven_list):
    while True:
        print("Admin Menu")
        print("1.  Add user")
        print("2.  Modify user")
        print("3.  Search Function")
        print("4.  Supplier information")
        print("5.  Delete user")
        print("6.  Inventory In")
        print("7.  Inventory Out")
        print("8.  Summary Inventory")
        print("9.  Search Items")
        print("10. Exit")
        choice = input("Enter your choice: ")
        print("===="*30)
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
            inventory_in(inven_list)

        if choice == "7":
            inventory_out(inven_list)

        if choice == "8":
            summary_inven(inven_list)

        if choice == "9":
            search_items(inven_list)

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
        with open("users.txt","a") as user_f:
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
        print("---"*30)

        if ask == "y":
            user_list.append(user_details)
            break
        if ask == "n":
            user_list.append(user_details)
            continue


def modify_user(user_list):
    #print modify menu
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
    userfound = False
    print("Search user page")
    print(user_list)
    search_userID = input("Enter the user ID you want to search: ")
    print(user_list)
    with open("users.txt","r") as user_read:
        # read = user_read.read()
        for i in user_list:
            if search_userID == i[0]:
                userfound = True
                if userfound == True:
                    print("User ID: ", i[0])
                    print("User name: ", i[1])
                    print("User password: ", i[2])
                    print("User Type: ", i[3])
                    print("————"*30)
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
    with open("supplierss.txt", "r") as supp_f:
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
    with open("supplierss.txt", "r") as file:
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
        print("Change suppplier code page")
        search_supp_code = input("Enter the supplier code you want to search:")
        # user_list.clear()
        with open("supplierss.txt", "w") as supp_f:
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
        with open("supplierss.txt", "w") as supp_f:
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
    with open("supplierss.txt","w") as supp_f:
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
    with open("users.txt","w") as user_f:
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
        inventory_in(inven_list)

    if choice == "2":
        inventory_out(inven_list)

    if choice == "3":
        summary_inven(inven_list)

    if choice == "4":
        search_items(inven_list)

    if choice == "5":
        exit()

def inventory_in(inven_list):
    print("Inventory In page")
    # enter the inventory code to find the items you want
    search_inven_code = input("Enter the items code for search: ")
    # let i be the line of the inventory list

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
            print("Items code didn't found.")
            return

def inventory_out(inven_list):
    print("Inventory Out Page")
    search_inven_code = input("Enter the items code for search: ")
    for i in range(len(inven_list)):
        if search_inven_code == inven_list[i][0]:
            print("The quantity of the items is",inven_list[i][2])
            quantity = int(input("Enter the quantity you out: "))
            importer = input("Enter your user ID: ")
            new_quantity = inven_list[i][2] - quantity
            inven_list[i][2] = new_quantity
            print("The item have out",quantity)
            print("New quantity: ",inven_list[i][2])
            print("The person that output the items: ", importer)
            return inventory_out(inven_list)

        else:
            print("Items code didn't found")
            return inventory_out(inven_list)

def summary_inven(inven_list):
    print("Summary Inventory")
    search_items_code = input("Enter the item code you want to search: ")
    for i in range(len(inven_list)):
        if search_items_code == inven_list[i][0]:
            print("Items code is: ", inven_list[i][0])
            print("Items name is: ", inven_list[i][1])
            print("Items quantity is: ",inven_list[i][2])
            print("Items supplier name is: ",inven_list[i][3])
            print("Items supplier code is: ",inven_list[i][4])


        else:
            print("Items code not found")
            return

open_file()
