import datetime


def main_menu():
    pass


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


def create_suppliers():
    jqsb = f'JQSB, JQ Sdn.Bhd, MS,FS, date'
    qfsb = f'QFSB, QF Sdn Bhd, GL,HC, date'
    pysb = f'PYSB, PY Sdn Bhd, GW,SC, date'
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
    sphs = f'SPHS, Sungai Pal Hospital, MS,FS, date'
    mwhs = f'MWHS, Mou Wish Hospital, GL,HC, date'
    cshs = f'CSHS, Cyber Science Hospital, GW,SC, date'
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
    hc = f'HC,QFSB,100,date,date'
    fs = f'FS,JQSB,100,date,date'
    ms = f'MS,JQSB,100,date,date'
    gl = f'GL,QFSB,100,date,date'
    gw = f'GW,PYSB,100,date,date'
    sc = f'SC,PYSB,100,date,date'
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

    else:
        print("Sorry, I don't understand")
        update_inventory()


def supply_or_distribute(s_or_d):
    supply_item = str(input('Item code:'))
    quantity_changes = int(input('Quantity(Boxes):'))
    supply_item = supply_item.upper().strip()
    with open('ppe.txt', 'r') as edit_quantity:
        lines = edit_quantity.readlines()

    with open('ppe.txt', 'w') as edit_quantity:
        for item in lines:
            if item.startswith(supply_item):
                item_info = item.split(',')
                item_code = item_info[0]
                item_name = item_info[1]
                item_quantity = int(item_info[2])
                last_supply_date = item_info[3]
                last_distribute_date = item_info[4]
                if s_or_d == 'supply':
                    check_again = input(f'The remaining quantity is "{item_quantity}" boxes,\n'
                                        f'Are you sure want to add it ? \nYes(Y)  No(N)\n>')
                    if check_again.upper() == 'Y':
                        item_info[2] = str(item_quantity + quantity_changes)
                        item_info[3] = date_time()
                        print('Item successfully updated')
                    elif check_again.upper() == 'N':
                        print('Item Update Failed')

                    else:
                        print("Sorry I Don't Understand , Please type 'Y' or 'N'")
                elif s_or_d == 'distribute':
                    check_again = input(f'The remaining quantity is "{item_quantity}" boxes,\n'
                                        f'Are you sure want to distribute ? \nYes(Y)  No(N)\n>')
                    if check_again.upper() == 'Y':
                        item_info[2] = str(item_quantity - quantity_changes)
                        item_info[4] = date_time()
                        print('Item successfully updated')
                    else:
                        print('Item Update Failed')
                edit_quantity.write(','.join(item_info))
            else:
                edit_quantity.write(item)

create_items()
update_inventory()

