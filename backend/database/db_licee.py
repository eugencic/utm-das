from database.db_connector import new_connect

# parametrii name pentru denumiea liceului si adresa - adress

def new_liceu(name, adress):
    db = new_connect()
    cur = db.cursor()

    cur.execute("INSERT INTO `sql7588695`.`licee` (`denumire`, `adresa`) "
                "VALUES ('" + name + "', '" + adress + "');")

    cur.execute("SELECT * FROM sql7588695.licee")

    # print the first cell of the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end='   |   ')
        print()
    for i in range(30):
        print('#', end='#')
    print()

    db.commit()
    cur.close()
    db.close()


def delete_liceu(name):
    db = new_connect()
    cur = db.cursor()

    cur.execute("DELETE FROM `sql7588695`.`licee` WHERE(`denumire` = '" + str(name) + "');")

    cur.execute("SELECT * FROM sql7588695.licee")

    # print the first cell of the rows
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end='   |   ')
        print()
    for i in range(30):
        print('#', end='#')
    print()

    db.commit()
    cur.close()
    db.close()
