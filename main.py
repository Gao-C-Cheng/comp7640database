from ast import keyword
from turtle import back
from handlers import shop, items, customer, orders
import pymysql

#'localhost', 3306, 'root', '', 'retail'
host = 'localhost'
port = 3306
user = 'root'
password = ''
database = 'retail'
shop1 = shop(host, port, user, password, database)
item = items(host, port, user, password, database)
customer1 = customer(host, port, user, password, database)
order = orders(host, port, user, password, database)


def main():
    q = True
    while q:
        string = f'''Welcome to our retail database
    choose your identity
    1.costumer
    2.supplyer
    3.exit
    Enter your value:'''
        val = input(string)
        if val == '1':
            print()
            customer_inferface()
        elif val == '2':
            print()
            supplyer_inferface()
        else:
            q = False

def supplyer_inferface():
    while True:
        command = input('''
    press 1. if you are shops owner
    press 2. if you are supplyer
    press q or any other key to go back:
    ''')
        if command == '1':
            shop_owner()
        elif command == '2':
            supplyer()
        else:
            return

def shop_owner():
    while True:
        shop1.show_all_shop()
        idshop = input(
    'please enter your shop ID (enter q go back to main meanu):')
        if idshop == 'q':
            return
        idshop = int(idshop)
        if shop1.contains_ID(idshop):
            your_shop(idshop)
        else:
            name = input("""
    we can't find your shop in our database 
    please input your shop name to sigin up an account:
    """)
            rating = 2
            location = input("""
    enter the address of your shop        
    """)    
            webid = 30
            try:
                shop1.insert_shop(idshop,name,rating,location,webid)
                print(f"""
    you have successfully sign up an account!, 
    your id is {idshop} !""")
            except (shop1.db.Error, shop1.db.Warning) as e:
                print(e)
                return

def your_shop(idshop:int):
    print(f'welcome {idshop}!')
    while True:
        command = input('''
        press 1.if you want to get items to your shop
        press 2.if you want to remove items to your shop
        press q or anyother key to go back:
        ''')
        if command=='1':
            print('all items in the market')
            item.show_all_items()
            print()
            print('all items in your shop')
            shop1.show_all_items_in_shop(idshop)
            good = input('enter a item id add to your shop (enter q to go back)')
            if good !='q':
                shop1.add_item_to_shop(good,idshop)
        elif command=='2':
            item.show_all_items()
            print()
            print('all items in your shop')
            shop1.show_all_items_in_shop(idshop)
            good = input('enter a item id remove from your shop (enter q to go back)')
            if good != 'q':
                shop1.remove_item_from_shop(good,idshop)
        else:
            return

def supplyer():
    while True:
        command = input('''
        you are suppler
        press 1.to add a item to the market
        press q or any other key to go back:

        ''')
        if command=='1':
            name = input('enter name of the item: ')
            prince = input('enter the prince should be a float')
            keyword =input('enter the searching key word')
            qty = input('enter number of item should be an int')
            item.insert_item(name,prince,keyword,qty)
        else:
            return

    

def customer_inferface():
    while True:
        idcustomer = input(
    'please enter your customer ID enter q go back to main meanu:')
        if idcustomer == 'q':
            return
        idcustomer = int(idcustomer)
        if customer1.contains_ID(idcustomer):
            welcome(idcustomer)
        else:
            name = input("""
    we can't find you in our database 
    please input your name to sigin up an account:
    """)
            address = input("please provide your address:")
            try:
                customer1.insert_customer(idcustomer, address, name)
                print(f"""
    you have successfully sign up an account!, 
    your id is {idcustomer} !""")
            except (customer1.db.Error, customer1.db.Warning) as e:
                print(e)
                return
    

def welcome(idcustomer: int):
    print(f'welcome! {idcustomer}')
    while True:
        command = input("""
    what do you want to do?
    press 1.place a order
    press 2.check and cancel your order
    press 3.to delete your account
    press anyother key to go back""")
        if command == '1':
            place_order(idcustomer)
        elif command == '2':
            check_order(idcustomer)
        elif command == '3':
            if delete_account(idcustomer):
                return
        else:
            print('back')
            return

def delete_account(idcustomer) ->bool:
    check = input('''
    Are you sure to delete your account?
    press yes to delete
    press any key to go back
    ''')
    if check=='yes':
        customer1.delete_customer(idcustomer)
        return True
    return False

def check_order(idcustomer:int):
    order.show_order_cid(idcustomer)
    command = input('cancel an order by using order id (press q to go back): ')
    if command=='q':
        return
    else:
        order.remove_order(int(command))


def place_order(idcustomer:int):
    item.show_all_items()
    itemlist = []
    qtylist = []
    row = input("""place your order!
    enter the items id in first entry 
    and number of items in the second entry
    split them with space enter q quit:
    """)
    while row != 'q':
        res = row.split(' ')
        itemlist.append(int(res[0]))
        qtylist.append(int(res[1]))
        row = input()

    if itemlist and qtylist:
        print(itemlist)
        print(qtylist)
        customer1.place_order(idcustomer, itemlist, qtylist)
    else:
        print('shopping list is empty!')


if __name__ == '__main__':
    main()
