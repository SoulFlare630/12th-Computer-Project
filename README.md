# Car Showroom Database

A menu-driven Python and MySQL application for managing a car showroom. It tracks customers, inventory, staff, quotes, completed sales, invoices, and showroom reports.

## Requirements

- Python 3
- MySQL Server running on the same computer (`localhost`)
- A MySQL account with permission to create and use a database
- The MySQL Connector/Python package

Install the connector with:

```bash
python -m pip install mysql-connector-python
```

## Setup and Run

1. Start the MySQL Server.
2. Open a terminal in the project folder.
3. Run the program:

   ```bash
   python "Car Showroom.py"
   ```

4. Enter your MySQL username and password when prompted. The program connects to `localhost`, creates the `carshowroom` database if needed, and creates its tables.
5. Choose whether to insert the optional sample records.
6. Log in with an existing staff name and passkey. If the database has no Manager account, the program prompts you to create one first.

### Sample login

If you insert the supplied sample data into an empty database, the sample Manager login is:

- Name: `Mathew Thomas`
- Passkey: `admin123`

These credentials are publicly visible in the source code and must not be used for real accounts.

## Features

- **Customers:** Add, view, update, and delete customer records.
- **Inventory:** Add, view, update, and delete cars; track available, reserved, and sold quantities.
- **Transactions:** Create quotes or finalised transactions, reserve or sell inventory, finalise quotes, cancel quotes, and print or reprint invoices.
- **Staff:** Managers can add, view, update, and delete staff records.
- **Statistics and reports:** Managers can view showroom totals, quarterly sales and profit, staff performance, and a customer's transaction history.
- **Administrator tools:** Managers can add sample data, recreate missing tables, or clear table data.

## Database Tables

The application creates these tables in the `carshowroom` database:

- `Customers`
- `Inventory`
- `Staff`
- `Transactions`

## Important Notes

- Staff passkeys are stored as plain text in the database. This program is intended for a local school project, not for production or use with real customer data.
- The administrator's **WIPE ALL DATA** option truncates every table. Use it carefully.
- The sample-data option uses fixed record IDs, so inserting the same sample records again can fail if those IDs already exist.
- Database connection settings are fixed to `localhost`; the program does not currently ask for a server address or port.
