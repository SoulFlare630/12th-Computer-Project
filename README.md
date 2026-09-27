# Car Showroom Database

A menu-driven Python and MySQL project for managing showroom customers, inventory, staff, quotes, sales, invoices, and basic reports.

## Requirements

- Python 3
- MySQL Server running on the same computer
- A MySQL account allowed to create and use databases
- MySQL Connector/Python

Install the connector:

```bash
python -m pip install mysql-connector-python
```

## Run

1. Start MySQL Server.
2. Open a terminal in the project folder and run:

   ```bash
   python "Car Showroom.py"
   ```

3. Enter your MySQL username and password. The program connects to `localhost`, creates the `carshowroom` database if needed, and creates any missing tables.
4. Choose whether to insert the optional sample data.
5. Log in with a staff name and passkey. If no Manager exists, the program asks you to create one before login.

## Program Entry and Cleanup

The interactive workflow runs through `main()` when the script is launched directly. Importing the Python file does not start the prompts or connect to MySQL. When `main()` exits, the program closes the database cursor and connection, including when an error interrupts the workflow.

If sample data was inserted into an empty database, the sample Manager login is:

- Name: `Mathew Thomas`
- Passkey: `admin123`

These credentials are included in the source for demonstration only. Do not use them for real accounts.

## Menus and Features

- **Customer Details:** Add, display, update, or delete customer records.
- **Inventory Management:** Add, display, update, or delete cars. Inventory tracks available, reserved, and sold quantities.
- **Transactions:** Create a quote or finalized sale, finalize a quote, cancel a quote, display transactions, and print or reprint an invoice. The all-transactions view includes car, customer, and employee names.
- **Staff Details:** Managers can add, display, update, and delete staff records.
- **Statistics:** Managers can view stock and customer/staff totals, quarterly sales and profit, staff sales performance, and a customer's transaction history.
- **Administrator Menu:** Managers can insert sample data, create missing tables, or clear table data.

The table views print aligned columns. Staff passkeys are not included in the staff listing.

## Transaction and Inventory Rules

- A transaction requires an existing customer and an existing car with available stock.
- Creating a quote moves one unit from available stock to reserved stock.
- Creating a finalized transaction moves one unit from available stock to sold stock.
- Finalizing a quote moves one unit from reserved stock to sold stock.
- Canceling a quote deletes the quote and returns its reserved unit to available stock.
- The displayed profit is calculated as sale price minus the car's cost price; it does not include other expenses.

## Database Tables

The `carshowroom` database contains:

- **Customers:** `cust_id`, name, phone, email, address
- **Inventory:** `car_id`, make, model, year, cost price, selling price, available quantity, reserved quantity, sold quantity
- **Staff:** `emp_id`, name, passkey, role, phone, salary, experience
- **Transactions:** `txn_id`, car/customer/employee IDs, sale price, calculated profit, status, transaction date, quarter

The IDs in `Transactions` are not declared as foreign keys. Deleting related customer, car, or staff records can therefore leave transaction history without matching details. The transaction list displays fallback labels for missing related records; invoice printing requires those related records to exist.

## Manual Test Checklist

- Start with an empty database and verify that the tables are created and a Manager can be added.
- Insert sample data once, log in as the sample Manager, and view each table.
- Try invalid IDs, blank required fields, invalid staff roles, and negative inventory quantities when adding records.
- Create a quote for an in-stock car, verify available/reserved quantities, then finalize or cancel it and verify the quantities again.
- Try creating a transaction for an out-of-stock car and confirm no transaction is recorded.
- Print an invoice and view the quarterly and staff reports with finalized transactions.

## Limitations and Safety

- Staff passkeys are stored as plain text, and the login prompt uses ordinary console input. Use only test credentials and synthetic data; this is not production authentication.
- Database connections are fixed to `localhost`; host and port are not configurable in the menu.
- Sample records use fixed IDs. Inserting them again can fail when those IDs already exist.
- The **WIPE ALL DATA** option truncates every table. It is destructive and should only be used with test data.
- The table-setup option creates missing tables; it does not migrate or repair the structure of existing tables.
