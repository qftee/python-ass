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

def supplier_list():
    with open ("supplierss.txt","r") as file:
        allrec = []
        for line in file:
            rec = line.strip().split(":")
            allrec.append(rec)
    num = 4 - len(allrec)
    while num != 0:
        print("Add new supplier")
        print(allrec)
        supp_code = input("Enter the supplier code: ")
        supp_name = input("Enter the name of supplier:")
        supp_details = str(supp_code) + ":" + str(supp_name)
        num = num - 1
        #if supp_code != rec[0]:
        #else:
            #print("Supplier have been taken")
        choice = input("Did you finish input the details of the inventory (y/n)?")
        if choice == "y":
            break

        if choice == "n":
            with open("supplierss.txt", "a") as file:
                file.write(supp_details + "\n")
    print("supplier full")

supplier_list()


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