from colorama import Fore , init, Style
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
    car_type varchar(20),
    car_colour varchar(20),
    seats int,
    fuel_type varchar(10),
    transmission_mode varchar(15),
    rental_status varchar(15),
    rental_cost_per_km int
)
"""
cursor.execute(create_query_carsinfo)

##cars_rented status table
create_query_carsrented = """
CREATE TABLE IF NOT EXISTS CARS_RENTED(
    car_id INT,
    customer_id INT,
    FOREIGN KEY(car_id) REFERENCES CARS_INFO(car_id),
    FOREIGN KEY(customer_id) REFERENCES CUSTOMERS(customer_id),
    fuel_in_litres int,
    rent_date DATE,
    return_date DATE,
    cost int
)
"""
cursor.execute(create_query_carsrented)

##maintenance table 
create_query_maintenance = """
CREATE TABLE IF NOT EXISTS MAINTENANCE(
    car_id int,
    FOREIGN KEY(car_id) REFERENCES CARS_INFO(car_id),
    last_service DATE,
    next_service DATE,
    service_type varchar(20),
    service_cost int,
    parts_replaced varchar(20)
) 
"""

cursor.execute(create_query_maintenance)

##employee table
create_query_employee = """
CREATE TABLE IF NOT EXISTS EMPLOYEE(
    em_id INT PRIMARY KEY,
    em_name varchar(30),
    em_role varchar(30),
    salary INT
)
"""

cursor.execute(create_query_employee)

###############################################################################################################
##user functions##
#add records#
def add_records_carsinfo():
    while True:
        carid = int(input("Enter CAR ID : "))
        carmodel = input("Enter car model : ").lower()
        yom = input("Enter year of manufacture of car : ").lower()
        carpn = input("Enter car's registration no. : ").lower()
        cart = input("Enter car type : ").lower()
        carc = input("Enter car color : ").lower()
        seat = int(input("Enter the number of seats in the car : "))
        fuelt = input("Enter the fuel type (petrol/diesel/CNG): ").lower()
        transmissionmode = input("Enter transmission mode (automatic/manual): ").lower()
        rentals = input("Rented/unrented : ").lower()
        renc = int(input("Rent per Km : "))
        
        
        insq = "INSERT INTO CARS_INFO VALUES ('" + str(carid) + "', '" + carmodel + "', '" + yom + "', '" + carpn + "', '" + cart + "', '" + carc + "', " + str(seat) + ", '" + fuelt + "', '" + transmissionmode + "', '" + rentals + "', " + str(renc) + ")"
        cursor.execute(insq)
        mydb.commit()
        insqq = "INSERT INTO MAINTENANCE VALUES('"+str(carid)+"',NULL,NULL,'None',NULL,'-');"
        cursor.execute(insqq)
        mydb.commit()
        while True:
            cont = input("Add more records (y/n)? : ").lower()
            if cont == "y":
                break  
            elif cont == "n":
                return  
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def add_records_customers():
    while True:
        cuid = int(input("Enter customers id : "))
        cuname = input("Enter customers name : ").lower()
        cadd = input("Enter address for customer : ").lower()
        payment = input("Enter payment method for customers (if done) :").lower()
        ids = input("Enter id sumbitted by customer for proof :").lower()
        insqq = "INSERT INTO CUSTOMERS values('" +str(cuid)+"','"+cuname+"','"+cadd+"','"+payment+"','"+ids+"');"
        cursor.execute(insqq)
        mydb.commit()
        while True:
            contt = input("Add more records (y/n)? : ").lower()
            if contt == "y":
                break  
            elif contt == "n":
                return  
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

            
def add_records_carrented():
    while True:
        card = int(input("Enter the carid of rented car: "))
        cud = int(input("Enter the customerid of the customer: "))
        fil = int(input("Enter the amount of fuel present: "))
        rentd = input("Enter the rent date (YYYY-MM-DD): ")
        retd = input("Enter the return date (YYYY-MM-DD): ")
        cost = int(input("Enter the amount paid by customer: "))
        
        insq = """
        INSERT INTO CARS_RENTED (car_id, customer_id, fuel_in_litres, rent_date, return_date, cost)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
        """.format(card, cud, fil, rentd, retd, cost)
        
        cursor.execute(insq)
        mydb.commit()
        
        while True:
            contt = input("Add more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def add_records_maintenance():
    while True:
        cid = int(input("Enter car Id : "))
        
        ld = input("Enter the date for last service (YYYY-MM-DD) or leave blank for NULL: ")
        ld = "NULL" if ld.strip() == "" else f"'{ld}'"
        
        nd = input("Enter the date for next service (YYYY-MM-DD) or leave blank for NULL: ")
        nd = "NULL" if nd.strip() == "" else f"'{nd}'"

        st = input("Enter the type of service(if any) : ").lower()
        sc = int(input("Enter the cost for service : "))
        pr = input("Parts replaced(if any) : ").lower()

        insq = f"""
        INSERT INTO MAINTENANCE(car_id, last_service, next_service, service_type, service_cost, parts_replaced)
        VALUES({cid}, {ld}, {nd}, '{st}', {sc}, '{pr}')
        """

        cursor.execute(insq)
        mydb.commit()

        while True:
            contt = input("Add more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def add_records_employee():
    while True:
        emid = int(input("Enter employee id : "))
        emname = input("Enter employee name : ").lower()
        emrole = input("Enter employees role : ").lower()
        salary = input("Enter empoyees salary : ").lower()
        insq = "INSERT INTO EMPLOYEE values('"+str(emid)+"','"+emname+"','"+emrole+"','"+str(salary)+"');"
        cursor.execute(insq)
        mydb.commit()
        while True:
            contt = input("Add more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

##########################################################################################################################################update function#

def update_records_carinfo():
    while True:
        print("Current records : ")
        cursor.execute("SELECT * FROM CARS_INFO;")
        data = cursor.fetchall()
        avail_ids = []
        for i in data:
            print(i)
            avail_ids.append(i[0])
        q = int(input("For which Car ID do you want to update records? : "))
        if q not in avail_ids:
            print("Please enter a valid car id")
            continue  

        print("1. Car model")
        print("2. Year of manufacture")
        print("3. Car plate number")
        print("4. Car type")
        print("5. Car colour")
        print("6. Number of seats")
        print("7. Fuel type")
        print("8. Transmission mode")
        print("9. Rental status")
        print("10. Rental cost per kilometer")
        
        r = int(input("Which info do you want to update? : "))
        
        if r == 1:
            newm = input("Enter new car model : ")
            cursor.execute("UPDATE CARS_INFO SET car_model='" + newm + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 2:
            newy = input("Enter new year of manufacture : ")
            cursor.execute("UPDATE CARS_INFO SET year_of_manufacture='" + newy + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 3:
            newp = input("Enter new plate number : ")
            cursor.execute("UPDATE CARS_INFO SET car_plate_number='" + newp + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 4:
            newt = input("Enter new car type : ")
            cursor.execute("UPDATE CARS_INFO SET car_type='" + newt + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 5:
            newc = input("Enter new car color : ")
            cursor.execute("UPDATE CARS_INFO SET car_colour='" + newc + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 6:
            news = int(input("Enter new number of seats : "))
            cursor.execute("UPDATE CARS_INFO SET seats=" + str(news) + " WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 7:
            newf = input("Enter the new fuel type : ")
            cursor.execute("UPDATE CARS_INFO SET fuel_type='" + newf + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 8:
            newm = input("Enter new mode for car : ")
            cursor.execute("UPDATE CARS_INFO SET transmission_mode='" + newm + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 9:
            newr = input("Enter rental status : ")
            cursor.execute("UPDATE CARS_INFO SET rental_status='" + newr + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        elif r == 10:
            newrc = input("Enter new rental cost : ")
            cursor.execute("UPDATE CARS_INFO SET rental_cost_per_km='" + newrc + "' WHERE car_id=" + str(q) + ";")
            mydb.commit()
        else:
            print("Invalid choice.")


        while True:

            contt = input("Update more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")    
                


            
def update_records_customers():
    while True:
        print("Current Records:")
        cursor.execute("SELECT * FROM CUSTOMERS;")
        data = cursor.fetchall()
        avails_ids = []
        for i in data:
            print(i)
            avails_ids.append(i[0])
        q = int(input("Enter the customer id for which you want to update : "))
        if q not in avails_ids:
            print("Please enter a valid customer id")
        else:
            print("1. Customer name")
            print("2. Customer address")
            print("3. Payment")
            print("4. Id submitted")
            r = int(input("Which record do you want to update? : "))
            if r == 1:
                newn = input("Enter customer's new name : ")
                cursor.execute("UPDATE CUSTOMERS SET customer_name='" + newn + "' WHERE customer_id=" + str(q) + ";")
                mydb.commit()
            elif r == 2:
                newa = input("Enter customer's new address: ")
                cursor.execute("UPDATE CUSTOMERS SET customer_address='" + newa + "' WHERE customer_id=" + str(q) + ";")
                mydb.commit()
            elif r == 3:
                newp = input("Enter new payment method : ")
                cursor.execute("UPDATE CUSTOMERS SET payment='" + newp + "' WHERE customer_id=" + str(q) + ";")
                mydb.commit()
            elif r == 4:
                newi = input("Enter new id : ")
                cursor.execute("UPDATE CUSTOMERS SET id_submitted='" + newi + "' WHERE customer_id=" + str(q) + ";")
                mydb.commit()
            else:
                print("Inavlid choice")

            while True:

                contt = input("Update more records (y/n)? : ").lower()
                if contt == "y":
                    break
                elif contt == "n":
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def update_records_carsrented():
    while True:
        print("Current Records :")
        cursor.execute("SELECT * from CARS_RENTED;")
        data = cursor.fetchall()
        avail_ids = []
        for i in data:
            print(i)
            avail_ids.append(i[0])
        q = int(input("Enter the car id to update :"))
        if q not in avail_ids:
            print("Please enter valid car id")
        else:
            print("1.Fuel")
            print("2.Rent Date")
            print("3.Return Date")
            print("4.Cost")
            r=int(input("Enter the record you want to change : "))

            if r == 1:
                newf = int(input("Enter new amount of fuel : "))
                cursor.execute("UPDATE CARS_RENTED SET fuel_in_litres="+str(newf)+" WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r == 2:
                newd = input("Enter rent date(YYYY-MM-DD): ")
                cursor.execute("UPDATE CARS_RENTED SET rent_date='"+newd+"' WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r==3:
                newrd = input("Enter return date(YYYY-MM-DD): ")
                cursor.execute("UPDATE CARS_RENTED SET return_date='"+newrd+"' WHERE car_id="+str(q)+";")
                mydb.commit()

            elif r==4:
                newc = int(input("Enter new cost for rental : "))
                cursor.execute("UPDATE CARS_RENTED SET cost="+str(newc)+" WHERE car_id="+str(q)+";")
                mydb.commit()
            else:
                print("")
            while True:

                contt = input("Update more records (y/n)? : ").lower()
                if contt == "y":
                    break
                elif contt == "n":
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def update_records_maintenance():
    while True:
        print("Current Records:")
        cursor.execute("Select * from MAINTENANCE;")
        data = cursor.fetchall()
        avail_ids=[]
        for i in data:
            print(i)
            avail_ids.append(i[0])

        q = int(input("Enter car id to update maintenance record for : "))
        if q not in avail_ids:
            print("Please enter a valid car ID")
        else:
            print("1.Last service date")
            print("2.Next service date")
            print("3.Service Type")
            print("4.Service cost")
            print("5.Parts Replaced")
            r = int(input("Enter the record to update : "))
            if r == 1:
                newld = input("Enter last service date(YYYY-MM-DD) : ")
                cursor.execute("UPDATE MAINTENANCE SET last_service='"+newld+"' WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r == 2:
                newnd = input("Enter next service date(YYYY-MM-DD) :")
                cursor.execute("UPDATE MAINTENANCE SET next_service='"+newnd+"' WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r==3:
                newt=input("Enter new type of service : ")
                cursor.execute("UPDATE MAINTENANCE SET service_type='"+newt+"' WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r==4:
                newc = int(input("Enter new service cost : "))
                cursor.execute("UPDATE MAINTENANCE SET service_cost="+str(newc)+" WHERE car_id="+str(q)+";")
                mydb.commit()
            elif r==5:
                newp = input("Enter part replaced : ")
                cursor.execute("UPDATE MAINTENANCE SET parts_replaced='"+newp+"' WHERE car_id="+str(q)+";")
                mydb.commit()
            else:
                print("Please enter valid input")
                continue
            while True:

                contt = input("Update more records (y/n)? : ").lower()
                if contt == "y":
                    break
                elif contt == "n":
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def update_records_employees():
    while True:
        print("Current records:")
        cursor.execute("Select * from EMPLOYEE;")
        data = cursor.fetchall()
        avail_ids=[]
        for i in data:
            print(i)
            avail_ids.append(i[0])
        q = int(input("Enter employee id to update records for : "))
        if q not in avail_ids:
            print("Please enter valid employee id")
        else:
            print("1.Employee name")
            print("2.Employee role")
            print("3.Salary")
            r = int(input("Enter which record to update: "))
            if r == 1:
                newn = input("Enter new name for employee: ")
                cursor.execute("UPDATE EMPLOYEE SET em_name='"+newn+"' WHERE em_id="+str(q)+";")
                mydb.commit()
            elif r == 2:
                newr = input("Enter new role for employee : ")
                cursor.execute("UPDATE EMPLOYEE SET em_role='"+newr+"' WHERE em_id="+str(q)+";")
                mydb.commit()
            elif r == 3:
                news = int(input("Enter new salary : "))
                cursor.execute("UPDATE EMPLOYEE SET salary="+str(news)+" WHERE em_id="+str(q)+";")
                mydb.commit()
            else:
                print("Please enter valid record")

            while True:

                contt = input("Update more records (y/n)? : ").lower()
                if contt == "y":
                    break
                elif contt == "n":
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")

#########################################################################################################################################
#delete function#

def delete_records():
    while True:
        print("1.Cars Info")
        print("2.Cars Rented")
        print("3.Customer")
        print("4.Maintenance")
        print("5.Employee")
        q = int(input("Enter which table you want to update : "))
        if q ==1:
            print("Current record :")
            cursor.execute("SELECT * FROM CARS_INFO;")
            data1 = cursor.fetchall()
            avail_id1 = []
            for i in data1:
                print(i)
                avail_id1.append(i[0])
            r1 = int(input("Enter id for which record is to be deleted : "))
            try:
                cursor.execute("DELETE FROM CARS_INFO WHERE car_id="+str(r1)+";")
                mydb.commit()
            except:
                print("Please delete records from dependent tables first!")
             
        elif q == 2:
            print("Current Records :")
            cursor.execute("SELECT * FROM CARS_RENTED;")
            data2 = cursor.fetchall()
            avail_id2 = []
            for i in data2:
                print(i)
                avail_id2.append(i[0])
            r2 = int(input("Enter id for which record is to be deleted : "))
            cursor.execute("DELETE FROM CARS_RENTED WHERE car_id="+str(r2)+";")
            mydb.commit()

        elif q == 3:

            print("Current Records :")
            cursor.execute("SELECT * FROM CUSTOMERS;")
            data3 = cursor.fetchall()
            avail_id3 = []
            for i in data3:
                print(i)
                avail_id3.append(i[0])
            r3 = int(input("Enter id for which record is to be deleted : "))
            cursor.execute("DELETE FROM CUSTOMERS WHERE customer_id="+str(r3)+";")
            mydb.commit()

        elif q == 4:

            print("Current Records :")
            cursor.execute("SELECT * FROM MAINTENANCE;")
            data4 = cursor.fetchall()
            avail_id4 = []
            for i in data4:
                print(i)
                avail_id4.append(i[0])
            r4 = int(input("Enter id for which record is to be deleted : "))
            cursor.execute("DELETE FROM MAINTENANCE WHERE car_id="+str(r4)+";")
            mydb.commit()

        elif q == 5:

            print("Current records")
            cursor.execute("SELECT * FROM EMPLOYEE;")
            data5 = cursor.fetchall()
            avail_ids5 = []
            for i in data5:
                print(i)
                avail_ids5.append(i[0])
            r5=int(input("Enter id for which record is to be delete : "))
            cursor.execute("DELETE FROM EMPLOYEE WHERE em_id="+str(r5)+";")
            mydb.commit()

        else:
            print("Please enter valid table number")
        while True:

            contt = input("Delete more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

########################################################################################################################################
#search function 


def search_records():
    while True:
        print("1.Car records")
        print("2.Maintenance records")
        print("3.Employee records")
        print("4.Customer records")
        x = int(input("Enter which records you want to seach : "))
        if x == 1:
            y = int(input("Enter car id to search for : "))
            cursor.execute("select * from CARS_INFO;")
            found_info = False
            datax = cursor.fetchall()
            cursor.execute("select * from CARS_RENTED;")
            datay = cursor.fetchall()
            for i in datax:
                if i[0]==y:
                    print("Data found from CARS_INFO table")
                    print(i)
                    found_info=True
            for m in datay:
                if m[0]==y:
                    print("Data found from CARS_RENTED")
                    print(m)
                    found_info=True
            if found_info == False:
                print("No data found!")

        elif x == 2:
            n = int(input("Enter car id to search for: "))
            cursor.execute("select * from MAINTENANCE;")
            found_info1=False
            datan = cursor.fetchall()
            for j in datan:
                if j[0] == n:
                    print("Data found")
                    print(j)
                    found_info1=True
            if found_info1==False:
                print("No data found")
        elif x == 3:
            o = int(input("Enter employee id to search for : "))
            cursor.execute("Select * from EMPLOYEE;")
            found_info2=False
            datao = cursor.fetchall()
            for l in datao:
                if l[0]==o:
                    print("Data found")
                    print(l)
                    found_info2=True
            if found_info2==False:
                print("No record found")
        elif x == 4:
            v = int(input("Enter customer id to search for : "))
            cursor.execute("select * from CUSTOMERS;")
            datav = cursor.fetchall()
            found_info3=False
            for u in datav:
                if u[0]==v:
                    print("Data found")
                    print(u)
                    found_info=True
            if found_info3 == False:
                print("No record found")

        while True:

            contt = input("Search more records (y/n)? : ").lower()
            if contt == "y":
                break
            elif contt == "n":
                return
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

##########################################################################################################################################list available cards customizable search function#

def list_avail_cars():
    selected_parameter = []
    while True:
        print("1.Seats")
        print("2.Year of manufacture")
        print("3.Car Model")
        print("4.Car type")
        print("5.Car colour")
        print("6.Fuel type")
        print("7.Transmission mode")
        
        r = int(input("Enter the customization : "))
        query = "SELECT * FROM CARS_INFO WHERE rental_status='unrented'"
        if r in selected_parameter:
            print("You cannot choose two customizations for one parameter.")
            continue
        elif r == 1:
            ns = int(input("How many seats do you want in the car : "))
            query += " AND seats="+str(ns)+""
            selected_parameter.append(r)
        
        elif r == 2:
            ym = input("Enter the year of manufacture for the car : ").lower()
            query += " AND year_of_manufacture='"+ym+"'"
            selected_parameter.append(r)
        
        elif r==3:
            cm = input("Enter car model : ").lower()
            query += " AND car_model='"+cm+"'"
            selected_parameter.append(r)
        elif r==4:
            ct = input("Enter car type(sports/suv/sedan) : ").lower()
            query += " AND car_type='"+ct+"'"
            selected_parameter.append(r)
        elif r==5:
            cc = input("Enter car colour : ").lower()
            query += " AND car_colour='"+cc+"'"
            selected_parameter.append(r)
        elif r==6:
            tm = input("Enter fuel type(diesel/petrol/CNG) : ").lower()
            query += " AND fuel_type='"+tm+"'"
            selected_parameter.append(r)
        elif r==7:
            ft = input("Enter transmission mode : ").lower()
            query += " AND transmission_mode='"+ft+"'"
        else:
            print("Please enter valid records")
            continue

        while True:
            print("1.Customize more")
            print("2.Display results")
            print("3.Exit")
            cont = int(input(""))
            if cont == 1:
                break
            elif cont == 2:
                query += ";"
                print(query)
                cursor.execute(query)
                data = cursor.fetchall()
                for i in data:
                    print(i)
            elif cont == 3:
                return
            else:
                print("Enter valid input")
#########################################################################################################################################
#rent a car function#

def rentcar():
    cursor.execute("SELECT * FROM CARS_INFO WHERE rental_status='unrented';")
    data = cursor.fetchall()
    for i in data:
        print(i)
    r = int(input("Enter the car id you want to rent : "))
    fuel = int(input("Enter the current fuel in car : "))
    c = int(input("Enter customer ID : "))
    rentd = input("Enter rent date(YYYY-MM-DD): ")
    retd = input("Enter return date(YYYY-MM-DD): ")
    cos = int(input("Enter cost for rental : "))
    cursor.execute("UPDATE CARS_INFO SET rental_status='rented' WHERE car_id="+str(r)+";")
    mydb.commit()
    try:
        cursor.execute("INSERT INTO CARS_RENTED values('"+str(r)+"','"+str(c)+"','"+str(fuel)+"','"+rentd+"','"+retd+"','"+str(cos)+"' );")
        mydb.commit()
        print("Car successfully Rented")
    except:    
        print("Please make sure that car id exists and/or customer id exists already. If not please register.")


#########################################################################################################################################
#return a car function#

def returncar():
    print("Rented Cars: ")
    cursor.execute("SELECT * FROM CARS_RENTED;")
    data = cursor.fetchall()
    for i in data:
        print(i)
    while True:
        if len(data)==0:
            break
        r = int(input("Enter CARID to return : "))
        cursor.execute("SELECT * FROM CARS_RENTED;")
        data = cursor.fetchall()
        rented_cars=[]
        for i in data:
            rented_cars.append(i[0])
        if r not in rented_cars:
            print("Please enter valid car id")
        else:
            break
    try:
        cursor.execute("DELETE FROM CARS_RENTED WHERE car_id="+str(r)+";")
        mydb.commit()
        cursor.execute("UPDATE CARS_INFO SET rental_status='unrented' WHERE car_id="+str(r)+";")
        mydb.commit()
        print("Car successfully returned!")
    except:
        print("NO cars have been rented!")

##########################################################################################################################################view records function#

def viewrecords():
    while True:
        print("1.Cars info")
        print("2.Rented cars")
        print("3.Maintenance records")
        print("4.Customer records")
        print("5.Employee records")
        r = int(input("Which records do you want to view? : "))
        if r == 1:
            cursor.execute("SELECT * FROM CARS_INFO;")
            data1 = cursor.fetchall()
            for i in data1:
                print(i)
            if len(data1) == 0:
                print("empty")
        elif r == 2:
            cursor.execute("SELECT * FROM CARS_RENTED;")
            data2 = cursor.fetchall()
            for i in data2:
                print(i)
            if len(data2) == 0:
                print("empty")

        elif r == 3:
            cursor.execute("SELECT * FROM MAINTENANCE;")
            data3 = cursor.fetchall()
            for i in data3:
                print(i)
            if len(data3) == 0:
                print("empty")

        elif r == 4:
            cursor.execute("SELECT * FROM CUSTOMERS;")
            data4 = cursor.fetchall()
            for i in data4:
                print(i)
            if len(data4) == 0:
                print("empty")

        elif r == 5:
            cursor.execute("SELECT * FROM EMPLOYEE;")
            data5 = cursor.fetchall()
            for i in data5:
                print(i)
            if len(data5) == 0:
                print("empty")
        else:
            print("Please Enter valid record")

        while True:
            cont = input("View more records(y/n) : ").lower()
            if cont == "y":
                break
            elif cont == "n":
                return
            else:
                print("")

#########################################################################################################################################
#cost fucntion#

def costest():
    while True:
        cursor.execute("SELECT * FROM CARS_INFO;")
        data = cursor.fetchall()
        for i in data:
            print(i)
        r = int(input("For which  car id do you want to estimate the cost : "))
        kms = int(input("Please enter approx. distance to be travelled in kms : "))
        for i in data:
            if i[0] == r:
                rentperkm = i[10]
        cost = rentperkm*kms

        print("The total cost for the car will be")
        print("Base Amount : ", cost)
        print("Fuel cost :", 8*kms )
        print("Insurance(Will be paid back if no damanges are found ) : ", 2000)
        print("Total = $",cost+8*kms+2000)

        while True:
            cont = input("Calculate again? (y/n)").lower()
            if cont == "y":
                break
            elif cont == "n":
                return
            else:
                continue
#########################################################################################################################################
#DESIGN#
def ascii_design():
    init()
    ascii_art = [
        "   █████████    █████████   ███████████   ",
        "  ███░░░░░███  ███░░░░░███ ░░███░░░░░███ ",
        " ███     ░░░  ░███    ░███  ░███    ░███ ",
        "░███          ░███████████  ░██████████   ",
        "░███          ░███░░░░░███  ░███░░░░░███ ",
        "░░███     ███ ░███    ░███  ░███    ░███ ",
        " ░░█████████  █████   █████ █████   █████",
        "  ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░   ░░░░░ "
    ]    

    for line in ascii_art:
        print(Fore.RED + line.center(80) + Fore.RESET)



    ascii_art2 = [
        " ███████████   ██████████ ██████   █████ ███████████   █████████   █████      ",
        "░░███░░░░░███ ░░███░░░░░█░░██████ ░░███ ░█░░░███░░░█  ███░░░░░███ ░░███       ",
        " ░███    ░███  ░███  █ ░  ░███░███ ░███ ░   ░███  ░  ░███    ░███  ░███       ",
        " ░██████████   ░██████    ░███░░███░███     ░███     ░███████████  ░███       ",
        " ░███░░░░░███  ░███░░█    ░███ ░░██████     ░███     ░███░░░░░███  ░███       ",
        " ░███    ░███  ░███ ░   █ ░███  ░░█████     ░███     ░███    ░███  ░███      █",
        " █████   █████ ██████████ █████  ░░█████    █████    █████   █████ ███████████",
        "░░░░░   ░░░░░ ░░░░░░░░░░ ░░░░░    ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░░ "
    ] 

    for line in ascii_art2:
        print(Fore.GREEN+ line.center(80) + Fore.RESET)


    ascii_art1 = [
        "  █████████  █████ █████  █████████  ███████████ ██████████ ██████   ██████",
        " ███░░░░░███░░███ ░░███  ███░░░░░███░█░░░███░░░█░░███░░░░░█░░██████ ██████ ",
        "░███    ░░░  ░░███ ███  ░███    ░░░ ░   ░███  ░  ░███  █ ░  ░███░█████░███ ",
        "░░█████████   ░░█████   ░░█████████     ░███     ░██████    ░███░░███ ░███ ",
        " ░░░░░░░░███   ░░███     ░░░░░░░░███    ░███     ░███░░█    ░███ ░░░  ░███ ",
        " ███    ░███    ░███     ███    ░███    ░███     ░███ ░   █ ░███      ░███ ",
        "░░█████████     █████   ░░█████████     █████    ██████████ █████     █████",
        " ░░░░░░░░░     ░░░░░     ░░░░░░░░░     ░░░░░    ░░░░░░░░░░ ░░░░░     ░░░░░ "
    ]

    for line in ascii_art1:
        print(Fore.BLUE + line.center(80) + Fore.RESET)


    menu_options = [
        "1.  Add Records",
        "2.  Update Records",
        "3.  Delete Records",
        "4.  Search Records",
        "5.  View Records",
        "6.  Search for Available Cars",
        "7.  Rent Car",
        "8.  Return Car",
        "9.  Calculate Cost",
        "0.  Exit"
    ] 
    indentation = " " * 8  
    ind2 = " "*3
    print(Fore.CYAN + Style.BRIGHT + indentation + "=" * 60)
    print(indentation + "                   Car Rental System Menu" + indentation)
    print(Fore.CYAN + indentation + "=" * 60 + Style.RESET_ALL)

    for option in menu_options:
        print(Fore.GREEN + Style.BRIGHT + indentation+ind2 + option.center(60 - len(indentation)) + Style.RESET_ALL)

    print(Fore.CYAN + indentation + "=" * 60 + Style.RESET_ALL)

#########################################################################################################################################
#WHILE LOOP#

while True:
    ascii_design()
    inpt = int(input(""))
    if inpt == 1:
        print("1)CARS_INFO")
        print("2)CARS_RENTED")
        print("3)MAINTENANCE")
        print("4)EMPLOYEE")
        print("5)CUSTOMERS")
        change1 = int(input("Which table do you want to enter records in : "))
        if change1 == 1:
            add_records_carsinfo()
        elif change1==2:
            add_records_carrented()
        elif change1==3:
            add_records_maintenance()
        elif change1==4:
            add_records_employee()
        elif change1==5:
            add_records_customers()
        else:
            print("Please enter valid input")
    elif inpt == 2:
        print("1)CARS_INFO")
        print("2)CARS_RENTED")
        print("3)MAINTENANCE")
        print("4)EMPLOYEE")
        print("5)CUSTOMERS")
        change2 = int(input("Which table do you want to update records for : "))
        if change2 == 1:
            update_records_carinfo()
        elif change2==2:
            update_records_carsrented()
        elif change2==3:
            update_records_maintenance()
        elif change2==4:
            update_records_employees()
        elif change2==5:
            update_records_customers()
        else:
            print("Please enter valid input")
    elif inpt == 3:
        delete_records()
    elif inpt == 4:
        search_records()
    elif inpt==5:
        viewrecords()
    elif inpt==6:
        list_avail_cars()
    elif inpt==7:
        rentcar()
    elif inpt==8:
        returncar()
    elif inpt==9:
        costest()
    elif inpt==0:
        print("HAVE A GOOD DAY!")
        break
    else:
        continue

################################################ END-OF-PROGRAM #########################################################################


