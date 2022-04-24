import pymysql
import handlers

def create_shop():
    shop_id=input("Enter your shop-id: ")
    shop_name=input("Enter your shop-name: ")
    shop_rating=input("Enter your shop-rating: ")
    shop_location=input("Enter your shop-location: ")
    shop_idwebsite=website_id
    try:
        shop = shop(host,port,user,password,database)
        shop.insert_shop(shop_id,shop_name,shop_rating,shop_location,shop_idwebsite)
        print("success")
    except:
        print("fail")


    string = f'''What do you want to do?
                    1. continue create a shop
                    2. shopping
                    3. add item to shop
                    4. delete shop
                    5. search shop
                    6. update shop'''
    temp = input(string)
    if temp == 1: create_shop()
    elif temp == 2: create_customer()
    elif temp == 3: item.add_item_to_shop()
    elif temp == 4: shop.delete_shop()
    elif temp == 5: shop.search_shop_by()
    elif temp == 6: shop.update_shop()



def create_customer():
    customer_id = input("Enter your customer-id: ")
    customer_address = input("Enter your customer-address: ")
    customer_name = input("Enter your customer-name: ")
    try:
        customer = customer(host,port,user,password,database)
        customer.insert_customer(customer_id, customer_address, customer_name)
        print("success")
    except:
        print("fail")

    string = f'''What do you want to do?
                    1. create a shop
                    2. shopping
                    3. delete customer account
                    4. place order'''
    temp = input(string)
    if temp == 1: create_shop()
    elif temp == 2: shopping()
    elif temp == 3: customer.delete_customer()
    elif temp == 4: customer.place_order()

def main():
    #connect the database
    string = f'''Welcome to our retail database
    Please connect the database first.'''
    print(string)
    host = input("Enter your host: ")
    port = input("Enter your port: ")
    user = input("Enter your user: ")
    password = input("Enter your password: ")
    database = input("Enter your database: ")

    #create website
    string = f'''Welcome to our retail database
    Please create the website first.'''
    print(string)
    website_id = input("Enter your website-id: ")
    website_name = input("Enter your website-name: ")
    try:
        website = website(host,port,user,passowrd,database)
        website.insert_website(website_id, website_name)
        print("success")
    except:
        print("fail")


    string = f'''What do you want to do?
                    1. create a shop
                    2. be a customer'''
    temp = input(string)
    if temp == 1:
        #create shop
        create_shop()

    elif temp == 2:
        #create customer
        create_customer()






if __name__ == '__main__':
    main()