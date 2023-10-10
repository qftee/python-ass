def track_inventory():
    with open('ppe.txt', 'r') as open_file:
        for line in open_file:
            item_info = line.strip().split(',')
            item_code, item_name, item_quantity, last_supply_date, last_distribute_date = item_info
            if int(item_quantity) >= int(item_info[2]):
                item_quantity = item_info[2]
                ','.join(item_info) + "\n"
                with open('temporary.txt', 'a') as sort:
                    sort.write(str(item_info))


def sort_quantity():
    with open('ppe.txt', 'r') as open_file:
        line = open_file.readlines()

    for lines in range(len(line)-1):
        first_value = int(line[lines].split(',')[2])
        second_value = int(line[lines+1].split(',')[2])
        if first_value > second_value:
            line[lines + 1] = line[lines]
    print(line)
    with open('ppe.txt', 'w') as file:
        file.writelines(line)


sort_quantity()

