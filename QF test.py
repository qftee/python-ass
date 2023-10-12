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
                item_code, item_name, item_quantity, last_supply_date, last_distribute_date = item_info
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



