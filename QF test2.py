def supply():
    supply_item = str(input('Item code:'))
    quantity_supply = int(input('Quantity(Boxes):'))
    supply_item = supply_item.upper().strip()
    with open('ppe.txt', 'r') as edit_quantity:
        lines = edit_quantity.readlines()

    with open('ppe.txt', 'w') as edit_quantity:
        for item in lines:
            if item.startswith(supply_item):
                parts = item.split(',')
                quantity = int(parts[2])
                parts[2] = str(quantity + quantity_supply)
                edit_quantity.write(','.join(parts))
            else:
                edit_quantity.write(item)


supply()
