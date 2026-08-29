'''==========CAR SHOWROOM DATABASE==========
Made by:
Joel Ephrem Cebin
Adhinath V. K.
Alan Anil'''
debug = False
import mysql.connector

def dbconnect(passwd):
    global db, crsr
    db = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)
    crsr = db.cursor()
    
def setup():
    crsr.execute("create database if not exists carshowroom")
    crsr.execute("use carshowroom")
    crsr.execute("create table if not exists Customers (cust_id int primary key, name varchar(100) not null, phone varchar(15) not null, email varchar(100), address varchar(255))")
    crsr.execute("create table if not exists Inventory (car_id int primary key, make varchar(50) not null, model varchar(50) not null, year int not null, cost_price decimal(15, 2) not null, selling_price decimal(15, 2) not null, available_qty int default 0, reserved_qty int default 0, sold_qty int default 0)")
    crsr.execute("create table if not exists Staff (emp_id int primary key, name varchar(100) not null, passkey varchar(50), role varchar(20) not null, phone varchar(15) unique not null, salary decimal(10,2) not null, experience decimal(4, 2) not null)")
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


def purge_dummies():
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
            
            
def add_new(n):
    if n == 1:
        car_id = int(input("Enter car ID: "))
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = int(input("Enter year: "))
        cost_price = float(input("Enter cost price: "))
        selling_price = float(input("Enter selling price: "))
        available_qty = int(input("Enter available quantity: "))

        crsr.execute("INSERT INTO Inventory (car_id, make, model, year, cost_price, selling_price, available_qty) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                     (car_id, make, model, year, cost_price, selling_price, available_qty))

    elif n == 2:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter name: ")
        passkey = input("Enter passkey: ")
        role = input("Enter role: ")
        phone = input("Enter phone: ")
        salary = float(input("Enter salary: "))
        experience = float(input("Enter experience: "))

        crsr.execute("INSERT INTO Staff (emp_id, name, passkey, role, phone, salary, experience) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                     (emp_id, name, passkey, role, phone, salary, experience))

    elif n == 3:
        cust_id = int(input("Enter customer ID: "))
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        crsr.execute("INSERT INTO Customers (cust_id, name, phone, email, address) VALUES (%s,%s,%s,%s,%s)",
                     (cust_id, name, phone, email, address))

    else:
        print("Invalid option.")
        return

    db.commit()
    print("Record added successfully.")


def delete(n):
    if n == 1:
        car_id = int(input("Enter car ID to delete: "))
        crsr.execute("DELETE FROM Inventory WHERE car_id = %s", (car_id,))

    elif n == 2:
        emp_id = int(input("Enter employee ID to delete: "))
        crsr.execute("DELETE FROM Staff WHERE emp_id = %s", (emp_id,))

    elif n == 3:
        cust_id = int(input("Enter customer ID to delete: "))
        crsr.execute("DELETE FROM Customers WHERE cust_id = %s", (cust_id,))

    elif n == 4:
        txn_id = int(input("Enter transaction ID to delete: "))
        crsr.execute("DELETE FROM Transactions WHERE txn_id = %s", (txn_id,))

    else:
        print("Invalid option.")
        return

    db.commit()

    if crsr.rowcount > 0:
        print("Record deleted successfully.")
    else:
        print("Record not found.")


def edit(n):
    if n == 1:
        car_id = int(input("Enter car ID to edit: "))
        make = input("Enter new make: ")
        model = input("Enter new model: ")
        year = int(input("Enter new year: "))
        cost_price = float(input("Enter new cost price: "))
        selling_price = float(input("Enter new selling price: "))
        available_qty = int(input("Enter new available quantity: "))
        reserved_qty = int(input("Enter new reserved quantity: "))
        sold_qty = int(input("Enter new sold quantity: "))

        crsr.execute("UPDATE Inventory SET make=%s, model=%s, year=%s, cost_price=%s, selling_price=%s, available_qty=%s, reserved_qty=%s, sold_qty=%s WHERE car_id=%s",
                     (make, model, year, cost_price, selling_price, available_qty, reserved_qty, sold_qty, car_id))

    elif n == 2:
        emp_id = int(input("Enter employee ID to edit: "))
        name = input("Enter new name: ")
        passkey = input("Enter new passkey: ")
        role = input("Enter new role: ")
        phone = input("Enter new phone: ")
        salary = float(input("Enter new salary: "))
        experience = float(input("Enter new experience: "))

        crsr.execute("UPDATE Staff SET name=%s, passkey=%s, role=%s, phone=%s, salary=%s, experience=%s WHERE emp_id=%s",
                     (name, passkey, role, phone, salary, experience, emp_id))

    elif n == 3:
        cust_id = int(input("Enter customer ID to edit: "))
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        crsr.execute("UPDATE Customers SET name=%s, phone=%s, email=%s, address=%s WHERE cust_id=%s",
                     (name, phone, email, address, cust_id))

    elif n == 4:
        txn_id = int(input("Enter transaction ID to edit: "))
        car_id = int(input("Enter new car ID: "))
        cust_id = int(input("Enter new customer ID: "))
        emp_id = int(input("Enter new employee ID: "))
        sale_price = float(input("Enter new sale price: "))
        net_profit = float(input("Enter new net profit: "))
        status = input("Enter new status: ")
        txn_date = input("Enter new transaction date (YYYY-MM-DD): ")
        quarter = input("Enter new quarter: ")

        crsr.execute("UPDATE Transactions SET car_id=%s, cust_id=%s, emp_id=%s, sale_price=%s, net_profit=%s, status=%s, txn_date=%s, quarter=%s WHERE txn_id=%s",(car_id, cust_id, emp_id, sale_price, net_profit, status, txn_date, quarter, txn_id))

    else:
        print("Invalid option.")
        return

    db.commit()

    if crsr.rowcount > 0:
        print("Record updated successfully.")
    else:
        print("Record not found.")
