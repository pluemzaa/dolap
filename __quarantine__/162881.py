import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

username = "CY_673380479_9"
password = "Napat12345"
dsn = "10.199.8.14:1722/ORCLCDB"
table_name = input().upper()
book_id = input().upper()
cursor = None
connection = None
try:
    # Establish a connection to the Oracle database
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    query = f"SELECT COUNT(*) cnt FROM {table_name} WHERE BOOKID='{book_id}'"    

    cursor.execute(query)

    # Fetch and print the table names
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])

except cx_Oracle.Error as error:
    print("Error:", error)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()