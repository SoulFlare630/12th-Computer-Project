'''==========CAR SHOWROOM DATABASE==========
Made by:
Joel Ephrem Cebin
Adhinath V. K.
Alan Anil'''
debug = False
import mysql.connector

def dbconnect(usr, passwd):
    global db, crsr
    try:
        db = mysql.connector.connect(host = 'localhost', user = usr, password = passwd)
    except mysql.connector.Error:
        return False
    crsr = db.cursor()
    return True
    
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
        data = crsr.fetchall()
        for i in data:
            print(i)
        crsr.execute('desc Inventory')
        data = crsr.fetchall()
        for i in data:
            print(i)
        crsr.execute('desc Staff')
        data = crsr.fetchall()
        for i in data:
            print(i)
        crsr.execute('desc Transactions')
        data = crsr.fetchall()
        for i in data:
            print(i)


def dummies():
    crsr.execute("insert into Customers values (301, 'Naveen Nair', '9847123456', 'naveen.nair@gmail.com', 'Panampilly Nagar, Kochi'), (302, 'Fathima Rafeeq', '9447234567', 'fathima.r@yahoo.com', 'Manacaud, Thiruvananthapuram'), (303, 'Rony Mathew', '9744345678', 'rony.mathew@outlook.com', 'Kanjikuzhy, Kottayam'), (304, 'Aisha Sulaiman', '9895456789', 'aisha.sulaiman@gmail.com', 'Palayam, Kozhikode'), (305, 'Harikrishnan V.', '9496567890', 'hari.krishnan@gmail.com', 'Chembukkav, Thrissur')")
    crsr.execute("insert into Inventory values (201, 'Toyota', 'Innova Hycross ZX', 2025, 2400000.00, 2750000.00, 3, 1, 2), (202, 'Hyundai', 'Creta SX(O)', 2025, 1500000.00, 1720000.00, 4, 0, 3), (203, 'Mahindra', 'Thar Roxx AX7L', 2026, 1850000.00, 2100000.00, 0, 1, 4), (204, 'Maruti Suzuki', 'Swift ZXi+', 2025, 750000.00, 880000.00, 5, 0, 4), (205, 'Tata', 'Nexon EV Empowered', 2026, 1450000.00, 1680000.00, 2, 0, 1)")
    crsr.execute("insert into Staff values (101, 'Mathew Thomas', 'admin123', 'Manager', '9846011223', 85000.00, 7.50), (102, 'Mohammed Asif', 'sales123', 'Sales', '9745122334', 38000.00, 3.00), (103, 'Sreekanth Pillai', 'sales456', 'Sales', '9633233445', 42000.00, 4.50), (104, 'Anju Varghese', 'sales789', 'Sales', '9447344556', 32000.00, 1.50)")
    crsr.execute("insert into Transactions values (401, 201, 301, 102, 2750000.00, 350000.00, 'Finalised', '2026-01-18', 'Q1'), (402, 204, 302, 102, 880000.00, 130000.00, 'Finalised', '2026-04-12', 'Q2'), (403, 202, 301, 103, 1720000.00, 220000.00, 'Finalised', '2026-07-25', 'Q3'), (404, 205, 304, 102, 1680000.00, 230000.00, 'Finalised', '2026-10-05', 'Q4'), (405, 203, 303, 103, 2100000.00, 250000.00, 'Quote', '2026-11-14', 'Q4'), (406, 201, 301, 104, 2750000.00, 350000.00, 'Quote', '2026-12-02', 'Q4')")
    db.commit()
    print("Dummy values have been inserted successfully")
    print("Dummy Admin Name: Mathew Thomas")
    print("Dummy Admin Password: admin123")
    
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
            print("Table Values Cleared")
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
    '''
    1 - New Car
    2 - New Employee
    3 - New Customer
    '''
    try:
        if n == 1:
            car_id = int(input("Enter Car ID: "))
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = int(input("Enter Year: "))
            cost_price = float(input("Enter the Cost Price: "))
            selling_price = float(input("Enter the Selling Price: "))
            available_qty = int(input("Enter the Available Quantity: "))
            crsr.execute("INSERT INTO Inventory (car_id, make, model, year, cost_price, selling_price, available_qty) VALUES (%s,%s,%s,%s,%s,%s,%s)", (car_id, make, model, year, cost_price, selling_price, available_qty))
            db.commit()
            print("Car added successfully.")
            return True
            
        elif n == 2:
            emp_id = int(input("Enter the Employee ID: "))
            name = input("Enter the Name: ")
            passkey = input("Enter the Passkey: ")
            role = input("Enter the Role: ")
            phone = input("Enter the Phone: ")
            salary = float(input("Enter the Salary: "))
            experience = float(input("Enter the Experience: "))
            crsr.execute("INSERT INTO Staff (emp_id, name, passkey, role, phone, salary, experience) VALUES (%s,%s,%s,%s,%s,%s,%s)", (emp_id, name, passkey, role, phone, salary, experience))
            db.commit()
            print("Employee added successfully.")
            return True
            
        elif n == 3:
            cust_id = int(input("Enter the Customer ID: "))
            name = input("Enter the Name: ")
            phone = input("Enter the Phone: ")
            email = input("Enter the Email: ")
            address = input("Enter the Address: ")
            crsr.execute("INSERT INTO Customers (cust_id, name, phone, email, address) VALUES (%s,%s,%s,%s,%s)", (cust_id, name, phone, email, address))
            db.commit()
            print("Customer added successfully.")
            return True
            
        else:
            print("Failed: Invalid Option Selected.")
            return False

    except ValueError:
        print("Failed: Invalid input! Please enter the correct data type (e.g., numbers for IDs).")
        return False
    except Exception as e:
        db.rollback() 
        print("Failed to add record due to a database error:", e)
        return False


def edit_record(n):
    '''
    1 - Inventory
    2 - Staff
    3 - Customers
    '''
    try:
        if n == 1:
            record_id = int(input("Enter Car ID to edit: "))
            col = input("Enter column to update (make, model, year, cost_price, selling_price, available_qty): ")
            val = input("Enter new value for " + col + ": ")
            crsr.execute("UPDATE Inventory SET " + col + " = %s WHERE car_id = %s", (val, record_id))
            if crsr.rowcount == 0:
                print("Failed: Car ID not found or no changes were made.")
                return False
            db.commit()
            print("Car record updated successfully.")
            return True
            
        elif n == 2:
            record_id = int(input("Enter Employee ID to edit: "))
            col = input("Enter column to update (name, passkey, role, phone, salary, experience): ")
            val = input("Enter new value for " + col + ": ")
            crsr.execute("UPDATE Staff SET " + col + " = %s WHERE emp_id = %s", (val, record_id))
            if crsr.rowcount == 0:
                print("Failed: Employee ID not found or no changes were made.")
                return False
            db.commit()
            print("Employee record updated successfully.")
            return True
            
        elif n == 3:
            record_id = int(input("Enter Customer ID to edit: "))
            col = input("Enter column to update (name, phone, email, address): ")
            val = input("Enter new value for " + col + ": ")
            crsr.execute("UPDATE Customers SET " + col + " = %s WHERE cust_id = %s", (val, record_id))
            if crsr.rowcount == 0:
                print("Failed: Customer ID not found or no changes were made.")
                return False
            db.commit()
            print("Customer record updated successfully.")
            return True
            
        else:
            print("Failed: Invalid Option Selected.")
            return False

    except ValueError:
        print("Failed: Invalid input! Please enter a valid numeric ID.")
        return False
    except Exception as e:
        db.rollback()
        print("Failed to update record due to a database error:", e)
        return False


def delete_record(n):
    '''
    1 - Inventory
    2 - Staff
    3 - Customers
    4 - Quotes (To be Added)
    '''
    try:
        if n == 1:
            record_id = int(input("Enter Car ID to delete: "))
            crsr.execute("DELETE FROM Inventory WHERE car_id = %s", (record_id,))
            if crsr.rowcount == 0:
                print("Failed: Car ID not found.")
                return False
            db.commit()
            print("Car deleted successfully.")
            return True

        elif n == 2:
            record_id = int(input("Enter Employee ID to delete: "))
            crsr.execute("DELETE FROM Staff WHERE emp_id = %s", (record_id,))
            if crsr.rowcount == 0:
                print("Failed: Employee ID not found.")
                return False
            db.commit()
            print("Employee deleted successfully.")
            return True

        elif n == 3:
            record_id = int(input("Enter Customer ID to delete: "))
            crsr.execute("DELETE FROM Customers WHERE cust_id = %s", (record_id,))
            if crsr.rowcount == 0:
                print("Failed: Customer ID not found.")
                return False
            db.commit()
            print("Customer deleted successfully.")
            return True

        elif n == 4:
            record_id = int(input("Enter the Quote ID to delete: "))
            crsr.execute("select txn_id, car_id from Transactions where status = 'Quote' and txn_id = %s", (record_id,))
            tup = crsr.fetchone()
            if tup is None:
                print("No Quotes Found")
                return False
            txn_id = tup[0]
            car_id = tup[1]
            crsr.execute("delete from Transactions where txn_id = %s", (record_id,))
            crsr.execute("update Inventory set available_qty = available_qty + 1, reserved_qty = reserved_qty - 1 where car_id = %s", (car_id,))
            db.commit()
            print("Quote Deleted Successfully")
            return True

        else:
            print("Failed: Invalid Option Selected.")
            return False

    except ValueError:
        print("Failed: Invalid input! Please enter a valid numeric ID.")
        return False
    except Exception as e:
        db.rollback()
        print("Failed to delete record due to a database error:", e)
        return False           


def auth(name, psky):
    global emp, Admin
    emp = name.strip()
    crsr.execute("select role from Staff where name = %s and passkey = %s", (name, psky.strip()))
    posn = crsr.fetchone()
    if posn is not None:
        if posn[0] == 'Manager':
            print("Login Successful (Admin Mode)")
            Admin = True
            return True
        else:
            print("Login Successful")
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
    print("Transaction Finalised Successfully")
    inv = input("Do you want to print the bill? (y/n): ").lower()
    if inv == 'y':
        status = bill(txn_id)
        if status == False:
            print("Bill Printing Failed")
    return True

def disp(n):
    '''
    1 - Customers
    2 - Inventory
    3 - Staff
    4 - Transactions
    '''
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

def cust_history():
    try:
        cust_id = int(input("Enter the Customer ID: "))
    except ValueError:
        print("Invalid Input")
        return False

    crsr.execute("select name from Customers where cust_id = %s", (cust_id,))
    cust_name = crsr.fetchone()
    
    if cust_name is None:
        print("Invalid Customer ID")
        return False

    print("\n========== PURCHASE HISTORY ==========")
    print("CUSTOMER: ", cust_name[0])
    print("--------------------------------------")

    crsr.execute("select Transactions.txn_id, Transactions.txn_date, Inventory.make, Inventory.model, Transactions.sale_price, Transactions.status from Transactions, Inventory where Transactions.car_id = Inventory.car_id and Transactions.cust_id = %s order by Transactions.txn_date desc", (cust_id,))
    recs = crsr.fetchall()

    if recs == []:
        print("No purchase history found for this customer.")
    else:
        print(('Txn ID', 'Date', 'Make', 'Model', 'Price', 'Status'))
        for i in recs:
            print(i)
            
    print("======================================\n")
    return True

def show_statistics():
    try:
        print("\n========== SHOWROOM STATISTICS ==========")
        
        crsr.execute("SELECT SUM(available_qty) FROM Inventory")
        total_cars = crsr.fetchone()[0]
        if total_cars == None:
            total_cars = 0
        print("Total Cars in Stock:", total_cars)
        
        crsr.execute("SELECT SUM(cost_price * available_qty) FROM Inventory")
        inventory_value = crsr.fetchone()[0]
        if inventory_value == None:
            inventory_value = 0
        print("Total Inventory Value (Cost): $", inventory_value)
        
        crsr.execute("SELECT COUNT(cust_id) FROM Customers")
        total_customers = crsr.fetchone()[0]
        if total_customers == None:
            total_customers = 0
        print("Total Registered Customers:", total_customers)
        
        crsr.execute("SELECT COUNT(emp_id) FROM Staff")
        total_staff = crsr.fetchone()[0]
        if total_staff == None:
            total_staff = 0
        print("Total Staff Members:", total_staff)
        
        print("=========================================\n")
        return True
        
    except Exception as e:
        print("Failed to retrieve statistics due to a database error:", e)
        return False
        
#MAIN PROGRAM

while True:
    if dbconnect(input("Enter your MySQL Username: "), input("Enter you MySQL Password: ")):
        print("Database Connection Successful")
        break
    else:
        print("Database Connection Failed")

setup()
opt = input("Do you want to add dummy values into the database for testing? (y/n): ")
if opt.lower() == 'y':
    dummies()
else:
    print("Dummy values can be added later if you change your mind.")
    
crsr.execute("select count(*) from Staff where Role = 'Manager'")
data = crsr.fetchone()
if data[0] == 0:
    while True:
        print("No Manager Data is Available in the Database.")
        print("Please add a Manager account to continue")
        if add_new(2):
            crsr.execute("select count(*) from Staff where Role = 'Manager'")
            data = crsr.fetchone()
            if data[0] != 0:
                break

while True:
    if auth(input("Enter your Name: "), input("Enter your Passkey: ")):
        break

while True:
    print("==========CAR SHOWROOM DATABASE==========")
    print("|        PLEASE SELECT AN OPTION        |")
    print("|        [1] Customer Details           |")
    print("|        [2] Inventory Management       |")
    print("|        [3] Transactions               |")
    print("|        [4] Exit                       |")
    if Admin:
        print("|        [5] Staff Details              |")
        print("|        [6] Statistics                 |")
        print("|        [7] Administrator Menu         |")
    print("+---------------------------------------+")
    opt = input("       Enter an option: ").strip()

    if opt == '1':
        while True:
            print("[1] Add New Customer")
            print("[2] View All Customers")
            print("[3] Update Customer Details")
            print("[4] Delete Customer Details")
            print("[5] Back")
            sub_opt = input('Select an Option: ').strip()
            if sub_opt == '1':
                add_new(3)
            elif sub_opt == '2':
                disp(1)
            elif sub_opt == '3':
                edit_record(3)
            elif sub_opt == '4':
                delete_record(3)
            elif sub_opt == '5':
                break
            else:
                print("Invalid Option")

    elif opt == '2':
        while True:
            print("[1] Add a New Car")
            print("[2] View Inventory")
            print("[3] Update Car Details")
            print("[4] Delete a Car")
            print("[5] Back")
            sub_opt = input('Select an Option: ').strip()
            if sub_opt == '1':
                add_new(1)
            elif sub_opt == '2':
                disp(2)
            elif sub_opt == '3':
                edit_record(1)
            elif sub_opt == '4':
                delete_record(1)
            elif sub_opt == '5':
                break
            else:
                print("Invalid Option")

    elif opt == '3':
        while True:
            print("[1] Create a New Quote/Transaction")
            print("[2] Finalise a Quote")
            print("[3] Cancel a Reservation")
            print("[4] View/Reprint an Invoice")
            print("[5] Show All Transactions")
            print("[6] Back")
            sub_opt = input("Enter your choice: ")
            if sub_opt == '1':
                txn()
            elif sub_opt == '2':
                try:
                    finalise(int(input("Enter the Transaction ID: ")))
                except ValueError:
                    print("ERROR: Transaction ID must be Numerical")
            elif sub_opt == '3':
                delete_record(4)
            elif sub_opt == '4':
                try:
                    bill(int(input("Enter the Transaction ID: ")))
                except ValueError:
                    print("ERROR: Transaction ID must be Numerical")
            elif sub_opt == '5':
                disp(4)
            elif sub_opt == '6':
                break
            else:
                print("Invalid Option")

    elif opt == '4':
        break

    elif opt == '5':
        if Admin:
            while True:
                print("[1] New Staff")
                print("[2] View all Staff")
                print("[3] Update Staff Details")
                print("[4] Delete a Staff Member")
                print("[5] Back")
                sub_opt = input("Enter your Choice: ")
                if sub_opt == '1':
                    add_new(2)
                elif sub_opt == '2':
                    disp(3)
                elif sub_opt == '3':
                    edit_record(2)
                elif sub_opt == '4':
                    delete_record(2)
                elif sub_opt == '5':
                    break
                else:
                    print("Invalid Option")
        else:
            print("ERROR: Not Enough Permissions")

    elif opt == '6':
        if Admin:
            while True:
                print("[1] Showroom Overview")
                print("[2] Quarterly Report")
                print("[3] Staff Performance")
                print("[4] Customer History")
                print("[5] Back")
                sub_opt = input("Enter your Choice: ")
                if sub_opt == '1':
                    show_statistics()
                elif sub_opt == '2':
                    q_report()
                elif sub_opt == '3':
                    emp_stats()
                elif sub_opt == '4':
                    cust_history()
                elif sub_opt == '5':
                    break
                else:
                    print("Invalid Option")
        else:
            print("ERROR: Not Enough Permissions")
            
    elif opt == '7':
        if Admin:
            while True:
                print("[1] WIPE ALL DATA")
                print("[2] Insert Dummy Values")
                print("[3] Repair Tables")
                print("[4] Back")
                sub_opt = input("Enter your Choice: ")
                if sub_opt == '1':
                    purge()
                elif sub_opt == '2':
                    dummies()
                elif sub_opt == '3':
                    setup()
                elif sub_opt == '4':
                    break
                else:
                    print("Invalid Option")
        else:
            print("ERROR: Not Enough Permissions")
    else:
        print("Invalid Option")