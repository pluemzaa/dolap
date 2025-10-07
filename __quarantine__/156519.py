import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

username = "CY_673380155_5"
password = "Godzilla64"
dsn = "10.199.8.14:1722/ORCLCDB"

table_name = input()
pk = input()

cursor = None
connection = None
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Query the data dictionary to get column information for the specified table
    cursor.execute(f"SELECT SUBJCODE FROM {table_name} ORDER BY SUBJCODE")

    for row in cursor:
        print(f"{row[0]}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()