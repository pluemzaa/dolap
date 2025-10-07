import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

user_acc = input()

# Replace these with your Oracle database credentials and connection details
username = "CY_673380156_3"
password = "p1563"
dsn = "10.199.8.14:1722/ORCLCDB"
table_name = "product".upper()
cursor = None
connection = None

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Check for Foreign Key Constraints
    cursor.execute(f"""SELECT column_name
from user_constraints natural join user_cons_columns
where table_name = 'SUBJECT' AND constraint_type='P' ORDER BY column_name
    """)

    
    for row in cursor:
        print(f"{row[0]}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()