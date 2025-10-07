import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")

username = "CY_673380190_3"
password = "0000"
dsn = "10.199.8.14:1722/ORCLCDB"

sql_test = input().upper()
sql_ans = input().upper()
cursor = None
connection = None

def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for row1, row2 in zip(list1, list2):
        if row1 != row2:
            return False

    return True

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    # Query the data dictionary to get column information for the specified table
    cursor.execute(f"{sql_ans}")
    rows = cursor.fetchall()
    cursor.execute(f"{sql_test}")
    test_rows = cursor.fetchall()

    print(are_lists_equal(rows,test_rows))

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()