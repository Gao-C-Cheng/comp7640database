from handlers import items, orders, customer

item1 = items('localhost', 3306, 'root', '', 'retail')
item1.insert_item(2,'notebook',10.3,'stationery',20)
item1.add_item(5,10)
#sql = f'''insert into items (iditems,Itname,prince,keyword,qty) values ({2},{'n'},{10.3},{'s'},{10});'''
print()

order = orders('localhost', 3306, 'root', '', 'retail')

customer1 = customer('localhost', 3306, 'root', '', 'retail')

print(customer1.contains_ID(3))
customer1.insert_customer(3,'201 spring graden', 'ryan')

itlist=[1,2]
qtylist=[3,2]

customer1.place_order(1,itlist,qtylist)