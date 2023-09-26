with open('ppe.txt', 'r') as edit_quantity:
    lines = edit_quantity.readlines()
    count = 0
    for item in lines:
        count += 1
        if item.startswith('HC'):
            print(item)
            item_info = item.strip().split(',')
            print(item_info)