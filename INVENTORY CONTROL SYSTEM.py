"""
INVENTORY CONTROL SYSTEM

Customer ( CID , Cname , Caddress , CMobile )

Product  ( PID , Pname , Price , Pdesc , StockQty , MinStock )

Order    ( OID , CID , PID , OrderQty , TotalPrice )

1- Add Customer
2- View All Customer
3- Delete A Customer
4- Add Product
5- View All Product
6- Update A Product
7- Delete A Product
8- Add Stock             
9- Place An Order
10- View All Orders
11- View Orders By CID
12- View Orders By PID    
13- Low Stock Alert
0- Exit
"""

#REQUIRED LIBRARIES
import pickle
import os

#---------------------------------------
#      AUTOINCREMENT CID
#---------------------------------------
def generateCID():
    try:
        file = open('cid.txt','r')
        cid = int(file.read())
        file.close()
    except:
        cid = 100   # starting

    cid = cid + 1

    file = open('cid.txt','w')
    file.write(str(cid))
    file.close()
    return cid

#---------------------------------------
#      ADD A CUSTOMER INFORMATION
#---------------------------------------
def addCustomer():
    file = open('customers.bin','ab')
    cid = generateCID()
    print("\n\t Generated Customer ID :", cid)
    cname = input("\t Enter Customer Name : ")
    cadd = input("\t Enter Customer Address : ")
    cmob = int(input("\t Enter Customer Mobile : "))
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    print("\n\t Customer Added Sucessfully!")
    file.close()
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#      VIEW ALL CUSTOMER'S INFORMATION
#---------------------------------------------------
def viewAllCustomer():
    file = open('customers.bin','rb')
    try:
        while True:
           print("\n\tCustomer ID :",pickle.load(file))
           print("\tCustomer Name :",pickle.load(file))
           print("\tCustomer Address :",pickle.load(file))
           print("\tCustomer Mobile :",pickle.load(file))
           print("\t----------------------------")
    except:
        print("\n\t Here is your all customer..")
    file.close()
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#         DELETE A CUSTOMER'S INFORMATION
#---------------------------------------------------
def deleteCustomer():
    file1 = open('customers.bin','rb')
    file2 = open('temp.bin','ab')
    cid = int(input("\t Enter Customer ID To Delete :"))
    flag =0
    try:
        while True:
            data = pickle.load(file1)
            if data == cid:
                print("\t Customer Name :",pickle.load(file1))
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
    except:
        if flag==1:
            print("\n\t Customer Deleted Sucessfully! ")
        else:
            print("\n\t Customer Not Found!")
    file1.close()
    file2.close()
    os.remove('customers.bin')
    os.rename('temp.bin','customers.bin')
    input("\t Press Enter To Continue...")

#---------------------------------------
#      AUTOINCREMENT PID
#---------------------------------------
def generatePID():
    try:
        file = open('pid.txt','r')
        pid = int(file.read())
        file.close()
    except:
        pid = 600

    pid = pid + 1

    file = open('pid.txt','w')
    file.write(str(pid))
    file.close()
    return pid

#---------------------------------------------------
#            ADD A PRODUCT INFORMATION
#---------------------------------------------------    
def addProduct():
    file = open('products.bin','ab')
    pid = generatePID()
    print("\n\t Generated Product ID :", pid)
    pname = input("\t Enter Product Name : ")
    pprice = int(input("\t Enter Product Price : "))
    pdesc= input("\t Write About The Product : ")
    stock = int(input("\t Enter Stock Quantity: "))
    minstock = int(input("\t Enter Minimum Stock: "))
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(pprice,file)
    pickle.dump(pdesc,file)
    pickle.dump(stock,file)
    pickle.dump(minstock,file)
    print("\n\t Product Added Succesfully!")
    file.close()
    input("\t Press Enter To Continue...")
    
#---------------------------------------------------
#           VIEW PRODUCT'S INFORMATION
#---------------------------------------------------
def viewAllProducts():
    file = open('products.bin','rb')
    try:
        while True:
           print("\n\tProduct ID :",pickle.load(file))
           print("\tProduct Name :",pickle.load(file))
           print("\tProduct Price :",pickle.load(file))
           print("\tAbout Product :",pickle.load(file))
           print("\tStock:", pickle.load(file))
           print("\tMinStock:", pickle.load(file))
           print("\t----------------------------")
    except:
        print("\n\t Here is your all products..")
    file.close()
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#          UPDATE PRODUCT PRICE
#---------------------------------------------------
def updateProduct():
    file1 = open('products.bin','rb')
    file2 = open('temp.bin','ab')
    pid = int(input("\n\t Enter Product ID To Update : "))
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\t Product Name :",name)
                print("\t Old Product Price:",pickle.load(file1))
                price = int(input("\t Enter New Price :"))
                pickle.dump(price,file2)
                desc = pickle.load(file1)
                pickle.dump(desc,file2)
                old_stock = pickle.load(file1)
                print("\t Old Stock :", old_stock)
                new_stock = input("\t Enter New Stock (press enter to keep same): ")
                if new_stock == "":
                    pickle.dump(old_stock,file2)
                else:
                    pickle.dump(int(new_stock),file2)
                    
                ministock = pickle.load(file1)
                pickle.dump(ministock,file2)    
                flag = 1
            else:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
    except:
        if flag==1:
           print("\t Product Updated Succesfully!")
        else:
            print("\t Prouct Not Found!")
    file1.close()
    file2.close()
    os.remove('products.bin')
    os.rename('temp.bin','products.bin')
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#         DELETE A PRODUCT'S INFORMATION
#---------------------------------------------------
def deleteProduct():
    file1 = open('products.bin','rb')
    file2 = open('temp.bin','ab')
    pid = int(input("\t Enter Product ID To Delete :"))
    flag =0
    try:
        while True:
            data = pickle.load(file1)
            if data == pid:
                print("\t\t Product Name :",pickle.load(file1))
                pickle.load(file1) #price
                pickle.load(file1) #desc
                pickle.load(file1) #stock
                pickle.load(file1) #ministock
                flag = 1
            else:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
    except:
        if flag==1:
            print("\n\t Product Deleted Sucessfully! ")
        else:
            print("\n\t Product Not Found!")
    file1.close()
    file2.close()
    os.remove('products.bin')
    os.rename('temp.bin','products.bin')
    input("\t Press Enter To Continue...")
    
#---------------------------------------------------
#         ADD NEW STOCK
#---------------------------------------------------
def addStock():
    file1 = open('products.bin','rb')
    file2 = open('temp.bin','wb')
    pid = int(input("\n\t Enter Product ID To Add Stock : "))
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data == pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\t Product Name :", name)
                price = pickle.load(file1)
                pickle.dump(price,file2)
                desc = pickle.load(file1)
                pickle.dump(desc,file2)
                old_stock = pickle.load(file1)
                print("\t Current Stock :", old_stock)
                add_qty = int(input("\t Enter Stock To Add : "))
                new_stock = old_stock + add_qty
                pickle.dump(new_stock,file2)
                print("\t Updated Stock :", new_stock)
                ministock = pickle.load(file1)
                pickle.dump(ministock,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
                pickle.dump(pickle.load(file1),file2)
    except EOFError:
        if flag == 1:
            print("\n\t Stock Updated Successfully!")
        else:
            print("\n\t Product Not Found!")
    file1.close()
    file2.close()
    os.remove('products.bin')
    os.rename('temp.bin','products.bin')

    input("\t Press Enter To Continue...")
    
#---------------------------------------------------
#       GET A CUSTOMER INFORMATION
#---------------------------------------------------
def getCustomer(cid):
    cus = []
    file = open('customers.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==cid:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus

#---------------------------------------------------
#      GET A PRODUCT INFORMATION
#---------------------------------------------------
def getProduct(pid):
    pro = []
    file = open('products.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==pid:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro
    
#-----------------------------------------
#         PLACE AN ORDER
#-----------------------------------------
def placeOrder():
    cid = int(input("\n\t Enter Customer ID : "))
    cus = getCustomer(cid)
    if len(cus)!=0:
        print("\t Customer Name :",cus[1])
        print("\t Customer Address :",cus[2])
        pid = int(input("\t Enter Product ID : "))
        pro = getProduct(pid)
        if len(pro)!=0:
            print("\t Product Name :",pro[1])
            print("\t Product Price :",pro[2])
            print("\t Available Stock :",pro[4])
            qty = int(input("\t Enter Quantity : "))
            if pro[4] < qty:
                print("\n\t Not Enough Stock!")
            else:
                new_stock = pro[4] - qty
                file = open('order.bin','ab')
                pickle.dump(cid,file)
                pickle.dump(cus[1],file)
                pickle.dump(cus[3],file)   
                pickle.dump(cus[2],file)
                pickle.dump(pid,file)
                pickle.dump(pro[1],file)   
                pickle.dump(pro[2],file)
                pickle.dump(qty,file)
                file.close()
                #PRODUCT FILE UPDATE
                file1 = open('products.bin','rb')
                file2 = open('temp.bin','wb')
                try:
                    while True:
                        pid_read = pickle.load(file1)
                        name = pickle.load(file1)
                        price = pickle.load(file1)
                        desc = pickle.load(file1)
                        stock = pickle.load(file1)
                        ministock = pickle.load(file1)

                        if pid_read == pid:
                            stock = new_stock   #update stock

                        pickle.dump(pid_read,file2)
                        pickle.dump(name,file2)
                        pickle.dump(price,file2)
                        pickle.dump(desc,file2)
                        pickle.dump(stock,file2)
                        pickle.dump(ministock,file2)
                except:
                      pass
                file1.close()
                file2.close()
                os.remove('products.bin')
                os.rename('temp.bin','products.bin')
                
                print("\n\t Order Placed Successfully!")
                print("\t Bill Amount :",int(qty)*int(pro[2]))
        else:
            print("\t Product Not Found!")
    else:
        print("\n\t Customer Not Found!")
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#       VIEW ALL ORDERS INFORMATION
#---------------------------------------------------    
def viewOrder():
    file = open('order.bin','rb')
    try:
        n = 1001
        while True:
            cid = pickle.load(file)
            cname = pickle.load(file)
            cmob = pickle.load(file)
            cadd = pickle.load(file)
            pid = pickle.load(file)
            pname = pickle.load(file)
            price = pickle.load(file)
            qty = pickle.load(file)
            #Check customer status
            cus = getCustomer(cid)
            if len(cus) == 0:
                cstatus = " (Deleted Customer)"
            else:
                cstatus = " (Active)"
            #CHECK PRODUCT STATUS
            pro = getProduct(pid)
            if len(pro) == 0:
                pstatus = " (Deleted Product)"
            else:
                pstatus = " (Available)"    
            print("\tOrder No. :",n)
            print("\tCustomer Name :",cname + cstatus)
            print("\tCustomer Mobile :",cmob)
            print("\tCustomer Address :",cadd)
            print("\tProduct Name :",pname + pstatus)
            print("\tProduct Price :",price)
            print("\tQuantity :", qty)
            print("\tTotal :",price * qty)
            print("\t------------------------------")
            n = n+1
    except:
        print("\n\t Here is your all orders....")
    file.close()
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#       VIEW ALL ORDERS INFORMATION BY CID
#---------------------------------------------------  
def viewOrderByCID():
    file = open('order.bin','rb')
    search_cid = int(input("\n\tEnter Customer ID : "))
    flag = 0

    try:
        while True:
            cid = pickle.load(file)
            cname = pickle.load(file)
            cmob = pickle.load(file)
            cadd = pickle.load(file)
            pid = pickle.load(file)
            pname = pickle.load(file)
            price = pickle.load(file)
            qty = pickle.load(file)
            if cid == search_cid:
                flag = 1
                pro = getProduct(pid)
                if len(pro) == 0:
                    pstatus = " (Deleted Product)"
                else:
                    pstatus = " (Available)"
                print("\tCustomer Name :",cname )
                print("\tCustomer Mobile :",cmob)
                print("\tCustomer Address :",cadd)
                print("\tProduct Name :",pname + pstatus )
                print("\tProduct Price :",price)
                print("\tQuantity :", qty)
                print("\tTotal :",price * qty)
                print("\t------------------------------")
    except:
        if flag == 0:
            print("\n\t No Orders Found!")
    file.close()
    input("\t Press Enter To Continue...")

#---------------------------------------------------
#       VIEW ALL ORDERS INFORMATION BY PID
#---------------------------------------------------
def viewOrderByPID():
     file = open('order.bin','rb')
     search_pid = int(input("\n\t Enter Product ID : "))
     flag = 0
     try:
        while True:
            cid = pickle.load(file)
            cname = pickle.load(file)
            cmob = pickle.load(file)
            cadd = pickle.load(file)
            pid = pickle.load(file)
            pname = pickle.load(file)
            price = pickle.load(file)
            qty = pickle.load(file)
            if pid == search_pid:
                flag = 1
                cus = getCustomer(cid)
                if len(cus) == 0:
                    cstatus = " (Deleted Customer)"
                else:
                    cstatus = " (Active)"
                print("\tCustomer Name :",cname + cstatus )
                print("\tCustomer Mobile :",cmob)
                print("\tCustomer Address :",cadd)
                print("\tProduct Name :",pname )
                print("\tProduct Price :",price)
                print("\tQuantity :", qty)
                print("\tTotal :",price * qty)
                print("\t------------------------------")
     except:
        if flag == 0:
            print("\n\t No Orders Found!")
     file.close()
     input("\t Press Enter To Continue...")

#---------------------------------------------------
#                  LOW STOCK ALERT
#---------------------------------------------------
def lowStockAlert():
    file = open('products.bin','rb')
    flag = 0

    try:
        while True:
            pid = pickle.load(file)
            pname = pickle.load(file)
            price = pickle.load(file)
            desc = pickle.load(file)
            stock = pickle.load(file)
            minstock = pickle.load(file)

            if stock <= minstock:
                flag = 1
                print("\n\t** LOW STOCK ALERT **")
                print("\tProduct ID :", pid)
                print("\tProduct Name :", pname)
                print("\tCurrent Stock :", stock)
                print("\tMinimum Stock :", minstock)
                print("\t--------------------------")

    except:
        if flag == 0:
            print("\n\t All products have sufficient stock ")

    file.close()
    input("\t Press Enter To Continue...")     

#DASHBOARD

while True:
    print("\n\t\t ***INVENTORY CONTROL SYSTEM***")
    print('''
                1- Add Customer
                2- View All Customer
                3- Delete A Customer
                4- Add Product
                5- View All Product
                6- Update A Product
                7- Delete A Product
                8- Add Stock             
                9- Place An Order
                10- View All Orders
                11- View Orders By CID
                12- View Orders By PID    
                13- Low Stock Alert
                0- Exit
    ''')
    ch= int(input("\t Enter Your Choice: "))
    if ch==0:
        print("\n\t\tBYE BYE ADMIN!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewAllCustomer()
    elif ch==3:
        deleteCustomer()    
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProducts()
    elif ch==6:
        updateProduct()
    elif ch==7:
        deleteProduct()
    elif ch==8:
        addStock()
    elif ch==9:
        placeOrder()
    elif ch==10:
        viewOrder()    
    elif ch==11:
        viewOrderByCID()
    elif ch==12:
        viewOrderByPID()    
    elif ch==13:
        lowStockAlert()


    
