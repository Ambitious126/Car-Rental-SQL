import mysql.connector 
mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="ppp",database="vatsalya",charset="utf8")
if mydb.is_connected():
    print("Connected successfully")
else:
    print("kys")

cursor = mydb.cursor()

table_e = False
def CheckTable():
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    ex_table = []
    for i in tables:
        ex_table.append()
    if "customers" not in ex_tables:
        print("")
    else:
        cursor.execute("CREATE TABLE CUSTOMERS;")

CheckTable()
