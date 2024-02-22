# 2023-01-21: mySQL and Python
## mySQL and Python

To install MySQL on Windows and write Python code in Visual Studio Code (VSCode) with MySQL integration, follow these steps:

### 1. Install MySQL

#### a. MySQL Installer:

1. Visit the [MySQL Downloads](https://dev.mysql.com/downloads/installer/) page.
2. Download the MySQL Installer for Windows.
3. Run the installer and follow the on-screen instructions.
4. During installation, select "MySQL Server" and "MySQL Workbench" components.

#### b. MySQL Server Configuration:

1. During installation, you'll be prompted to configure the MySQL Server.
2. Set a root password and remember it.
3. Configure other settings as needed.

#### c. MySQL Workbench:

1. After installing, open MySQL Workbench.
2. Connect to the MySQL Server using the root password.

### 2. Install Python and MySQL Connector

#### a. Install Python:

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. During installation, make sure to check the option to add Python to the system PATH.

#### b. Install MySQL Connector:

Open a command prompt or PowerShell and run:

```bash
pip install mysql-connector-python
```

### 3. Set Up Visual Studio Code

#### a. Install VSCode:

Download and install Visual Studio Code from [here](https://code.visualstudio.com/).

#### b. Install Python Extension:

1. Open VSCode.
2. Go to Extensions (Ctrl+Shift+X).
3. Search for "Python" and install the official Python extension.

### 4. Write Python Code in VSCode

#### a. Create a Python File:

1. Open VSCode.
2. Create a new Python file with a `.py` extension.

#### b. Write Python Code with MySQL Connector:

```python
import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

# Create a cursor
cursor = conn.cursor()

# Example Query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
```

Replace `"your_password"`, `"your_database"`, and `"your_table"` with your MySQL password, database name, and table name.

#### c. Run the Python Code:

1. Save the Python file.
2. Open a terminal in VSCode.
3. Run the script using `python your_file.py`.

This script connects to your MySQL database, executes a query, and prints the results.

Remember to adapt the code according to your specific database and table names.