# # def f1(x):
# #     print("inside fi() is a : "+str(x))
# #     f2(20)
# #     return x * x
# #     print("hello")
# #
# # def f3():
# #     a = b
# #     return
# #
# # def f2(p1):
# #     print("received a value: " +str(p1))
# #     a = p1 + 2
# #     return a
# #
# # def mainMenu():
# #     while True:
# #         print("1. add")
# #         print("2. modify")
# #         print("3. delete")
# #         print("4. search")
# #         print("5. exit")
# #         choice = input("Please enter your choice: ")
# #
# #         if (choice == "1"):
# #             Add()
# #         elif (choice == "2"):
# #             Modify()
# #         elif (choice == "3"):
# #             Delete()
# #         elif (choice == "4"):
# #             Search()
# #         elif (choice == "5"):
# #             print("End of program")
# #             break
# #
# #
# # def Add():
# #     print("inside Add Function")
# #     mainMenu()
# # def Modify():
# #     print("inside Modify Function")
# #     mainMenu()
# # def Delete():
# #     print("inside Delete Function")
# #     mainMenu()
# # def Search():
# #     print("inside Search Fucntion")
# #     mainMenu()
#
# #main login
# # a = 10
# # a = f1(a)
# # print("Value of a in main logic",a)
# # print("end of program.")
# # mainMenu()
#
# def AdminMenu():
#     print("Main Menu")
#     print("1. Add a user")
#     print("2. Modify User")
#     print("3. Delete User")
#     userChoice = input("Enter your Choice: ")
#     if (userChoice == "1"):
#         Add()
#     elif (userChoice == "2"):
#         print("Call Modify Function")
#     elif (userChoice == "3"):
#         print("Call Delete Function")
#     elif (userChoice == "4"):
#         print("Exiting from program")
#         exit()
#
# def StaffMenu():
#     print("Staff Menu")
#     print("1. Distribution items")
#     print("2. Receive items")
#     print("3. Exit")
#     userChoice = input("Enter your Choice: ")
#     if (userChoice == "1"):
#         DistItems()
#     elif (userChoice == "2"):
#         RecvItems()
#     elif (userChoice == "3"):
#         exit()
#
#
# def DistItems():
#     print("Inside Distribution Function..")
#
# def RecvItems():
#     print("Inside Receiving Function..")
#
# #Main Logic
# while True:
#     loginrecord = Login()
#     if len(loginrecord) != 0:
#         print("Login Successful....")
#         if (loginrecord[3] == "1"):
#             AdminMenu()
#         else:
#             StaffMenu()
#
#     else:
#         print("Login Unsuccessful....")
#     ans = input("Do you want to login again (y/n): ")
#     if (ans.lower() == "n"):
#         print("Existing from the system")
#         break
# def getdata():
#     try:
#         age = int(input("Please enter your age: "))
#         print("Age: ",age)
#     except:
#         print("invalid input...")
#
# getdata()
# supp_list = []
# search_supp_code = input("Enter the supplier code you want to search: ")
#         with open("suppliers1.txt","r") as supp_f:
#             for i in range(len(supp_list)):
#                 if search_supp_code == supp_list[i][0]:
#                     print("Old supplier code is: ",supp_list[0][1])
#                     new_supp_code = int(input("Enter the new supplier code: "))
#                     supp_list[i][0] = new_supp_code
#                     supp_f.write(supp_list[i][0])
# inven_list = []
# user_list = []
# try:
#     # open and read the inventory file
#     with open("ppes.txt", "r") as inven_details_f:
#         ppe_data = inven_details_f.read(inven_list)
#         # if don't have inventory data
#         if not ppe_data:
#             print("Insert the item details")
#             initial_creation(inven_list, user_list)
# except:
#     print("Inventory file not found, auto create a file")
#     # open a inventory file
#     with open("ppes.txt", "a") as inven_details_f:
#         initial_creation(inven_list, user_list)
#
# def initial_creation(inven_list, user_list):
#     print("you're in initial creation now.")
#     while True:
#         item_code = input("Enter the item code: ")
#         item_name = input("Enter the item name: ")
#         item_quantity = 100
#         item_supp_name = input("Enter the item supplier: ")
#         item_supp_code = input("Enter the item supplier code: ")
#         details = str(item_code) + ":" + str(item_name) + ":" + str(item_quantity) + ":" + str(item_supp_name) + ":" + str(item_supp_code) + "\n"
#         with open("ppes.txt","a") as inven_details_f_read:
#             inven_details_f_read.write(details)
#             details = inven_list
#             choice = input("Did you finish input the details of the inventory (y/n)?")
#             if choice == "y":
#                 main_login_page(user_list)
#                 break
#             if choice == "n":
#                 continue
# with open("testing123.txt","a") as read:
#     print("hi")
user_list = []
with open("users.txt", "r") as user_f:
    for line in user_f:
        line = line.strip().strip(":")
        user_list.append(line)
with open("users.txt", "w") as user_f:
    for i in user_list:
        print("i is ",i)
        print("i[0] is",i[0])
