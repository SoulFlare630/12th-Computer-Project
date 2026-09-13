'''==========CAR SHOWROOM DATABASE==========
Made by:
Joel Ephrem Cebin
Adhinath V. K.
Alan Anil'''
debug = False
import mysql.connector

def dbconnect(usr, passwd):
    global db, crsr
    db = mysql.connector.connect(host = 'localhost', user = usr, password = passwd)
    crsr = db.cursor()
    
def setup():
    crsr.execute("create database if not exists carshowroom")
    crsr.execute("use carshowroom")
    crsr.execute("create table if not exists Customers (cust_id int primary key, name varchar(100) not null, phone varchar(15) not null, email varchar(100), address varchar(255))")
    crsr.execute("create table if not exists Inventory (car_id int primary key, make varchar(50) not null, model varchar(50) not null, year int not null, cost_price decimal(15, 2) not null, selling_price decimal(15, 2) not null, available_qty int default 0, reserved_qty int default 0, sold_qty int default 0)")
    crsr.execute("create table if not exists Staff (emp_id int primary key, name varchar(100) not null, passkey varchar(50), role varchar(20) not null, phone varchar(15) not null, salary decimal(10,2) not null, experience decimal(4, 2) not null)")
    crsr.execute("create table if not exists Transactions (txn_id int primary key, car_id int not null, cust_id int not null, emp_id int not null, sale_price decimal(15,2) not null, net_profit decimal(15,2) not null, status varchar(20) default 'Quote', txn_date date not null, quarter varchar(5) not null)")
    
    if debug:
        print("Table Setup Complete")
        crsr.execute('desc Customers')
        crsr.execute('desc Inventory')
        crsr.execute('desc Staff')
        crsr.execute('desc Transactions')


def dummies():
    crsr.execute("insert into Customers values (301, 'Rahul Menon', '9123456780', 'rahul.m@gmail.com', 'Kochi, Kerala'), (302, 'Anaya Nair', '9123456781', 'ananya.n@gmail.com', 'Trivandrum, Kerala'), (303, 'Deepak George', '9123456782', 'deepak.g@outlook.com', 'Kottayam, Kerala')")
    crsr.execute("insert into Inventory values (201, 'Toyota', 'Urban Cruiser Hyryder', 2025, 1600000.00, 1850000.00, 4, 1, 2), (202, 'Honda', 'City ZX', 2025, 1400000.00, 1650000.00, 5, 0, 1), (203, 'Kia', 'Seltos GTX+',2025, 1700000.00, 1950000.00, 2, 2, 3), (204, 'Maruti Suzuki', 'Brezza ZXi', 2024, 950000.00, 1100000.00, 6, 1, 5), (205, 'Hyundai', 'Creta SX', 2025, 1350000.00, 1550000.00, 3, 0, 4)")
    crsr.execute("insert into Staff values (101, 'Suresh Kumar', 'admin123', 'Manager', '9876543210', '85000.00', 6.50), (102, 'Vikram Sharma', 'sales123', 'Sales', '9876543211', '35000.00', 2.00), (103, 'Rajesh Verma', 'sales456', 'Sales', '9876543212', '42000.00', 4.25)")
    crsr.execute("insert into Transactions values (401, 204, 301, 102, 1100000.00, 150000.00, 'Finalised', '2026-05-15', 'Q2'), (402, 203, 302, 103, 1950000.00, 250000.00, 'Quote', '2026-08-10', 'Q3'), (403, 201, 303, 102, 1850000.00, 250000.00, 'Finalised', '2026-08-20', 'Q3')")
    db.commit()
    print("Dummy values have been inserted successfully")
    
    if debug:
        crsr.execute('select * from Customers')
        recs = crsr.fetchall()
        for i in recs:
            print(i)
        print()
        crsr.execute('select * from Inventory')
        recs = crsr.fetchall()
        for i in recs:
            print(i)
        print()
        crsr.execute('select * from Staff')
        recs = crsr.fetchall()
        for i in recs:
            print(i)
        print()
        crsr.execute('select * from Transactions')
        recs = crsr.fetchall()
        for i in recs:
            print(i)
        print()


def purge():
    if Admin:
        print("WARNING: This operation will erase ALL DATA contained within the database.")
        conf = input("To confirm, type 'Yes, do as I say!': ")
        if conf == 'Yes, do as I say!':
            crsr.execute("truncate table Transactions")
            crsr.execute("truncate table Customers")
            crsr.execute("truncate table Inventory")
            crsr.execute("truncate table Staff")
            db.commit()
            print("Dummy values cleared")
            if debug:
                crsr.execute("show tables")
                recs = crsr.fetchall()
                for i in recs:
                    print(i)
            return True
        else:
            print("Deletion cancelled")
            return False
    else:
        print("This function requires elevated privileges")
        return False
            
            
def add_new(n):
    if n == 1:
        car_id = int(input("Enter Car ID: "))
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        cost_price = float(input("Enter the Cost Price: "))
        selling_price = float(input("Enter the Selling Price: "))
        available_qty = int(input("Enter the Available Quantity: "))

        crsr.execute("INSERT INTO Inventory (car_id, make, model, year, cost_price, selling_price, available_qty) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                     (car_id, make, model, year, cost_price, selling_price, available_qty))

    elif n == 2:
        emp_id = int(input("Enter the Employee ID: "))
        name = input("Enter the Name: ")
        passkey = input("Enter the Passkey: ")
        role = input("Enter the Role: ")
        phone = input("Enter the Phone: ")
        salary = float(input("Enter the Salary: "))
        experience = float(input("Enter the Experience: "))

        crsr.execute("INSERT INTO Staff (emp_id, name, passkey, role, phone, salary, experience) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                     (emp_id, name, passkey, role, phone, salary, experience))

    elif n == 3:
        cust_id = int(input("Enter the Customer ID: "))
        name = input("Enter the Name: ")
        phone = input("Enter the Phone: ")
        email = input("Enter the Email: ")
        address = input("Enter the Address: ")

        crsr.execute("INSERT INTO Customers (cust_id, name, phone, email, address) VALUES (%s,%s,%s,%s,%s)",
                     (cust_id, name, phone, email, address))

    else:
        print("Invalid Option.")
        return

    db.commit()
    print("Record Added Successfully.")


def delete(n):
    if n == 1:
        car_id = int(input("Enter Car ID to Delete: "))
        crsr.execute("DELETE FROM Inventory WHERE car_id = %s", (car_id,))

    elif n == 2:
        emp_id = int(input("Enter Employee ID to Delete: "))
        crsr.execute("DELETE FROM Staff WHERE emp_id = %s", (emp_id,))

    elif n == 3:
        cust_id = int(input("Enter Customer ID to Delete: "))
        crsr.execute("DELETE FROM Customers WHERE cust_id = %s", (cust_id,))

    elif n == 4:
        txn_id = int(input("Enter Transaction ID to Delete: "))
        crsr.execute("DELETE FROM Transactions WHERE txn_id = %s", (txn_id,))

    else:
        print("Invalid Option.")
        return

    rc = crsr.rowcount
    db.commit()

    if rc > 0:
        print("Record Deleted Successfully.")
    else:
        print("Record not Found.")


def edit(n):
    if n == 1:
        car_id = int(input("Enter the Car ID to Edit: "))
        make = input("Enter the New Make: ")
        model = input("Enter the New Model: ")
        year = int(input("Enter the New Year: "))
        cost_price = float(input("Enter the New Cost Price: "))
        selling_price = float(input("Enter the New Selling Price: "))
        available_qty = int(input("Enter the New Available Quantity: "))
        reserved_qty = int(input("Enter the New Reserved Quantity: "))
        sold_qty = int(input("Enter the New Sold Quantity: "))

        crsr.execute("UPDATE Inventory SET make=%s, model=%s, year=%s, cost_price=%s, selling_price=%s, available_qty=%s, reserved_qty=%s, sold_qty=%s WHERE car_id=%s",
                     (make, model, year, cost_price, selling_price, available_qty, reserved_qty, sold_qty, car_id))

    elif n == 2:
        emp_id = int(input("Enter the Employee ID to Edit: "))
        name = input("Enter the New Name: ")
        passkey = input("Enter The New Passkey: ")
        role = input("Enter the New Role: ")
        phone = input("Enter the New Phone Number: ")
        salary = float(input("Enter the New Salary: "))
        experience = float(input("Enter the New Experience: "))

        crsr.execute("UPDATE Staff SET name=%s, passkey=%s, role=%s, phone=%s, salary=%s, experience=%s WHERE emp_id=%s",
                     (name, passkey, role, phone, salary, experience, emp_id))

    elif n == 3:
        cust_id = int(input("Enter the Customer ID to Edit: "))
        name = input("Enter the New Name: ")
        phone = input("Enter the New Phone: ")
        email = input("Enter the New Email: ")
        address = input("Enter the New Address: ")

        crsr.execute("UPDATE Customers SET name=%s, phone=%s, email=%s, address=%s WHERE cust_id=%s",
                     (name, phone, email, address, cust_id))

    elif n == 4:
        txn_id = int(input("Enter the Transaction ID to Edit: "))
        car_id = int(input("Enter the New Car ID: "))
        cust_id = int(input("Enter the New Customer ID: "))
        emp_id = int(input("Enter the New Employee ID: "))
        sale_price = float(input("Enter the New Sale Price: "))
        net_profit = float(input("Enter the New Net Profit: "))
        status = input("Enter the New Status: ")
        txn_date = input("Enter the New Transaction Date (YYYY-MM-DD): ")
        quarter = input("Enter the New Quarter: ")

        crsr.execute("UPDATE Transactions SET car_id=%s, cust_id=%s, emp_id=%s, sale_price=%s, net_profit=%s, status=%s, txn_date=%s, quarter=%s WHERE txn_id=%s",(car_id, cust_id, emp_id, sale_price, net_profit, status, txn_date, quarter, txn_id))

    else:
        print("Invalid Option.")
        return

    rc = crsr.rowcount
    db.commit()

    if rc > 0:
        print("Record Updated Successfully.")
    else:
        print("Record not Found.")

def auth(name, psky):
    global emp, Admin
    emp = name
    crsr.execute("select role from Staff where name = %s and passkey = %s", (name, psky))
    posn = crsr.fetchone()
    if posn is not None:
        if posn[0] == 'Manager':
            print("Login Successfull (Admin Mode)")
            Admin = True
            return True
        else:
            print("Login Successfull")
            Admin = False
            return True
    else:
        print("User Not Found")
        Admin = False
        return False

def bill(txn_id):
    crsr.execute("select * from Transactions where txn_id = %s", (txn_id,))
    data = crsr.fetchone()
    if data is None:
        print("Invalid Transaction ID")
        return False
    date = data[7]
    crsr.execute("select model from Inventory where car_id = %s", (data[1],))
    carname = crsr.fetchone()
    if carname is not None:
        carname = carname[0]
    else:
        print("Car not found")
        return False
    crsr.execute("select name from Customers where cust_id = %s", (data[2],))
    cust_name = crsr.fetchone()
    if cust_name is not None:
        cust_name = cust_name[0]
    else:
        print("Customer Name not found")
        return False
    crsr.execute("select name from Staff where emp_id = %s", (data[3],))
    emp_name = crsr.fetchone()
    if emp_name is not None:
        emp_name = emp_name[0]
    else:
        print("Employee Name not found")
        return False
    print("===============  INVOICE  ===============")
    print("DATE: ", date)
    print("TRANSACTION ID: ", txn_id)
    print("CAR: ", carname)
    print("CUSTOMER: ", cust_name)
    print("EMPLOYEE: ", emp_name)
    print("PRICE: ", data[4])
    print("STATUS: ", data[6])
    print("------------------------------------------")
    return True

def txn():
    try:
        txn_id = int(input("Enter a Transaction ID: "))
    except:
        print("Invalid Input")
        return False
    crsr.execute("select txn_id from Transactions where txn_id = %s", (txn_id,))
    if crsr.fetchone() is not None:
        print("Transaction ID already in use")
        return False
    crsr.execute("select * from Customers")
    recs = crsr.fetchall()
    for i in recs:
        print(i)
    try:
        cust_id = int(input("Enter the Customer ID: "))
    except:
        print("Invalid Input")
        return False
    crsr.execute("select cust_id from Customers where cust_id = %s", (cust_id,))
    if crsr.fetchone() is None:
        print("Invalid Customer ID")
        return False
    crsr.execute("select * from Inventory")
    recs = crsr.fetchall()
    for i in recs:
        print(i)
    try:
        car_id = int(input("Enter the Car ID: "))
    except:
        print("Invalid Input")
        return False
    crsr.execute("select emp_id from Staff where name = %s", (emp,))
    emp_id = crsr.fetchone()
    if emp_id is None:
        print("Invalid Emloyee ID")
        return False
    emp_id = emp_id[0]
    try:
        sp = float(input("Enter the Sale Price: "))
    except:
        print("Invalid Input")
        return False
    crsr.execute("select cost_price, available_qty from Inventory where car_id = %s", (car_id,))
    cp = crsr.fetchone()
    if cp is None:
        print("Invalid Car ID")
        return False
    if cp[1] < 1:
        print("The Entered Product is Out of Stock")
        return False
    cp = cp[0]
    netprof = sp - cp
    print("The net profit from this transaction will be", netprof)
    status = input("Enter the Status (Quote/Finalised): ").strip().title()
    if status not in ('Quote', 'Finalised'):
        print("Invalid Status")
        return False
    txn_date = input("Enter the transaction date (YYYY-MM-DD): ")
    split = txn_date.split('-')
    if len(split) != 3:
        print("Invalid Date Format Used")
        return False
    if not (split[0].isdigit() and split[1].isdigit() and split[2].isdigit()):
        print("Invalid Date Format Used")
        return False
    if split[1] in ('01', '02', '03'):
        q = "Q1"
    elif split[1] in ('04', '05', '06'):
        q = "Q2"
    elif split[1] in ('07', '08', '09'):
        q = "Q3"
    elif split[1] in ('10', '11', '12'):
        q = "Q4"
    else:
        print("Invalid Month Value")
        return False
    try:
        crsr.execute("insert into Transactions values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (txn_id, car_id, cust_id, emp_id, sp, netprof, status, txn_date, q))
        if status == 'Finalised':
            crsr.execute("update Inventory set available_qty = available_qty - 1, sold_qty = sold_qty + 1 where car_id = %s", (car_id,))
        elif status == 'Quote':
            crsr.execute("update Inventory set available_qty = available_qty - 1, reserved_qty = reserved_qty + 1 where car_id = %s", (car_id,))
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        print("Database Error -", err)
        return False
    prnt = input("Print bill? (y/n): ")
    if prnt.lower() == "y":
        status = bill(txn_id)
        if status == False:
            print("Unable to Print Bill")
    return True

def finalise(txn_id):
    crsr.execute("select * from Transactions where txn_id = %s", (txn_id,))
    txn = crsr.fetchone()
    if txn is None:
        print("Invalid Transaction ID")
        return False
    if txn[6] == "Finalised":
        print("This transaction is already finalised")
        return False
    car_id = txn[1]
    try:
        crsr.execute("update Transactions set status = 'Finalised' where txn_id = %s", (txn_id,))
        crsr.execute("update Inventory set sold_qty = sold_qty + 1, reserved_qty = reserved_qty - 1 where car_id = %s", (car_id,))
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        print("Updation failed:", err)
        return False
    inv = input("Do you want to print the bill? (y/n): ").lower()
    if inv == 'y':
        status = bill(txn_id)
        if status == False:
            print("Bill Printing Failed")
    return True

def disp(n):
    if n == 1:
        crsr.execute("select * from Customers")
        print(('Customer ID', 'Name', 'Phone', 'Email', 'Address'))
        for i in crsr.fetchall():
            print(i)
    elif n == 2:
        crsr.execute("select * from Inventory")
        print(('Car ID', 'Make', 'Model', 'Year', 'Cost Price', 'Selling Price', 'Available', 'Reserved', 'Sold'))
        for i in crsr.fetchall():
            print(i)
    elif n == 3:
        if Admin:
            crsr.execute("select * from Staff")
            print(('Employee ID', 'Name', 'Passkey', 'Role', 'Phone', 'Salary', 'Experience'))
            for i in crsr.fetchall():
                print(i)
        else:
            print("Access Denied: Table requires Elevated Privileges to View")
            return False
    elif n == 4:
        crsr.execute("select * from Transactions")
        print(('Txn ID', 'Car ID', 'Cust ID', 'Emp ID', 'Sale Price', 'Net Profit', 'Status', 'Date', 'Quarter'))
        for i in crsr.fetchall():
            print(i)
    else:
        print("Invalid Option")
        return False
    return True

def q_report():
    if Admin:
        crsr.execute("select quarter, count(txn_id), sum(sale_price), sum(net_profit), avg(net_profit) from Transactions where status = 'Finalised' group by quarter order by quarter")
        data = crsr.fetchall()
        if data == []:
            print("No data to show")
            return False
        print(('Quarter', 'Transactions', 'Total Sale Price', 'Total Profit', 'Average Profit'))
        tsales, tprofit = 0, 0
        for i in data:
            print(i)
            tsales += i[2]
            tprofit += i[3]
        print(('TOTAL', '       ', tsales, tprofit, '             '))
        return True
    else:
        print("This function requires elevated privileges.")
        return False

def emp_stats():
    if Admin:
        crsr.execute("select Staff.emp_id, Staff.name, Staff.experience, count(Transactions.txn_id), sum(Transactions.net_profit) from Staff, Transactions where Staff.emp_id = Transactions.emp_id and Transactions.status = 'Finalised' group by Staff.name, Staff.experience, Staff.emp_id order by count(Transactions.txn_id) desc")
        data = crsr.fetchall()
        if data == []:
            print("No Data Available")
            return False
        print("==================STAFF SALES REPORT==================")
        print(('ID', 'Name', 'Experience', 'Sold', 'Total Profits'))
        for i in data:
            print(i)
        return True
    else:
        print("This function requires elevated privileges.")
        return False