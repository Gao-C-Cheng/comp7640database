import pymysql

class add_operation:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def add_website(self,idwebsite,WebsitName):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into website (idwebsite,WebsitName) values (%s,%s);
        """
        cursor.execute(sql, [idwebsite,WebsitName])
        
        db.commit()        
        cursor.close()
        db.close()
    def add_shop(self,idshop,sname,rating,Location,idwebsite):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into shop (idshop,sname,rating,Location,idwebsite) values (%s,%s,%s,%s,%s);
        """
        cursor.execute(sql, [idshop,sname,rating,Location,idwebsite])
        
        db.commit()        
        cursor.close()
        db.close()

    def add_items(self,iditems,Itname,prince,keyword,idshop):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into items (iditems,Itname,prince,keyword,idshop) values (%s,%s,%s,%s,%s);
        """
        cursor.execute(sql, [iditems,Itname,prince,keyword,idshop])
        
        db.commit()        
        cursor.close()
        db.close()

    def add_order_has_items(self,idorders,idItems,order_date):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into order_has_items (idorders,idItems,order_date) values (%s,%s,%s);
        """
        cursor.execute(sql, [idorders,idItems,order_date])
        
        db.commit()        
        cursor.close()
        db.close()
    
    def add_orders(self,idorders,qty,idcustomer,order_date):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into orders (idorders,qty,idcustomer,order_date) values (%s,%s,%s,%s);
        """
        cursor.execute(sql, [idorders,qty,idcustomer,order_date])
        
        db.commit()        
        cursor.close()
        db.close()

    def add_customer(self,idcustomer,address,cname):
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

        cursor = db.cursor()

        sql = """
        insert into customer (idcustomer,address,cname) values (%s,%s,%s);
        """
        cursor.execute(sql, [idcustomer,address,cname])
        
        db.commit()        
        cursor.close()
        db.close()



add_customer1 = add_operation("127.0.0.1", "root","123456","retail")
add_customer1.add_customer(6,"ac","a")
# add_customer1.add_website(1,"ac")
# add_customer1.add_shop(1,"ac",2,"saf",1)
# add_customer1.add_items(1,"ac",2.0,"saf",1)
# add_customer1.add_orders(1,1,1,1010)

