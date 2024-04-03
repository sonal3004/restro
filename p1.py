class restro:
    menu_items={"burger":50,"pizza":300}
    book_table=10
    customer_orders=0
    def display(self):
        print(a1.menu_items)
    def menu(self,item,price):
        a1.menu_items[item]=price
    def table(self):
        a1.book_table=a1.book_table-1
        if a1.book_table==0:
            print("sorry no tables left")
        else:
            print("**************************************************************")
            print("table booked!!\nyour table number is:",10-a1.book_table,"\n")
            print("tables left::",a1.book_table)
            print("***************************************************************")
    def order(self,ord):
        count=0
        for i in ord:
                a=a1.menu_items[i]
                count=count+a
        total_price=count
        a1.customer_orders=a1.customer_orders+1
        print("order confirmed")
        def receipt(total_price,o):
            print("**************************************************")
            print("**order is:",o,"                              **")
            for i in o:
                print(i,"is for",a1.menu_items[i])
            print("**total amount:",total_price,"                            **")
            print("**************************************************we accept only cash on delivery!!")
        receipt(total_price,ord)
a1=restro()
print("WELCOME TO RESTRO!!")
while True:
    print("1.add an item to menu\n2.book a table\n3.order something\n4.display menu\n5.exit")
    op=int(input("enter the coressponding no. of your choice::"))
    if op==1:
        print("items exixting in our menu are::",a1.menu_items)
        name=input("enter name of item to be added:")
        if name in a1.menu_items:
            print("we have this item already!!")
        else:
            price=int(input("enter price of this item:"))
            a1.menu(name,price)
            print("item added successfully!!\nnew menu includes::",a1.menu_items)
    if op==2:
        confirm=input("enter y if you are sure to book a table:")
        if confirm=='y':
            a1.table()
    if op==3:
        print("menu includes::",a1.menu_items)
        ord=[]
        for i in range(10):
            ch=input("enter your order::")
            if ch in a1.menu_items:
                ord.append(ch)
            else:
                print("you typed something wrong!!try again!!\n**************************************")
            k=input("press'y' to enter furthur items::")
            if k =='y':
                continue
            else:
                a1.order(ord)
                break                
        else:
            print("we dont have this item in our menu!!!")
    if op==4:
        a1.display()
    if op==5:
        break
    else:
        print("***************************************************************************")
        continue