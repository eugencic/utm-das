from DbConnector import newConnect


# parametrii name pentru denumiea liceului si adresa - adress
def newliceu(name , adress):
    db = newConnect()
    cur = db.cursor()

    cur.execute("INSERT INTO `sql7588695`.`licee` (`denumire`, `adresa`) "
                "VALUES ('" + name + "', '" + adress + "');")

    cur.execute("SELECT * FROM sql7588695.licee")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end = '   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.commit()
    cur.close()
    db.close()

def deleteliceu(name):
    db = newConnect()
    cur = db.cursor()

    cur.execute("DELETE FROM `sql7588695`.`licee` WHERE(`denumire` = '" + str(name) + "');")

    cur.execute("SELECT * FROM sql7588695.licee")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end='   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.commit()
    cur.close()
    db.close()