import mysql.connector

host_v = "sql7.freemysqlhosting.net"
user_v = "sql7588695"
passwd_v = "u3icbbgMbM"
db_v = "sql7588695"


def newConnect():
    db_connection = mysql.connector.connect(host = host_v, user = user_v, passwd = passwd_v, db = db_v)
    return db_connection


def viewTable(tablename):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT * FROM sql7588695." + tablename)

    # print all the first cells of all the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end='   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.close()