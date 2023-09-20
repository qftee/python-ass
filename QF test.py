def create_suppliers():
    jqsb = f'JQSB, JQ Sdn.Bhd, MS,FS, date'
    qfsb = f'QFSB, QF Sdn Bhd, GL,HC, date'
    pysb = f'PYSB, PY Sdn Bhd, GW,SC, date'
    with open('suppliers.txt', 'w') as create_supplier:
        create_supplier.write(jqsb + '\n')
        create_supplier.write(qfsb + '\n')
        create_supplier.write(pysb + '\n')


try:
    with open('suppliers.txt','r') as supplier:
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

create_items()
def supply():
    supply_item = input('Item code:')
    quantity = int(input('Quantity(Boxes):'))
    supply_item.upper()



def update_inventory():
    supply_or_distribute = int(input('''"1" Supply
    "2" Distribute
    "3" Exit
    >'''))
    if supply_or_distribute == 1:
        supply

    elif supply_or_distribute == 2:
        distribute

    elif supply_or_distribute == 3:
        mainmenu

    else:
        print("Sorry, I don't understand")
        update_inventory
