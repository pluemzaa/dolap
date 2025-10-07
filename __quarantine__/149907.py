username = "system"
password = "12345"
ip = "10.199.37.42"
port = 1521
database = "xe"
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"/app/instantclient_21_12")
#cx_Oracle.init_oracle_client(lib_dir=r"D:\\Programs\\instantclient_21_12")

# Oracle credentials
#username = "system"
#password = "password1234"
#ip = "10.199.33.11"
#port = 1521
#database = "xe"


dsn = f"{ip}:{port}/{database}"

try:
    # Attempt to connect
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("OK")
    connection.close()

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("ERROR")
    print(f"  - Code: {error.code}")
    print(f"  - Message: {error.message}")