import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

user_acc = input()

# Replace these with your Oracle database credentials and connection details
username = "CY_673380371_9"
password = "6733803719"
dsn = "10.199.8.14:1722/ORCLCDB"
table_name = "product".upper()
cursor = None
connection = None

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Check for Foreign Key Constraints
    cursor.execute(f"""SELECT COLUMN_NAME
FROM USER_CONS_COLUMNS
WHERE TABLE_NAME = 'STUDENT'
    """)

    
    for row in cursor:
        print(f"{row[0]}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()