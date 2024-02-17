# MySQL command line client
## Connect to MySQL Server through command line client


To connect to a MySQL server through the command-line client, you can use the `mysql` command. Here are the steps:

### 1. Open Command Prompt or PowerShell:

Open a Command Prompt or PowerShell on your Windows machine.

### 2. Navigate to MySQL Bin Directory:

The `mysql` command is usually located in the "bin" directory of your MySQL installation. If it's not in your system PATH, navigate to the MySQL bin directory using the `cd` command. For example:

```bash
cd C:\Program Files\MySQL\MySQL Server 8.0\bin
```

Make sure to replace the path with the actual path where MySQL is installed on your system.

### 3. Connect to MySQL Server:

Use the `mysql` command to connect to the MySQL server. The basic syntax is:

```bash
mysql -h hostname -u username -p
```

Replace the following placeholders:

- `hostname`: The MySQL server host (usually "localhost" for a local server).
- `username`: Your MySQL username.

After entering this command, you'll be prompted to enter the password for the specified user. Enter the password and press Enter.

For example, if you are connecting to a local MySQL server with the username "root," the command would be:

```bash
mysql -h localhost -u root -p
```

### 4. Enter Password:

After running the command, you will be prompted to enter the password for the specified MySQL user. Type the password and press Enter.

### 5. Successful Connection:

If the connection is successful, you will see the MySQL prompt, indicating that you are now connected to the MySQL server. It will look something like this:

```bash
mysql>
```

Now, you can execute SQL queries directly from the command line.

### 6. Execute SQL Queries:

You can execute SQL queries directly in the MySQL command-line client. For example:

```sql
SHOW DATABASES;
```

This query will display a list of available databases.

### 7. Exit MySQL Client:

To exit the MySQL command-line client, you can type:

```sql
exit;
```

Or use the shortcut:

```sql
\q
```

This will return you to the command prompt.

That's it! You have successfully connected to the MySQL server using the command-line client.
