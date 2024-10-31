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
##cars_info table 
create_query_carsinfo = """
CREATE TABLE IF NOT EXISTS CARS_INFO(
    car_id INT PRIMARY KEY,
    car_model varchar(50),
    year_of_manufacture varchar(5),
    car_plate_number varchar(40),
    seats int,
    fuel_type varchar(10),
    transmission_mode varchar(15),
    rental_status varchar(15),
)
"""

