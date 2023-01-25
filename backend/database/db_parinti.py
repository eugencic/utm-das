import hashlib

from database.db_connector import *
from mysql.connector import Error

# parametrii name_surname pentru numele si prenumele parintelui like "John Week"
#            liceul pentru liceul unde invata copii sai
#            username - username-ul dupa logare

def new_parinte(idnp, name_surname, liceu, username, posta):
    db = new_connect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_user_parinte FROM sql7588695.user_parinte WHERE (`username` = '" + username + "')")
        id_prof = cur.fetchall()
        cur.execute("SELECT id_liceu FROM sql7588695.licee WHERE (`denumire` = '" + liceu + "')")
        id_liceu = cur.fetchall()

        cur.execute("INSERT INTO `sql7588695`.`parinti` (`id_parinte`,`idnp`,`nume_prenume`, `id_liceu`, `posta`) "
                    "VALUES ('" + str(id_prof[0][0]) + "', '" + idnp + "', '" + name_surname + "', '" + str(
            id_liceu[0][0]) + "', '" + str(posta) + "');")

        cur.execute("SELECT * FROM sql7588695.parinti")

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


def delete_parinte(name):
    db = new_connect()
    cur = db.cursor()
    cur.execute("SELECT id_parinte FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
    id_prof = cur.fetchall()[0]

    cur.execute("DELETE FROM `sql7588695`.`parinti` WHERE(`nume_prenume` = '" + str(name) + "');")
    cur.execute("DELETE FROM `sql7588695`.`user_parinte` WHERE(`id_user_parinte` = '" + str(id_prof[0]) + "');")

    cur.execute("SELECT * FROM sql7588695.parinti")

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
def new_user_parinte(username, passwd):
    db = new_connect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO `sql7588695`.`user_parinte` (`username`, `passwd`, `rol`) "
                "VALUES ('" + username + "', '" + hash_passwd + "', 'parinte');")

    cur.execute("SELECT * FROM sql7588695.user_parinte")

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


# param copil e numele copilului, iar name e numele parintelui
def add_children(copil, name):
    db = new_connect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`nume_prenume` = '" + copil + "')")
        id_copil = cur.fetchall()
        cur.execute("SELECT id_copii,id_parinte FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
        temp = list(cur.fetchall()[0])
        parinte_copii_id = str(temp[0])
        parinte_id = str(temp[1])

        if parinte_copii_id == "None":
            parinte_copii_id = ''

        cur.execute("UPDATE `sql7588695`.`parinti` SET `id_copii` =  ('" + parinte_copii_id + "," + str(
            id_copil[0][0]) + "') WHERE (`id_parinte` = '" + parinte_id + "');")

        cur.execute("SELECT * FROM sql7588695.parinti")

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


def all_children(name):
    db = new_connect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_copii FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
        parinte_copii_id = cur.fetchall()[0][0]
        db.commit()
    except Error as error:
        print(error)

    finally:
        cur.close()
        db.close()

    ans = parinte_copii_id.split(",")
    return ans


def change_email(new_post, name):
    db = new_connect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_parinte FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
        parinte_id = cur.fetchall()[0][0]
        cur.execute("UPDATE `sql7588695`.`parinti` SET `posta` =  '" + new_post + "' WHERE `id_parinte` = '" + str(
            parinte_id) + "';")

        cur.execute("SELECT * FROM sql7588695.parinti")

        # print all the first cell of all the rows
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
