# # def initial_creation():
# #     supp_list = []
# #     inven_list = []
# #     while True:
# #         item_code = input("Enter the item code: ")
# #         item_name = input("Enter the item name: ")
# #         item_quantity = 100
# #         item_supp_code = input("Enter the supplier code: ")
# #         item_supp_name = input("Enter the supplier name: ")
# #         details = str(item_code) + ":" + str(item_name) + ":" + str(item_quantity) + ":" + str(item_supp_code) + ":" + str(item_supp_name)
# #         supp_det = str(item_supp_code) + ":" + str(item_supp_name)
# #         with open("supplierss.txt","r") as supp_ff:
# #             supp_list = supp_ff.readlines()
# #             for x in range(len(supp_list)):
# #                 supp_list[x] = supp_list[x].replace("\n","")
# #
# #         with open("supplierss.txt", "a") as supp_f:
# #             # if len(supp_list) <= 3:
# #                 supp_f.write(supp_det + "\n")
# #                 supp_list.append(supp_det)
# #
# #             if len(supp_list) > 4:
# #                 if supp_det not in supp_list:
# #                     print("Supplier enough !")
# #                     continue
# #
# #                 else:
# #                     supp_f.write(supp_det + "\n")
# #                     supp_list.append(supp_det)
# #
# #         with open("ppes.txt","a") as inven_f:
# #             inven_f.write(details + "\n")
# #             inven_list.append(details)
# #
# #         ask = input("Did you finish input item details (y/n)?")
# #         if ask == "y":
# #             break
# #         if ask == "n":
# #             continue
# #
# #
# #
# #
# #
# # initial_creation()
#
# def search_function(user_list, inven_list):
#     print("Search page")
#     print("1. Search user")
#     print("2. Search items")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         search_user(user_list)
#
#     if choice == "2":
#         search_items(inven_list)
#
# user_list=[]
# with open("users.txt", "r") as user_f:
#      for user_rec in user_f:
#          rec = user_rec.strip().split(":")
#          user_list.append(rec)
#
# def search_user(user_list):
#     userfound = False
#     print("Search user page")
#     print(user_list)
#     search_userID = input("Enter the user ID you want to search: ")
#     print (user_list)
#     for i in range(len(user_list)):
#         if search_userID == user_list[i][0]:
#             userfound = True
#             if userfound == True:
#                 print("User ID: ", user_list[i][0])
#                 print("User name: ", user_list[i][1])
#                 print("User password: ", user_list[i][2])
#                 print("User Type: ", user_list[i][3])
#                 break
#
#             else:
#                 print("The user was not found. Please try again.")
#                 break
#
#
# def add_user():
#     user_list = []
#     with open("users.txt", "r") as user_f:
#         for user_rec in user_f:
#             rec = user_rec.strip().split(":")
#             user_list.append(rec)
#     while True:
#         print("Add user page.")
#         user_ID = input("Enter the user ID: ")
#         user_name = input("Enter the user name: ")
#         user_pw = input("Enter the user password: ")
#         user_type = input("Choose the type of user (admin / staff): ")
#         user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type).lower()
#         # user_list.append(user_details)
#         with open("users.txt","a") as user_f:
#             user_f.write(user_details + "\n")
#             ask = input("Did you finish add new user (y/n)?")
#             if ask == "y":
#                 # with open("users.txt", "aic") as user_f:
#                 #     for user_rec in user_f:
#                 #         rec = user_rec.strip().split(":")
#                 #         user_list.append(rec)
#                 user_list.append(user_details.split(":"))
#                 main_login_
#                 return
#
#             if ask == "n":
#                 user_list.append(user_details.split(":"))
#                 continue
# #
# #
# inven_list = []
#
# try:
#     #  open and read the users file
#     with open("users.txt","r") as user_f:
#         user_data = user_f.read()
#         # if don't have user data, add user
#         if not user_data:
#             add_user()
#
#
# except FileNotFoundError:
#     print("Users file not found, auto create a file")
#     # open the users file
#     with open("users.txt","a") as user_f:
#         #add user
#         add_user()
# with open("ppes.txt","r") as supp_f:
#     read_line = supp_f.readlines()
#     print(read_line)
#     for line in read_line:
#         lines = line.strip("\n")
#         for suppread in supp_f:
#             if line == suppread:
#                 pass
# supp_code_dupp = False  #supplier code dupplicate check
# supp_name_dupp = False  #supplier name dupplicate check
# print("you're in initial creation now.")
# while True:
#     item_code = input("Enter the item code: ")
#     item_name = input("Enter the item name: ")
#     item_quantity = 100
#     item_supp_name = input("Enter the item supplier: ")
#     item_supp_code = input("Enter the item supplier code: ")
#     item_details = str(item_code) + ":" + str(item_name) + ":" + str(item_quantity) + ":" + str(item_supp_code)
#     check_supp_list = [] #Initiate to empty everytime rerun the loop
#     with open("supplierss.txt","a") as supp_f, open("supplierss.txt","r") as supp_read,open("ppes.txt", "a") as inven_details_f:
#         supp_list = supp_read.readlines()
#         #Checking and avoid dupplicated supplier
#         for i in supp_list:
#             a = i.strip().split(':')
#             check_supp_list.append(a)
#         for i in check_supp_list:
#             if str(item_supp_code) ==i[0] :
#                 supp_code_dupp = True
#                 break   #when detected supplier code is dupplicated, break the loop
#             else:
#                 supp_code_dupp = False
#
#         for i in check_supp_list:
#             if str(item_supp_name)== i[1]:
#                 supp_name_dupp = True
#                 break   #when detected supplier name is dupplicated, break the loop
#             else:
#                 supp_name_dupp = False
#
#         if supp_code_dupp is False and supp_name_dupp is False:
#             if len(supp_list) < 4:
#                 inven_details_f.write(item_details + "\n")
#                 supp_details = str(item_supp_code) + ":" + str(item_supp_name)
#
#                 supp_f.write(supp_details + "\n")
#                 supp_list.append(supp_details)
#                 print(supp_list)
#                 choice = input("Did you finish input the details of the inventory (y/n)?")
#                 if choice == "y":
#                     break   #break the while loop to finish the initial creation
#                 if choice == "n":
#                     continue
#             elif len(supp_list) >= 4:
#                 print('Supplier amount is full. Nothing been added.')
#         elif supp_code_dupp is True and supp_name_dupp is True:
#             print('Same supplier,add inventory only')
#             inven_details_f.write(item_details + "\n")
#             choice = input("Did you finish input the details of the inventory (y/n)?")
#             if choice == "y":
#                 break   #break the while loop to finish the initial creation
#             if choice == "n":
#                 continue
#         else:
#             print('Supplier name / supplier code is being used. Nothing been added.Please redo.')
# supp_list = []
# inven_list = []
#
# print("you're in initial creation now.")
# while True:
#     supp_name = False
#     supp_code = False
#     item_code = input("Enter the item code: ")
#     item_name = input("Enter the item name: ")
#     item_supp_name = input("Enter the item supplier: ")
#     item_supp_code = input("Enter the item supplier code: ")
#     item_details = str(item_code) + ":" + str(item_name) + ":100:" + str(item_supp_name) + ":" + str(item_supp_code)
#     supp_details = str(item_supp_code) + ":" + str(item_supp_name)
#      # will be empty after rerun the loop
#
#     with open("supplierss.txt","r") as read_supp:
#         lines = read_supp.readlines()
#     for i in lines:
#         i = i.replace("\n","").split(":")
#         if item_supp_code == i[0] and item_supp_name == i[1]:
#             supp_name = True
#             supp_code = True
#         # else:
#         #     supp_name = False
#         #     supp_code = False
#
#         #xxx=true
#         #for check, if xxx = true, else xxx = false
#     if supp_code == True and supp_name == True:
#         with open("ppes.txt","a") as inven_f:
#             inven_list.append(item_details)
#             inven_f.write(item_details + "\n")
#         print("Same supplier, add inventory only")
#
#
#     elif supp_name == False and supp_code == False:
#         if len(lines) < 4:
#             with open("ppes.txt", "a") as inven_f:
#                 # inven = item_details.strip().split(":")
#                 inven_f.write(item_details + "\n")
#                 inven_list.append(item_details)
#             with open("supplierss.txt", "a") as supp_f:
#                 # supp = supp_details.strip().split(":")
#                 supp_f.write(supp_details + "\n")
#                 supp_list.append(supp_details)
#
#
#         elif len(lines) >= 4:
#             print("Supplier full")
#
#     choice = input("Did you finish input the details of the inventory (y/n)?")
#     if choice == "y":
#         break
#     if choice == "n":
#     continue

# def supplier_list():
#     with open ("supplierss.txt","r") as file:
#         allrec = []
#         for line in file:
#             rec = line.strip().split(":")
#             allrec.append(rec)
#     num = 4 - len(allrec)
#     while num != 0:
#         print("Add new supplier")
#         print(allrec)
#         supp_code = input("Enter the supplier code: ")
#         supp_name = input("Enter the name of supplier:")
#         supp_details = str(supp_code) + ":" + str(supp_name)
#         num = num - 1
#         #if supp_code != rec[0]:
#         #else:
#             #print("Supplier have been taken")
#         choice = input("Did you finish input the details of the inventory (y/n)?")
#         if choice == "y":
#             break
#
#         if choice == "n":
#             with open("supplierss.txt", "a") as file:
#                 file.write(supp_details + "\n")
#     print("supplier full")
#
# supplier_list()
    #if xxx == true, do y,else do z
    # for i in supp_list:
    #     if item_supp_code == i[0]:
    #         supp_code = True
    #         break
    #     else:
    #         supp_code = False
    # for i in supp_list:
    #     if item_supp_name == i[1]:
    #         supp_name = True
    #     else:
    #         supp_name = False
def admin_menu(user_list, supp_list, inven_list):
    while True:
        print("Admin Menu")
        print("1.  Add user")
        print("2.  Modify user")
        print("3.  Search Function")
        print("4.  Supplier information")
        print("5.  Delete user")
        print("6.  Inventory In")
        print("7.  Inventory Out")
        print("8.  Summary Inventory")
        print("9.  Search Items")
        print("10. Exit")
        choice = input("Enter your choice: ")
        print("===="*30)
        temp_list = []
        with open("users.txt","r") as user_f:
            lines = user_f.readlines()
            for line in lines:
                line = line.strip().split(":")
                temp_list.append(line)
        user_list = temp_list
        print(user_list)
        if choice == "1":
            add_user(user_list)

        if choice == "2":
            modify_user(user_list)

        if choice == "3":
            search_function(user_list, inven_list)

        if choice == "4":
            supp_info(supp_list)

        if choice == "5":
            delete_user(user_list)

        if choice == "6":
            inventory_in(inven_list)

        if choice == "7":
            inventory_out(inven_list)

        if choice == "8":
            summary_inven(inven_list)

        if choice == "9":
            search_items(inven_list)

        if choice == "10":
            exit()
def modify_user(user_list):
    #print modify menu
    print("Modify Page")
    print("1. Change user name")
    print("2. Change user password")
    print("3. Change user Type")
    # user need to do a option
    choice = input("Enter your choice: ")


    # temp_list = []
    #012:ok:123:staff
# 013:kl:456:admin
# 017:lk:789:staff
# 1234:lklo:4545:staff
    # if the option is 1, will do a change name
    # if choice == "1":
    #     print("Change user name page")
    #     search_userID = input("Enter the user id you want to search:")
    #     with open("users.txt","w") as user_f:
    #         for i in user_list:
    #         # print(i)
    #             print(i)
    #             if search_userID == i[0]:
    #                 print("Old user name: ",i[1])
    #                 new_name = input("Enter your new user name: ")
    #                 # i[1] = new_name
    #                 i[1] = new_name
    #                 print("Name change successful..")
    #                 # join ":" into the file to separate it.
    #                 # user_f.write(":".join(user_list[i]) + "\n")
    #
    #                 user_f.write(":".join(i) + "\n")
    #
    #                 print(user_list)
    #             # for i in range(len(user_list)):
    #             else:
    #                 user_f.write(":".join(i) + "\n")
    #     return
    #
    # if choice == "2":
    #     print("Change user password.")
    #     search_userID = input("Enter the userID you want to search: ")
    #
    #     with open("users.txt", "w") as user_f:
    #         for i in user_list:
    #             if search_userID == i[0]:
    #                 old_pw = input("Enter your old password: ")
    #                 if old_pw == i[2]:
    #                     new_pw = input("Enter your new password: ")
    #                     i[2] = new_pw
    #                     # user_list = temp_list
    #                     print("Password change successful....")
    #                     user_f.write(":".join(i) + "\n")
    #                 else:
    #                     user_f.write(":".join(i) + "\n")
    #             else:
    #                 user_f.write(":".join(i) + "\n")
    #
    #
    # if choice == "3":
    #     print("Change user Type.")
    #     search_userID = input("Enter the userID you want to search: ")
    #     with open("users.txt","w") as user_f:
    #         for i in user_list:
    #             if search_userID == i[0]:
    #                 print("The user type for this user ID is: ",i[3])
    #                 if i[3] == "staff":
    #                     new_type = "admin"
    #                     i[3] = new_type
    #                     user_f.write(":".join(i) + "\n")
    #                     print("User type change successfully to admin....")
    #
    #                 elif i[3] == "admin":
    #                     new_type = "staff"
    #                     i[3] = new_type
    #                     user_f.write(":".join(i) + "\n")
    #                     print("User type change successfully to staff....")
    #             else:
    #                 print("The userID does not match and the user type cannot be changed.")
    #                 user_f.write(":".join(i) + "\n")
# def change_user(user_list):
#     print("Change user name page")
#     search_userID = input("Enter the user id you want to search:")
#     temp_list = []
#     with open("users.txt","w") as user_f:
#         for i in user_list:
#             i = i.strip().split(":")
#             temp_list.append(i)
#             print(temp_list)
#         # print(i)
#             if search_userID == i[0]:
#                 print("Old user name: ",i[1])
#                 new_name = input("Enter your new user name: ")
#                 # i[1] = new_name
#                 i[1] = new_name
#                 print("Name change successful..")
#                 # join ":" into the file to separate it.
#                 # user_f.write(":".join(user_list[i]) + "\n")
#
#                 user_f.write(":".join(i) + "\n")
#                 user_list = temp_list
#                 print(user_list)
#             # for i in range(len(user_list)):
#             else:
#                 user_f.write(":".join(i) + "\n")
#     change_pw()
# def change_pw():
#     print("Change user password.")
#     search_userID = input("Enter the userID you want to search: ")
#     with open("users.txt", "w+") as user_f:
#         for i in user_list:
#             # print(i)
#             i = i.strip().split(":")
#             if search_userID == i[0]:
#                 old_pw = input("Enter your old password: ")
#                 if old_pw == i[2]:
#                     new_pw = input("Enter your new password: ")
#                     i[2] = new_pw
#                     print("Password change successful....")
#                     user_f.write(":".join(i) + "\n")
#                 else:
#                     user_f.write(":".join(i) + "\n")
#             else:
#                 user_f.write(":".join(i) + "\n")
def add_user(user_list):
    while True:
        same_ID = False
        print("Add user page.")
        user_ID = input("Enter the user ID: ")
        user_name = input("Enter the user name: ")
        user_pw = input("Enter the user password: ")
        user_type = input("Choose the type of user (admin / staff): ")
        user_details = str(user_ID) + ":" + str(user_name) + ":" + str(user_pw) + ":" + str(user_type).lower()
        # user_list.append(user_details)
        with open("users.txt","r") as user_read:
            for lines in user_read:
                line = lines.strip().split(":")
                user_list.append(line)
        with open("users.txt","a") as user_f:
            print(user_list)
            for i in user_list:
                if user_ID == i[0]:
                    same_ID = True
                    print("User ID have been used, please change another.")
                    break
            print(same_ID)
            if same_ID == False:
                user_f.write(user_details + "\n")

        ask = input("Did you finish add new user (y/n)?")
        print("---"*30)

        if ask == "y":
            user_list.append(user_details)
            break
        if ask == "n":
            user_list.append(user_details)
            continue

user_list = []
with open("users.txt", "r") as user_f:
    for line in user_f:
        line = line.strip().split(":")
        user_list.append(line)
add_user(user_list)