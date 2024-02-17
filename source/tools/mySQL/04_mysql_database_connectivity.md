# MySQL database connectivity
## MySQL database connectivity using python


## Install mysql.connector
To use python mysql.connector, first install the library using pip

```
pip install mysql-connector-python
```

## Example

Run the following code to insure that mysql.connector is able to communicate with MySQL database

```
import mysql.connector
# Connect to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@n1e6i#"
)

print(mydb.connection_id)

```