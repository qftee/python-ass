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
    how_to_manage = int(input('''"1" Supply
"2" Distribute
"3" Main Menu
>'''))
    if how_to_manage == 1:
        supply_or_distribute('supply')

    elif how_to_manage == 2:
        supply_or_distribute('distribute')

    elif how_to_manage == 3:
        main_menu()

        print("Sorry, I don't understand")
        update_inventory()


def supply_or_distribute(s_or_d):
    item_change = input('Item code:')
    item_change = item_change.upper().strip()
    with open('ppe.txt', 'r') as edit_quantity:
        lines = edit_quantity.readlines()

    with open('ppe.txt', 'w') as edit_quantity:
        for item in lines:
            if item.startswith(item_change):
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
                    print('Item Successfully Updated')
                elif check_again.upper() == 'N':
                    print('Item Update Failed')

                edit_quantity.write(','.join(item_info) + "\n")
            else:
                edit_quantity.write(item)
                print('Item Not Found!')


create_items()
update_inventory()

