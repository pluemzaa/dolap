import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

username = "CY_673380552_5"
password = "p5525"
dsn = "10.199.8.14:1722/ORCLCDB"

table_name = input().upper()
cursor = None
connection = None
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Query the data dictionary to get column information for the specified table
    cursor.execute(f"SELECT column_name, data_type, data_length FROM all_tab_columns WHERE table_name = '{table_name}'")

    for row in cursor:
        print(f"{row[0]}|{row[1]}|{row[2]}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()