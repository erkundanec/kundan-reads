---
title: My First MySQL Guide
description: My first MySQL database interection using python
sidebar_position: 5
---

## Here's the tutorial with brief explanations for different mysql operations

### 1. Setup Connection and Database:

```python
import mysql.connector

# Connect to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

# Create a database
cur = mydb.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS db1")

# Switch to the created database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="db1"
)
```

**Explanation:** This section establishes a connection to the MySQL server, creates a database named 'db1' if it doesn't exist, and then switches to that database for subsequent operations.

### 2. INSERT Data into the 'book' Table:

#### Single Record Insert:

```python
cur = mydb.cursor()
s = "INSERT INTO book (bookid, title, price) VALUES (%s, %s, %s)"
b1 = (1, 'Python3', 345)
cur.execute(s, b1)
mydb.commit()
```

**Explanation:** This code inserts a single record into the 'book' table, representing a book with ID 1, title 'Python3', and price 345.

#### Multiple Records Insert:

```python
cur = mydb.cursor()
s = "INSERT INTO book (bookid, title, price) VALUES (%s, %s, %s)"
books = [(2, 'PHD', 145), (3, 'Java8', 450), (4, 'HTML', 200)]
cur.executemany(s, books)
mydb.commit()
```

**Explanation:** This code inserts multiple records into the 'book' table using `executemany`. It demonstrates how to insert books with different IDs, titles, and prices in a single operation.

### 3. SELECT Data from the 'book' Table:

```python
cur = mydb.cursor()
s = "SELECT * from book"
cur.execute(s)
result = cur.fetchall()

for rec in result:
    print(rec)
```

**Explanation:** This code retrieves all records from the 'book' table and prints them. The `SELECT *` query fetches all columns for each record.

### 4. UPDATE Data in the 'book' Table:

```python
cur = mydb.cursor()
s = "UPDATE book SET price = price + 10 WHERE price > 200"
cur.execute(s)
mydb.commit()

s = "SELECT * from book"
cur.execute(s)
result = cur.fetchall()

for rec in result:
    print(rec)
```

**Explanation:** This code updates the 'price' of books in the 'book' table. It increases the price by 10 for books where the original price was greater than 200.

### 5. DELETE Data from the 'book' Table:

```python
cur = mydb.cursor()
s = "DELETE FROM book WHERE title = 'PHD'"
cur.execute(s)
mydb.commit()
```

**Explanation:** This code deletes records from the 'book' table where the title is 'PHD'. It demonstrates how to remove specific data based on a condition.

Feel free to run these code blocks sequentially to understand how each MySQL operation affects the 'book' table.