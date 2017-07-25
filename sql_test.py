import pymssql

# We can connect to local sql server
c = pymssql.connect("127.0.0.1", "sam-PC\sam", "730625")
c.autocommit(True)

cursor = c.cursor()
cursor.execute("CREATE DATABASE Foo")
c.autocommit(False)
