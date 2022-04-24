from datetime import date
from operator import contains
import sqlite3
from unittest import result
import pymysql

class items:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cursor.close()
        self.db.close()
    
    def contains_ID(self,iditems:int) ->bool:
        ans = False
        cursor = self.cursor

        cursor.execute('select iditems from items')
        results = cursor.fetchall()
        for r in results:
            if iditems in r: ans = True
        
        return ans
    
    def get_item_qty(self,iditems:int) ->int:
        cursor = self.cursor

        cursor.execute('select qty from items where iditems=(%s)',[iditems])
        results = cursor.fetchall()[0][0]    
        return results

    def get_new_item_Id(self) ->int:
        cursor = self.cursor
        cursor.execute('select count(*) from items')
        num_of_items = cursor.fetchone()
        iditems = num_of_items[0]
        while self.contains_ID(iditems):
            iditems += 1
        return iditems

    def insert_item(self,Itname:str,prince:float,keyword:str,qty:int):
        db = self.db
        cursor = self.cursor
        #insert into items (iditems,Itname,prince,keyword,qty) values (1,'pencil',5.20,'stationery',10);
        iditems = self.get_new_item_Id()

        sql = f"""
            insert into items (iditems,Itname,prince,keyword,qty) values (%s,%s,%s,%s,%s);
            """
        try:
            cursor.execute(sql,[int(iditems),Itname,prince,keyword,qty])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)       
    
    def add_item(self,iditems:int,qty:int):
        db = self.db
        cursor = self.cursor

        sql = f'''
        select qty from items where idItems={iditems}
        '''
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            print('No such Item in our database!')
            return
        else:
            qty += results[0][0]
            sql = f'''update items set qty=(%s) where idItems=(%s);'''
            cursor.execute(sql,[qty,iditems])
            db.commit()
        

    def delete_item(self,Itname:str):
        db = self.db
        cursor = self.cursor
        try:
            sql = f'''
            delete from items where Itname=(%s);
            '''
            cursor.execute(sql,[Itname])

            db.commit()
        except (db.Error, db.Warning) as e:
            print(e)
    
    def show_all_items(self):
        db = self.db
        cursor = self.cursor
        sql = 'select * from items'
        
        try:
            cursor.execute(sql)
        except (db.Error,db.Warning) as e:
            print(e)
            return
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
            return
        for row in results:
            s = ''
            for cell in row:
                s = s + str(cell) + ', '
            print(s)

    def search_item_by(self,keyword:str):
        db = self.db

        cursor = self.cursor
        sql = f'''
        select * from items where keyword=(%s)
        '''
        try:
            cursor.execute(sql,[keyword])
        except (db.Error, db.Warning) as e:
            print(e)
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
            return
        for row in results:
            s = ''
            for cell in row:
                s = s + str(cell) + ', '
            print(s)


class orders:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.db.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.db.close()
    
    def containsID(self,idorders:int) ->bool:
        ans = False
        cursor = self.cursor

        cursor.execute('select idorders from orders')
        results = cursor.fetchall()
        for r in results:
            if idorders in r: ans = True
        
        return ans

    #insert into items (idorders,idcustomer,order_date) values (int,int,date);
    def get_new_order_Id(self) ->int:
        cursor = self.cursor
        cursor.execute('select count(*) from orders')
        num_of_orders = cursor.fetchone()
        idorder = num_of_orders[0]
        while self.containsID(idorder):
            idorder += 1
        return idorder

    def insert_order(self,idcutomer:int):
        db = self.db

        cursor = self.cursor
        idorders = self.get_new_order_Id()
        order_date = date.today()
        
        sql = f"""
            insert into orders (idorders,idcustomer,order_date) values (%s,%s,%s);
            """
        try:
            cursor.execute(sql,[int(idorders),idcutomer,order_date])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)
    
    def remove_order(self,idorders:int):
        db = self.db
        cursor = self.cursor
        sql = 'delete from orders where idorders=(%s);'

        try:
            cursor.execute(sql,[idorders])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)

    
    def show_order_cid(self,idcustomer:int):
        '''SELECT o.idorders, Itname, o.qty
            FROM items, order_has_items as o
            where items.idItems=o.idItems and o.idorders in (select idorders
												from orders
                                                where idcustomer=2);'''
        db = self.db
        cursor = self.cursor
        sql = f'''SELECT o.idorders, Itname, o.qty
            FROM items, order_has_items as o
            where items.idItems=o.idItems and o.idorders in (select idorders
												from orders
                                                where idcustomer={idcustomer});'''
        try:
            cursor.execute(sql)
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
            return
        for row in results:
            s = ''
            for cell in row:
                s = s + str(cell) + ', '
            print(s)

class customer:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.db.cursor()
        self.order = orders(host,port,user,password,database)
        self.items = items(host,port,user,password,database)
    #insert into customer (idcutomer,address,cname) values (int,str,str);
    
    def __del__(self):
        self.cursor.close()
        self.db.close()

    def contains_ID(self,idcutomer:int) ->bool:
        ans = False
        db = self.db

        cursor = self.cursor
        cursor.execute('select idcustomer from customer')
        results = cursor.fetchall()
        print(results)
        for r in results:
            if idcutomer in r: ans = True
        
        return ans

    def insert_customer(self,idcustomer:int, address:str, name:str):
        db = self.db

        cursor = self.cursor
        sql = f"""
            insert into customer (idcustomer,address,cname) values (%s,%s,%s);
            """
        try:
            cursor.execute(sql,[idcustomer,address,name])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)
    
    def delete_customer(self,idcustomer:str):
        db = self.db
        cursor = self.cursor
        sql = """
            delete from customer where idcustomer=(%s)
            """
        try:
            cursor.execute(sql,[idcustomer])
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)

    
    def place_order(self,idcustomer:str, items:list, qty:list):
        '''INSERT INTO table_name (column_list)
            VALUES
	        (value_list_1),
	        (value_list_2),
	        ...
	        (value_list_n);'''
        db = self.db
        cursor = self.cursor
        sql = 'insert into order_has_items (idorders,idItems,order_date,qty) values '
        data = ''
        for i in range(len(items)):
            if self.items.contains_ID(items[i]):
                order_id = self.order.get_new_order_Id()
                data += f'({order_id},{items[i]},"{date.today()}",{qty[i]}),'
            else:
                print('No such item!')
                return
        sql += data
        sql = sql[:-1] + ';'
        self.order.insert_order(idcustomer)
        try:
            print(sql)
            cursor.execute(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)

class shop:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cursor.close()
        self.db.close()
    
    def contains_ID(self,idshop:int) ->bool:
        ans = False
        db = self.db

        cursor = self.cursor
        cursor.execute('select idshop from shop')
        results = cursor.fetchall()
        print(results)
        for r in results:
            if idshop in r: ans = True
        
        return ans
    
    def show_all_shop(self):
        db = self.db
        cursor = self.cursor
         
        try:
            cursor.execute('select * from shop')
        except (db.Error, db.Warning) as e:
            print(e)
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
            return
        for row in results:
            s = ''
            for cell in row:
                s = s + str(cell) + ', '
            print(s)
    
    def show_all_items_in_shop(self,idshop:int):
        db = self.db
        cursor = self.cursor
        
        sql = f'''
        select * from items
        where idItems in (select idItems from shop_has_items where idshop={idshop})
        ''' 
        try:
            cursor.execute(sql)
        except (db.Error, db.Warning) as e:
            print(e)
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
            return
        for row in results:
            s = ''
            for cell in row:
                s = s + str(cell) + ', '
            print(s)


    def insert_shop(self,idshop:int,sname:str,rating:int,Location:str,idwebsite:int):
        db = self.db

        cursor = self.cursor

        sql = f"""
            insert into shop (idshop,sname,rating,Location,idwebsite) values (%s,%s,%s,%s,%s);
            """
        try:
            cursor.execute(sql,[idshop,sname,rating,Location,idwebsite])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)       
    
    def add_item_to_shop(self,idItems:int,idshop:int):
        db = self.db
        cursor = self.cursor
        
        sql = f'''
        insert into shop_has_items (idItems, idshop) values (%s,%s);
        '''
        try:
            cursor.execute(sql,[idItems, idshop])
            db.commit()
            print(sql)
        except (db.Error,db.Warning) as e:
            print(e)
        
    def remove_item_from_shop(self,idItems:int,idshop:int):
        db = self.db
        cursor = self.cursor
        
        sql = f'''
        delete from shop_has_items where iditems={idItems} and idshop={idshop};
        '''
        cursor.execute(sql)
        db.commit()

    def delete_shop(self,sname:str):
        db = self.db
        cursor = self.cursor

        try:
            sql = f'''
            delete from shop where sname=(%s);
            '''
            cursor.execute(sql,[sname])

            db.commit()
        except (db.Error, db.Warning) as e:
            print(e)
    
    def search_shop_by(self,sname:str):
        db = self.db

        cursor = self.cursor
        sql = f'''
        select * from shop where sname=(%s)
        '''
        try:
            cursor.execute(sql,[sname])
        except (db.Error, db.Warning) as e:
            print(e)
        results = cursor.fetchall()
        if len(results)==0:
            print('notthing')
        else:
            print("Shopname is "+ str(results[0][1])+", "+"rating is "+str(results[0][2])+", "+"location is "+str(results[0][3]))
            return

    def update_shop(self,sname:str, rating:int, Location:str, idshop:int):
        db = self.db
        cursor = self.cursor
        try:
            sql = f'''update shop set sname=(%s), rating=(%s), Location=(%s) where idshop=(%s);'''
            cursor.execute(sql,[sname,rating,Location,idshop])

            db.commit()
        except (db.Error, db.Warning) as e:
            print(e)

