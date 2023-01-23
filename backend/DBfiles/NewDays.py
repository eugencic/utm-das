#!/usr/bin/python
import mysql.connector
from DBfiles.DbConnector import newConnect

# parametrii tabel pentru denumiea tabelului si data_curenta in format 01.01 day.moth
def newdata(tabel , data_curr):
    db = newConnect()
    cur = db.cursor()

    cur.execute("ALTER TABLE `sql7588695`.`" + tabel + "` "
                "ADD COLUMN `" + str(data_curr) + "` VARCHAR(1) DEFAULT 'a' ;")

    # cur.execute("INSERT INTO `sql7588695`.`" + tabel + "` (" + data_curr + ")"
    #             "VALUES ('a') ;")

    cur.execute("SELECT * FROM sql7588695." + tabel)

    # print all the first cell of all the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end = '   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.commit()
    db.close()

def deletedata(tabel , data_to_delete):
    db = newConnect()
    cur = db.cursor()

    cur.execute("ALTER TABLE `sql7588695`.`" + str(tabel) + "` "
                "DROP COLUMN `" + str(data_to_delete) + "`;")

    cur.execute("SELECT * FROM sql7588695." + tabel)

    # print all the first cell of all the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end='   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.close()