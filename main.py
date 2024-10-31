import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="ppp",database="vatsalya",charset="utf8")
if mydb.is_connected():
    print("Connected successfully")
else:
    print("kys")

cursor = mydb.cursor()

##check if table exists if not create it
##customers table
create_query_customers = """
CREATE TABLE IF NOT EXISTS CUSTOMERS(
    customer_id INT PRIMARY KEY,
    customer_name varchar(40),
    customer_address varchar(60),
    payment varchar(40),
    id_submitted varchar(15)
)
"""
cursor.execute(create_query_customers)



