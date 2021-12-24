#!/usr/bin/env python
# coding: utf-8

# In[31]:


class foodorderingapp():
    global users,foodlist,total_items_ordered,bill_collection
    users = {}
    total_items_ordered = []
    bill_collection = {}
    foodlist = {11:{'item':'Pizza','price':300,'quantity':'8 Inch'},12:{'item':'Burger','price':150,'quantity':'1 Medium size'},
        13:{'item':'Coke',"price":30,'quantity':'150ml'},14:{'item':'Chicken nuggets','price':100,'quantity':'6 piece'}}
    
    def login(phone_number,password):
        if phone_number in users and password == users[phone_number]['password']:
            print("\nLogged in successfull")
            print("\nOptions:\n1)Place New Order (Select Options to view food list)\n2)Order History\n3)Update Profile") 
        else:
            print("Username and password do not match")

    def registration(username,fullname,phone_number,email,address,password):
        if username not in users:
            users[username] = {'fullname':fullname,'phone_number':phone_number,'email':email,'address':address,'password':password}
            print('\nRegistration successfull')
        else:
            print("\nEntered user name not available.Please enter different user")
            
    def options():
        print("\nFood options:")
        for i in foodlist:
            print(f"Enter {i} for {foodlist[i]['item']} ({foodlist[i]['quantity']}) [INR {foodlist[i]['price']}]")
        print("\nTo select the item and complete your order select option 'Place order'")
        
class admin(foodorderingapp):
    def additem(item,price,quantity):
        foodid = (str(1)+str(len(foodlist)+1))
        foodlist[foodid] = {'item':item,'price':price,'quantity':quantity}
        
        foodorderingapp.options()
    def edititem(foodid,value1,value2,value3):
        if foodid in foodlist:
                foodlist[foodid]['item'] = value1
                foodlist[foodid]['quantity'] = value2
                foodlist[foodid]['price'] = value3
                print(f"\nUpdated details\nItem     : {foodlist[foodid]['item']}\nQuantity : {foodlist[foodid]['quantity']}\nPrice    : {foodlist[foodid]['price']}")
        else:
            print(f"Incorrect food id - {foodid}")
    def stocks():
        if sales == 0:
            print("Current balance is zero ")
        else:
            print(f"\nTotal stock balance is {sales}")
            
    def discount(billid,discount_percentage):
        if billid in bill_collection:
            final_amount = bill_collection[billid] - (bill_collection[billid] * (discount_percentage/100))
            print(f"\nOriginal amount Rs.{bill_collection[billid]}")
            print(f"Final amount to be paid after {discount_percentage}% discount is Rs.{int(final_amount)}")
        else:
            print("Please enter valid Bill id")
            
class customer(foodorderingapp):
    
    def updateprofile(username,key,value1):
        if username in users:
            if key in users[username]:
                users[username][key] = value1
                print("\nUpdated details -")
                print(f"Full name   : {users[username]['fullname']}\nPhone number: {users[username]['phone_number']}\nEmail       : {users[username]['email']}\nAddress     : {users[username]['address']}\nPassword    : {users[username]['password']} ") 
            else:
                print('Please enter valid key')

        else:
            print("Please enter valid username")
            
    def placeorder(username,*argv):
        global currentorder,total,confirmedorder,sales
        currentorder = []
        confirmedorder = []
        validation = []
        total = 0
        index = 0
        sales = 0
        for i in foodlist:
            validation.append(i)
        if username in users:
            for arg in argv:
                if arg in validation:
                    print("\nSelected item: ")
                    selected = f"{foodlist[arg]['item']} ({foodlist[arg]['quantity']} )[INR {foodlist[arg]['price']}]"
                    print(f"{index+1}){foodlist[arg]['item']} ({foodlist[arg]['quantity']} )[INR {foodlist[arg]['price']}]")
                    total += foodlist[arg]['price']
                    index+=1
                    currentorder.append(selected)
                    print(f"\nTotal amount -Rs.{total}")
                    confirmation = input("\nDo you want to confirm the order? Y/N - ").upper()
                    if confirmation == 'Y':
                        total_items_ordered.append({username:currentorder})
                        sales += total
                        BillID = str('Zomma') + str((len(bill_collection))+1)
                        bill_collection[BillID] = total
                        print("\nOrder placed :")
                        for index,value in enumerate(currentorder):
                            print(f"{index+1}){value}")
                        print(f"\nBill number - {BillID}")
                        print(f"Amount to be paid-Rs.{total}")
                    else:
                        currentorder.clear()
                        print("Order cancelled")                    
                else:
                    print(f"\nFood id - {arg} not a valid option please enter correct food id")
        else:
            print('\nPlease enter valid User name')

    def orderhistory(username):
        global res , checklist
        res = {}
        checklist = []
        for i in total_items_ordered:
            for j in i:
                checklist.append(j)
        if username in checklist:
            for dict in total_items_ordered:
                for list in dict:
                    if list in res:
                        print(list)
                        res[list] += (dict[list])
                    else:
                        res[list] = dict[list]
            print("\nOrder history :")
            for index,value in enumerate(res[username]):
                print(f"{index+1}) {value}")
        else:
            print("\nUnable to find the user")
            
#Customer Class
# Values are (username,fullname,phone_number,email,address,password)
cust1 = customer.registration('Abhidasan','Abhi',9821654160,'Abhishithdasan@gmail.com','Bhandup','Abhi@01')
# Values are (username,password)
cust1 = customer.login('Abhidasan','Abhi@01')
#values are (username,key_name,key_value) - key options are -('fullname','phone_number','email','address','password')
#I created the edit option which allows to edit one value at a time
cust1 = customer.updateprofile('Abhidasan','address','Nahur')
# #values are (username,foodid). You can enter n number of orders
cust1 = customer.placeorder('Abhidasan',14)
# #values are (username)
cust1 = customer.orderhistory('Abhidasan')

# # #Admin Class
# # Values are (username,fullname,phone_number,email,address,password)
admin1 = admin.registration('Abhidasan1','Ashu',9768814170,'Adasan01@gmail.com','Nahur','Ashu@01')
# # Values are (username,password)
admin1 = admin.login('Abhidasan01','Ashu@01')
#values are ()
admin1 = admin.stocks()
#values are (foodid,key1,keyvalue1,) Keys are (fullname,phone_number,email,address,password)
admin1 = admin.edititem(12,'Franky','1 Roll',80)
#values = ()
admin1 = foodorderingapp.options()
#values (item name,price,quantity)
admin1 = admin.additem('Truffle',120,'1 Piece')
#values (bill number,discount number)
admin1 = admin.discount('Zomma1',20)

