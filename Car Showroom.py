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