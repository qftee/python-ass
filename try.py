import datetime


def main_menu():
    pass


def date_time():
    now = datetime.datetime.now()
    return now.strftime('%c')


print("You're In Initial Creation Now")
while True:
    supp_exist = False
    item_exist = False
    item_code = input("Enter the item code: ").strip().upper()
    item_name = input("Enter the item name: ").strip().upper()
    item_last_supply_date = date_time()
    item_last_distribute_date = date_time()
    item_supp_name = input("Enter the item supplier name: ").strip().upper()
    item_supp_code = input("Enter the item supplier code: ").strip().upper()
    supp_contact_number = input("Enter the phone number of the supplier: ").strip()
    supp_email = input("Enter the e-mail of the supplier: ").strip()
    item_details = f'{item_code},{item_name},{item_supp_code},100,{item_last_supply_date},{item_last_distribute_date}'
    supp_info = f'{item_supp_code},{item_supp_name},{supp_contact_number},{supp_email},{item_last_supply_date}'
    # will be empty after rerun the loop

    with open("suppliers.txt", "r") as read_supp:
        lines = read_supp.readlines()
    for convert in lines:
        supp_detail = convert.replace("\n", "").split(":")
        if item_supp_code == supp_detail[0] and item_supp_name == supp_detail[1]:
            supp_exist = True

    with open('ppe.txt', 'r') as read_inventory:
        lines = read_inventory.readlines()
    for convert in lines:
        item_detail = convert.replace("\n", "").split(":")
        if item_code == item_detail[0] and item_name == item_detail[1]:
            item_exist = True
