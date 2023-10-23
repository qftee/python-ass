import datetime
def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')
def open_file():
    user_list = []

    # Open and read the inventory file.
    try:

        with open("users.txt", "r") as user_f:
            for line in user_f:
                line = line.strip().strip(":")
                user_list.append(line)
        # create a empty file
        main_login_page(user_list)


    except FileNotFoundError:
        with open("supplierss.txt", "a") as supp_f:
            # supp_info(supp_list)
            supp_f.write("")
            pass

        with open("users.txt", "r") as user_f:
            for line in user_f:
                line = line.strip().split(":")
                user_list.append(line)

        with open("ppe.txt", "a") as inven_f:
            print("Insert the item details")
            initial_creation()
            main_login_page(user_list)


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

try:
    with open('ppe.txt', 'r') as item:
        check_items_available = item.read()
        if check_items_available == '':
            create_items()
except FileNotFoundError:
    create_items()
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
        return
    else:
        print("Logged in unsuccessful..")
        return

def admin_menu(user_list):
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
            search_function(user_list)

        if choice == "4":
            pass
            # print supp_info(supp_list)

        if choice == "5":
            delete_user(user_list)

        if choice == "6":
            pass
            # inventory_in(inven_list)

        if choice == "7":
           pass # inventory_out(inven_list)

        if choice == "8":
            pass #summary_inven(inven_list)

        if choice == "9":
            pass #search_items(inven_list)

        if choice == "10":
            exit()

def add_user(user_list):
    # with open("users.txt", "r") as user_f:
    #     for user_rec in user_f:
    #         rec = user_rec.strip().split(":")
    #         user_list.append(rec)
    print(user_list)
    while True:
        print("Add user page.")
        user_ID = input("Enter the user ID: ")
        user_name = input("Enter the user name: ")
        user_pw = input("Enter the user password: ")
        user_type = input("Choose the type of user (admin / staff): ")
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type).lower()
        # user_list.append(user_details)
        with open("users.txt","a") as user_f:
            user_f.write(user_details + "\n")
            ask = input("Did you finish add new user (y/n)?")
            print("---"*30)

            if ask == "y":
                # with open("users.txt", "a") as user_f:
                #     for user_rec in user_f:
                #         rec = user_rec.strip().split(":")
                #         user_list.append(rec) .split(":")
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

def search_function(user_list):
    print("Search page")
    print("1. Search user")
    print("2. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        search_user(user_list)

    if choice == "2":
        pass#search_items(inven_list)

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


#def search_items(inven_list):
    #print("Search items page")
    #search_item_code = input("Enter the items code you want to search: ")
    #for i in range(len(inven_list)):
        #if search_item_code == inven_list[i][0]:
            #print("Item code: ", inven_list[i][0])
            #print("Item name: ", inven_list[i][1])
           # print("Item quantity: ", inven_list[i][2])
            #print("Item supplier: ", inven_list[i][3])
           # print("Item supplier code: ", inven_list[i][4])
            #break

       # else:
           # print("This item was not found.")
           # return


#def supp_info(supp_list):
    #print("Supplier information page.")
    #print("1. Add supplier")
    #print("2. Modify supplier")
    #print("3. Delete supplier")
    #print("4. Back")
    #choice = input("Enter your choice: ")
    #with open("supplierss.txt", "r") as supp_f:
       # for line in supp_f:
          #  supp_data = line.strip().split(":")
          #  supp_list.append(supp_data)
    #if choice == "1":
       # add_supp()

   # if choice == "2":
      #  modify_supp(supp_list)

    #if choice == "3":
     #  delete_supp(supp_list)

    #if choice == "4":
      #  return

#def add_supp():
    #with open("supplierss.txt", "r") as file:
      #  allrec = []
       # for line in file:
       #    rec = line.strip().split(":")
       #     allrec.append(rec)
   # num = 4 - len(allrec)
   # while num != 0:
    #    print("Add new supplier")
     #   print(allrec)
     #   supp_code = input("Enter the supplier code: ")
     #   supp_name = input("Enter the name of supplier:")
     #  supp_phonenum = input("Enter the phone number of the supplier: ")
     #   supp_mail = input("Enter the mail box of the supplier: ")
      #  supp_details = str(supp_code) + ":" + str(supp_name) + ":" + str(supp_phonenum) + ":" + str(supp_mail)
      #  num = num - 1
      #  # if supp_code != rec[0]:
      #  # else:
        # print("Supplier have been taken")
      #  choice = input("Did you finish input the details of the inventory (y/n)?")
      #  if choice == "y":
      #      break

     #   if choice == "n":
     #       with open("supplierss.txt", "a") as file:
      #          file.write(supp_details + "\n")
  #  print("supplier full")

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


def main_menu():
    pass





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









