import pymysql

class shop:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)


    def insert_shop(self,idshop:int,sname:str,rating:int,Location:str,idwebsite:int):
        db = self.db

        cursor = db.cursor()

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
        cursor.close()
        db.close()
    
    def add_item_to_shop(self,idItems:int,idshop:int):
        db = self.db

        cursor = db.cursor()
        sql = f'''
        insert into shop_has_items (idItems, idshop) values (%s,%s);
        '''
        cursor.execute(sql,[idItems, idshop])
        db.commit()
        
        cursor.close()
        db.close()

    def delete_shop(self,sname:str):
        db = self.db
        cursor = db.cursor()

        try:
            sql = f'''
            delete from shop where sname=(%s);
            '''
            cursor.execute(sql,[sname])

            db.commit()
        except (db.Error, db.Warning) as e:
            print(e)
        cursor.close()
        db.close()
    
    def search_shop_by(self,sname:str):
        db = self.db

        cursor = db.cursor()
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
    
shop1 = shop("localhost",3306,"root","123456","retail")
# shop1.insert_shop(1, "a", 1, "as", 1)
# shop1.delete_shop("a")
shop1.search_shop_by("a")
# shop1.add_item_to_shop(1,1)