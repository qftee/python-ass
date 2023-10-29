import datetime


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def staff_main_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print('Staff Menu')
        print('='*30)
        print("1.  Supplier")
        print("2.  Hospital")
        print("3.  Inventory")
        print("4.  Search Features")
        choice = input("Enter your choice: ")

        if choice == '1':
            staff_supplier_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '2':
            staff_hospital_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '3':
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)

        elif choice == '4':
            staff_search_function(user_list, supplier_list, inventory_list, hospital_list)
        else:
            print("Sorry I don't Understand, please type again")
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list):
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
        choice = input("Enter your choice: ")
        print("==" * 30)
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

        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_supplier_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Add Supplier")
        print("2.  Delete Supplier")
        print("3.  Modify Supplier Data")
        print("4.  Supplier Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)
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

        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_hospital_menu(user_list, supplier_list, inventory_list, hospital_list):
    while True:
        print("1.  Add Hospital")
        print("2.  Delete Hospital")
        print("3.  Modify Hospital Data")
        print("4.  Hospital Summary")
        print("5.  Main Menu")
        print("6.  Exit")
        choice = input("Enter your choice: ")
        print("==" * 30)
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

        else:
            print("Sorry I Don't Understand, Please Type Again")
            staff_inventory_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_function(user_list, supplier_list, inventory_list, hospital_list):
    print("Search Page")
    print("1. Search User")
    print("2. Search Items")
    print("3. Search Supplier")
    print("4. Search Hospital")
    print("5. Transaction Record")
    choice = input("Enter your choice: ")

    if choice == "1":
        staff_search_items(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "2":
        staff_search_supplier(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "3":
        staff_search_hospital(user_list, supplier_list, inventory_list, hospital_list)

    if choice == "4":
        staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list)

    print('==' * 30)


def staff_supply(user_list, supplier_list, inventory_list, hospital_list):
    print('Supply Page')
    print('==' * 30)
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
                    f'Item Code:{items[0]}   Item Name:{items[1]}   Item Quantity:{items[3]}    Supplier Code:{items[2]}'
                    f'    Last Supply Date:{items[4]}\n')
                confirm = input('Is This Item Detail Correct? Y/N:')
                if confirm.upper().strip() == 'Y':
                    item_found = True
                    continue
                elif confirm.upper().strip() == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_supply(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_supply(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_supply(user_list, supplier_list, inventory_list, hospital_list)
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

                    with open('suppliers.txt', 'w') as file:
                        for sup in lines:
                            if sup.startswith(item_supplier):
                                sup = sup.strip().split(',')
                                sup[4] = date_time()
                                file.write(','.join(sup) + '\n')
                            else:
                                file.write(sup)
                    with open('transaction.txt', 'a') as trans:
                        trans.write(f'{"supply"}'
                                    f',{item_code},{item_supplier},{item_info[3]},{quantity_changes},{date_time()}\n')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)
    choice = input('Continue Add Item? Y/N:').strip().upper()
    if choice == 'Y':
        staff_supply(user_list, supplier_list, inventory_list, hospital_list)
    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_distribute(user_list, supplier_list, inventory_list, hospital_list):
    print('Distribute Page')
    print('=='*30)
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    count = 0
    count2 = 0
    item_found = False
    with open('ppe.txt', 'r') as file_line, open('hospital.txt', 'r') as hospital_file:
        line = len(file_line.readlines())
        hospital = len(hospital_file.readlines())
    with open('ppe.txt', 'r') as check:
        for items in check:
            count += 1
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
                    if confirm2.strip() == '1':
                        staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    if item_found:
        hospital_code = input('Please Type The Hospital Code:')
        hospital_code = hospital_code.upper().strip()
        hospital_found = False
        with open('hospital.txt', 'r') as check:
            for hospitals_line in check:
                count2 += 1
                if hospitals_line.startswith(hospital_code):
                    hospitals_line = hospitals_line.strip().split(',')
                    print(f'Hospital Code:{hospitals_line[0]}   Hospital Name:{hospitals_line[1]}   '
                          f'Last Distribute Date:{hospitals_line[4]}\n')
                    confirm = input('Is This Hospital Detail Correct? Y/N:')
                    if confirm.upper().strip() == 'Y':
                        hospital_found = True
                        continue
                    elif confirm.upper().strip() == 'N':
                        confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                        if confirm2.strip() == '1':
                            staff_distribute(user_list, supplier_list, inventory_list, hospital_list)
                        elif confirm2.strip() == '2':
                            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                elif not hospital_found and count2 >= hospital:
                    print('Hospital Not Found')
                    confirm4 = input('1. Type Again\n2.Return To Main Menu\n>')
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
                    if new_quantity <= 0:
                        print(f'The available quantity is {item_quantity} boxes, not enough to distribute.')
                        confirmation = input('1.Retype\n2.Main Menu\n>')
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
                        with open('transaction.txt', 'a') as trans:
                            trans.write(f'{"distribute"}'
                                        f',{item_code},{hospital_code},{item_info[3]},{quantity_changes},{date_time()}\n')
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


def staff_inventory_summary(user_list, supplier_list, inventory_list, hospital_list):
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
    choice = input('1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_less_25(user_list, supplier_list, inventory_list, hospital_list):
    count = 0
    item_less_25 = False
    with open('ppe.txt', 'r') as check:
        line = len(check.readlines())
        check.seek(0)
        for item in check:
            count += 1
            item_info = item.strip().split(',')
            item_code, item_name, supplier_code, item_quantity, last_supply_date, last_distribute_date = item_info
            if int(item_quantity) < 25:
                item_less_25 = True
                print(f"{item_code}'s quantity is below 25 boxes,\n"
                      f"The Remaining quantity is {item_quantity} boxes\n")
    if count >= line and not item_less_25:
        print('All The Items In our Inventory Is More Than 25 Boxes')
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list):
    s_or_d_or_b = input('\nPlease Enter Filter Type:\n'
                        '"s" Supply\n'
                        '"d" Distribute\n'
                        '"b" Both\n> ')
    if s_or_d_or_b.lower().strip() not in ['s', 'd', 'b']:
        print("\nPlease Type In The Correct Format !\n")
        confirm = input('"T" Type Again\n"R" Return To Main Menu\n>')
        if confirm.upper().strip() == "T":
            staff_track_filter_date(user_list, supplier_list, inventory_list, hospital_list)
        elif confirm.upper().strip() == "R":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
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

    with open('transaction.txt', "r") as file:
        for line in file:
            transaction_details = line.strip().split(',')
            s_or_d, item_code, supplier_code, remaining_quantity, quantity_change, date_change = transaction_details
            date_change = datetime.datetime.strptime(date_change, '%a %b %d %X %Y')
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

    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_supplier_summary(user_list, supplier_list, inventory_list, hospital_list):
    with open('suppliers.txt', 'r') as read_supplier:
        for line in read_supplier:
            line = line.strip().split(',')
            print(f'Supplier Code:{line[0]}     Supplier Name:{line[1]}     Supplier Phone Number:{line[2]}     '
                  f'Supplier Email:{line[3]}      Last Supply Date:{line[4]} ')
    choice = input('1.Main Menu\n2.Exit').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)



def staff_search_hospital(user_list, supplier_list, inventory_list, hospital_list):
    print("\nSearch Hospital Page")
    print('==' * 30)
    search_hospital_code = input("Search Hospital Code: ").upper().strip()
    found = False
    for hospital in hospital_list:
        hospital_details = hospital.split(',')
        if search_hospital_code == hospital_details[0]:
            found = True
            print("Hospital Code: ", hospital_details[0])
            print("Hospital Name: ", hospital_details[1])
            print("Hospital Phone Number: ", hospital_details[2])
            print("Hospital Email: ", hospital_details[3])
            print("Last Distribute Date: ", hospital_details[4])
            break

    if not found:
        print("\nHospital Not Found")

    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_supplier(user_list, supplier_list, inventory_list, hospital_list):
    print("\nSearch Supplier Page")
    print('==' * 30)
    search_supplier_code = input("Search Supplier Code:").upper().strip()
    found = False
    for supplier in supplier_list:
        supplier_details = supplier.split(',')
        if search_supplier_code == supplier_details[0]:
            found = True
            print("Supplier Code: ", supplier_details[0])
            print("Supplier Name: ", supplier_details[1])
            print("Supplier Phone Number: ", supplier_details[2])
            print("Supplier Email: ", supplier_details[3])
            print("Last Supply Date: ", supplier_details[4])
            break

    if not found:
        print("\nSupplier Not Found")

    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_search_items(user_list, supplier_list, inventory_list, hospital_list):
    print("\nSearch Items Page")
    print('==' * 30)
    search_item_code = input("Search Item Code: ").upper().strip()
    found = False
    for item in inventory_list:
        item_details = item.split(',')
        if search_item_code == item_details[0]:
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

    choice = input('\n1.Main Menu\n2.Exit\n>').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_add_inventory(user_list, supplier_list, inventory_list, hospital_list):
    item_exist = False
    supplier_found = False
    with open('suppliers.txt', 'r') as file_line:
        supp_line = len(file_line.readlines())
    with open("ppe.txt", "r") as file:
        allrec = []
        for read in file:
            rec = read.strip().split(",")
            allrec.append(rec)
    print("Add New Inventory Page")
    print('==' * 30)
    item_code = input("Enter the item code: ").upper().strip()
    item_name = input("Enter the name of item:").upper().strip()
    item_supplier_code = input("Enter the item supplier code: ").upper().strip()
    item_last_supply_date = date_time()
    item_last_distribute_date = date_time()
    item_details = f'{item_code},{item_name},{item_supplier_code},100,{item_last_supply_date},{item_last_distribute_date}'.strip()
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
    with open("ppe.txt", "r") as read_ppe:
        lines = read_ppe.readlines()
    for convert in lines:
        item_detail = convert.replace("\n", "").split(",")
        if item_code == item_detail[0] and item_name == item_detail[1]:
            item_exist = True
    if item_exist:
        print('Item already exist')
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
    choice = input(" Add Another Item?(y/n): ")
    if choice == "n":
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
    elif choice == "y":
        staff_add_inventory(user_list, supplier_list, inventory_list, hospital_list)


def staff_add_hospital(user_list, supplier_list, inventory_list, hospital_list):
    hosp_exist = False
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
        hospital_code = input("Enter the hospital code: ").upper().strip()
        hospital_name = input("Enter the name of hospital:").upper().strip()
        hospital_email = input("Enter the Email of the hospital: ").strip()
        hospital_phone_number = input("Enter the phone number of the hospital: ").strip()
        last_distribute_date = date_time()
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
        choice = input(" Add Another Hospital?(y/n): ")
        if choice == "n":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            staff_add_hospital(user_list, supplier_list, inventory_list, hospital_list)


def staff_add_supp(user_list, supplier_list, inventory_list, hospital_list):
    supp_exist = False
    with open("suppliers.txt", "r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(",")
            allrec.append(rec)
    num = 4 - len(allrec)
    if num == 0:
        print("Supplier Full")
    while num != 0:
        print("Add New Supplier")
        print('==' * 30)
        supp_code = input("Enter The Supplier Code: ").strip().upper()
        supp_name = input("Enter The Name Of Supplier:").strip().upper()
        supp_phone_number = input("Enter The Phone Number Of The Supplier: ").strip()
        supp_mail = input("Enter The Email  Of The Supplier: ").strip()
        last_supply_date = date_time()
        supp_details = f'{supp_code},{supp_name},{supp_phone_number},{supp_mail},{last_supply_date}'
        num = num - 1
        with open("suppliers.txt", "r") as read_supp:
            lines = read_supp.readlines()
        for convert in lines:
            supp_detail = convert.replace("\n", "").split(",")
            if supp_code == supp_detail[0] and supp_name == supp_detail[1]:
                supp_exist = True
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

        choice = input("Add Another Supplier (y/n):").lower().strip()
        if choice == "n":
            staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
        elif choice == "y":
            staff_add_supp(user_list, supplier_list, inventory_list, hospital_list)


def staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list):
    print("Modify Hospital Page")
    print('=' * 30)
    hospital_code = input('Hospital Code:').upper().strip()
    count = 0
    hospital_found = False
    with open('hospital.txt', 'r') as file_line:
        line = len(file_line.readlines())
    with open('hospital.txt', 'r') as check:
        for hospitals in check:
            count += 1
            if hospitals.startswith(hospital_code):
                hospitals = hospitals.strip().split(',')
                print(
                    f'Hospital Code:{hospitals[0]}   Hospital Name:{hospitals[1]}   Hospital Phone Number:{hospitals[3]}       Hospital Email:{hospitals[2]}'
                    f'Last Distribute Date:{hospitals[4]}\n')
                confirm = input('Is This Hospital Information You Need To edit? Y/N:').upper().strip()
                if confirm == 'Y':
                    hospital_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= line and not hospital_found:
                print('Hospital Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_hospital_data(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if hospital_found:
        print("1. Change Hospital Code")
        print("2. Change Hospital Name")
        print("3. Change Hospital Email")
        print("4. Change Hospital Phone Number")
        print("5. Back")
        choice = input("Enter your choice: ")
        with open('hospital.txt', 'r') as check_lines:
            lines = check_lines.readlines()

        with open('hospital.txt', 'w') as hospital_f:
            for hospital in lines:
                if hospital.startswith(hospital_code):
                    hospital_info = hospital.strip().split(',')
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

                    print(f'After Update...\n'
                          f'Hospital Code:{hospital_info[0]}   Hospital Name:{hospital_info[1]}   Hospital Email:{hospital_info[2]}    '
                          f'Hospital Phone Number:{hospital_info[3]}      Last Supply Date:{hospital_info[4]}\n')
                    print('Item Successfully Updated!')
                    hospital_f.write(','.join(hospital_info) + "\n")

                else:
                    hospital_f.write(hospital)
    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)


def staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list):
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
                        staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= line and not item_found:
                print('Items Not Found')
                confirm3 = input('1. Type Again\n2.Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_inventory_data(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

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

                        with open('suppliers.txt','r') as supplier_f:
                            for supplier in supplier_f:
                                count += 1
                                if supplier.startswith(new_supplier_code):
                                    supplier_found = True
                                    item_info[2] = new_supplier_code
                                elif not supplier_found and count >= line:
                                    print("Sorry The Supplier You Type Haven't Register")
                                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    else:
                        print("Sorry I Dont Understand , Please Type Again.")
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
                    print(f'After Update...\n'
                          f'Item Code:{item_info[0]}   Item Name:{item_info[1]}   Item Quantity:{item_info[3]}     Supply Code:{item_info[2]}    '
                          f'Last Supply Date:{item_info[5]}\n')
                    print('Item Successfully Updated!')
                    edit_quantity.write(','.join(item_info) + "\n")

                else:
                    edit_quantity.write(item)


def staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list):
    print("Modify Supplier Page")
    print('=' * 30)
    supplier_code = input('Supplier Code:').upper().strip()
    count = 0
    supplier_found = False

    with open('suppliers.txt', 'r') as file_line:
        line = len(file_line.readlines())
    with open('suppliers.txt', 'r') as check:
        for supplier in check:
            count += 1
            if supplier.startswith(supplier_code):
                supplier = supplier.strip().split(',')
                print(
                    f'Supplier Code:{supplier[0]}   Supplier Name:{supplier[1]}   Supplier Phone Number:{supplier[2]}    Supply Email:{supplier[3]}    '
                    f'Last Supply Date:{supplier[4]}\n')
                confirm = input('Is This Supplier You Need To edit? Y/N:').upper().strip()
                if confirm == 'Y':
                    supplier_found = True
                    continue
                elif confirm == 'N':
                    confirm2 = input('1. Type Again\n2.Return To Main Menu\n>')
                    if confirm2.strip() == '1':
                        staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                    elif confirm2.strip() == '2':
                        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
            elif count >= line and not supplier_found:
                print('Supplier Not Found')
                confirm3 = input('1. Type Again\n2. Return To Main Menu\n>')
                if confirm3.strip() == '1':
                    staff_modify_supp(user_list, supplier_list, inventory_list, hospital_list)
                elif confirm3.strip() == '2':
                    staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if supplier_found:
        print("1. Change Supplier Code")
        print("2. Change Supplier Name")
        print("3. Change Supplier Email")
        print("4. Change Supplier Phone Number")
        choice = input("Enter your choice: ")
        with open('suppliers.txt', 'r') as edit_quantity:
            lines = edit_quantity.readlines()

        with open('suppliers.txt', 'w') as edit_quantity:
            for suppliers in lines:
                if suppliers.startswith(supplier_code):
                    supplier_info = suppliers.strip().split(',')
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
                    print(f'After Update...\n'
                          f'Supplier Code:{supplier_info[0]}   Supplier Name:{supplier_info[1]}   Supplier Phone Number:{supplier_info[2]}     Supplier Email:{supplier_info[3]}    '
                          f'Last Supply Date:{supplier_info[4]}\n')
                    print('Supplier Info Successfully Changed!')
                    edit_quantity.write(','.join(supplier_info) + "\n")

                else:
                    edit_quantity.write(suppliers)


def staff_delete_supp():
    print('Delete Supplier Page')
    supp_code = input("Enter Supplier Code : ").upper().strip()

    with open("suppliers.txt", "r") as file:
        lines = file.readlines()

    with open("suppliers.txt", "w") as supplier_f:
        for line in lines:
            if not line.startswith(supp_code):
                supplier_f.write(line)

    print("Supplier Deleted")


def staff_delete_hospital():
    print('Delete Hospital Page')
    hospital_code = input("Enter Hospital Code : ").upper().strip()

    with open("hospital.txt", "r") as file:
        lines = file.readlines()

    with open("hospital.txt", "w") as hospital_f:
        for line in lines:
            if not line.startswith(hospital_code):
                hospital_f.write(line)

    print("Hospital Deleted")


def staff_delete_item():
    print('Delete Item Page')
    item_code = input("Enter Item Code : ").upper().strip()

    with open("ppe.txt", "r") as file:
        lines = file.readlines()

    with open("ppe.txt", "w") as inventory_f:
        for line in lines:
            if not line.startswith(item_code):
                inventory_f.write(line)

    print("Item Deleted")


def staff_hospital_summary(user_list, supplier_list, inventory_list, hospital_list):
    with open('hospital.txt', 'r') as read_hospital:
        for line in read_hospital:
            line = line.strip().split(',')
            print(f'Hospital Code:{line[0]}     Hospital Name:{line[1]}     Hospital Phone Number:{line[2]}'
                  f'Hospital Email:{line[3]}      Last Distribute Date:{line[4]} ')
    choice = input('1.Main Menu\n2.Exit\nEnter Your Choice:').strip()
    if choice == '1':
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)

    if choice == '2':
        exit()

    else:
        staff_main_menu(user_list, supplier_list, inventory_list, hospital_list)
