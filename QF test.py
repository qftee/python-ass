import datetime


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
    hc = f'HC,Head Cover,QFSB,100,{date_time()},{date_time()}'
    fs = f'FS,Face Shield,JQSB,100,{date_time()},{date_time()}'
    ms = f'MS,Mask,JQSB,100,{date_time()},{date_time()}'
    gl = f'GL,Gloves,QFSB,100,{date_time()},{date_time()}'
    gw = f'GW,Gown,PYSB,100,{date_time()},{date_time()}'
    sc = f'SC,Shoe Cover,PYSB,100,{date_time()},{date_time()}'
    with open('ppe.txt', 'w') as create_item:
        create_item.write(hc + '\n')
        create_item.write(fs + '\n')
        create_item.write(ms + '\n')
        create_item.write(gl + '\n')
        create_item.write(gw + '\n')
        create_item.write(sc + '\n')


def update_inventory():
    how_to_manage = int(input('"1" Supply \n"2" Distribute \n"3" Main Menu \n>'))
    if how_to_manage == 1:
        supply()
    elif how_to_manage == 2:
        distribute()
    elif how_to_manage == 3:
        main_menu()

        print("Sorry, I don't understand")
        update_inventory()



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



def display_inventory_quantity():
    all_record = []
    count = 0
    with open('ppe.txt', 'r') as list:
        for line in list:
            all_record.append(line.strip().split(','))
        for x in range(len(all_record)-1):
            for y in range(x, len(all_record)):
                if int(all_record[x][3]) > int(all_record[y][3]):
                    temp = all_record[x]
                    all_record[x] = all_record[y]
                    all_record[y] = temp
    for i in range(len(all_record)):
        print(f'Item Code:{all_record[i][0]}           Item Name:{all_record[i][1]}           Supplier Code:{all_record[i][2]}            Quantity:{all_record[i][3]} boxes \n'
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


create_items()
update_inventory()





