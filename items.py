import pymysql

class items:
    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)


    def insert_item(self,iditems:int,Itname:str,prince:float,keyword:str,qty:int):
        db = self.db

        cursor = db.cursor()
        #insert into items (iditems,Itname,prince,keyword,qty) values (1,'pencil',5.20,'stationery',10);

        sql = f"""
            insert into items (iditems,Itname,prince,keyword,qty) values (%s,%s,%s,%s,%s);
            """
        try:
            cursor.execute(sql,[iditems,Itname,prince,keyword,qty])
            print(sql)
            db.commit()
        except (db.Error, db.Warning) as e:
            print(sql)
            print(e)       
        cursor.close()
        db.close()
    
    def add_item(self,iditems:int,qty:int):
        db = self.db

        cursor = db.cursor()
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
        
        cursor.close()
        db.close()

    def delete_item(self,Itname:str):
        db = self.db
        cursor = db.cursor()

        try:
            sql = f'''
            delete from items where Itname=(%s);
            '''
            cursor.execute(sql,[Itname])

            db.commit()
        except (db.Error, db.Warning) as e:
            print(e)
        cursor.close()
        db.close()
    
    def search_item_by(self,keyword:str):
        db = self.db

        cursor = db.cursor()
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
    