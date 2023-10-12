# def initial_creation():
#     supp_list = []
#     inven_list = []
#     while True:
#         item_code = input("Enter the item code: ")
#         item_name = input("Enter the item name: ")
#         item_quantity = 100
#         item_supp_code = input("Enter the supplier code: ")
#         item_supp_name = input("Enter the supplier name: ")
#         details = str(item_code) + ":" + str(item_name) + ":" + str(item_quantity) + ":" + str(item_supp_code) + ":" + str(item_supp_name)
#         supp_det = str(item_supp_code) + ":" + str(item_supp_name)
#         with open("supplierss.txt","r") as supp_ff:
#             supp_list = supp_ff.readlines()
#             for x in range(len(supp_list)):
#                 supp_list[x] = supp_list[x].replace("\n","")
#
#         with open("supplierss.txt", "a") as supp_f:
#             # if len(supp_list) <= 3:
#                 supp_f.write(supp_det + "\n")
#                 supp_list.append(supp_det)
#
#             if len(supp_list) > 4:
#                 if supp_det not in supp_list:
#                     print("Supplier enough !")
#                     continue
#
#                 else:
#                     supp_f.write(supp_det + "\n")
#                     supp_list.append(supp_det)
#
#         with open("ppes.txt","a") as inven_f:
#             inven_f.write(details + "\n")
#             inven_list.append(details)
#
#         ask = input("Did you finish input item details (y/n)?")
#         if ask == "y":
#             break
#         if ask == "n":
#             continue
#
#
#
#
#
# initial_creation()

def search_function(user_list, inven_list):
    print("Search page")
    print("1. Search user")
    print("2. Search items")
    choice = input("Enter your choice: ")
    if choice == "1":
        search_user(user_list)

    if choice == "2":
        search_items(inven_list)

user_list=[]
with open("users.txt", "r") as user_f:
     for user_rec in user_f:
         rec = user_rec.strip().split(":")
         user_list.append(rec)

def search_user(user_list):
    userfound = False
    print("Search user page")
    print(user_list)
    search_userID = input("Enter the user ID you want to search: ")
    print (user_list)
    for i in range(len(user_list)):
        if search_userID == user_list[i][0]:
            userfound = True
            if userfound == True:
                print("User ID: ", user_list[i][0])
                print("User name: ", user_list[i][1])
                print("User password: ", user_list[i][2])
                print("User Type: ", user_list[i][3])
                break

            else:
                print("The user was not found. Please try again.")
                break


def add_user():
    user_list = []
    with open("users.txt", "r") as user_f:
        for user_rec in user_f:
            rec = user_rec.strip().split(":")
            user_list.append(rec)
    while True:
        print("Add user page.")
        user_ID = input("Enter the user ID: ")
        user_name = input("Enter the user name: ")
        user_pw = input("Enter the user password: ")
        user_type = input("Choose the type of user (admin / staff): ")
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type).lower()
        # user_list.append(user_details)
        with open("users.txt","a") as user_f:
            user_f.write(user_details + "\n")
            ask = input("Did you finish add new user (y/n)?")
            if ask == "y":
                # with open("users.txt", "a") as user_f:
                #     for user_rec in user_f:
                #         rec = user_rec.strip().split(":")
                #         user_list.append(rec)
                user_list.append(user_details.split(":"))
                search_function(user_list, inven_list)
                break

            if ask == "n":
                user_list.append(user_details.split(":"))
                continue
#
#
inven_list = []

try:
    #  open and read the users file
    with open("users.txt","r") as user_f:
        user_data = user_f.read()
        # if don't have user data, add user
        if not user_data:
            add_user()


except FileNotFoundError:
    print("Users file not found, auto create a file")
    # open the users file
    with open("users.txt","a") as user_f:
        #add user
        add_user()


