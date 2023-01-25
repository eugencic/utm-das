import hashlib

from database.db_connector import new_connect
from mysql.connector import Error

# parametrii name_surname pentru numele si prenumele profesorului like "John Week"
#            obiect pentru obiectul care il preda

def new_prof(name_surname, obiect, username):
    db = new_connect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_user_profesor FROM sql7588695.user_profesor WHERE (`username` = '" + username + "')")
        id_prof = cur.fetchall()
        cur.execute("INSERT INTO `sql7588695`.`profesori` (`id_profesori`,`nume_prenume`, `obiect`) "
                    "VALUES ('" + str(id_prof[0][0]) + "', '" + name_surname + "', '" + obiect + "');")

        cur.execute("SELECT * FROM sql7588695.profesori")

        # print the first cell of the rows
        for row in cur.fetchall():
            for i in range(len(row)):
                print(row[i], end='   |   ')
            print()

        for i in range(30):
            print('#', end='#')
        print()

        db.commit()

    except Error as error:
        print(error)

    finally:
        cur.close()
        db.close()


def delete_prof(name):
    db = new_connect()
    cur = db.cursor()
    cur.execute("SELECT id_profesori FROM sql7588695.profesori WHERE (`nume_prenume` = '" + name + "')")
    id_prof = cur.fetchall()[0]

    cur.execute("DELETE FROM `sql7588695`.`profesori` WHERE(`nume_prenume` = '" + str(name) + "');")
    cur.execute("DELETE FROM `sql7588695`.`user_profesor` WHERE(`id_user_profesor` = '" + str(id_prof[0]) + "');")

    cur.execute("SELECT * FROM sql7588695.profesori")

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


# parametrii username pentru username
#            passwd pentru parola

def new_user_prof(username, passwd):
    db = new_connect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO `sql7588695`.`user_profesor` (`username`, `passwd`) "
                "VALUES ('" + username + "', '" + hash_passwd + "');")

    cur.execute("SELECT * FROM sql7588695.user_profesor")

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
