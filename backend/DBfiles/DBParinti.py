from DbConnector import newConnect
from mysql.connector import Error
import hashlib

# parametrii name_surname pentru numele si prenumele parintelui like "john Week"
#            liceul pentru liceul unde invata copii sai :D
#            username - username-ul dupa logare
def newparinte(idnp, name_surname , liceu, username, posta):
    db = newConnect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_user_parinte FROM sql7588695.user_parinte WHERE (`username` = '" + username + "')")
        id_prof = cur.fetchall()
        cur.execute("SELECT id_liceu FROM sql7588695.licee WHERE (`denumire` = '" + liceu + "')")
        id_liceu = cur.fetchall()

        cur.execute("INSERT INTO `sql7588695`.`parinti` (`id_parinte`,`idnp`,`nume_prenume`, `id_liceu`, `posta`) "
                "VALUES ('"+ str(id_prof[0][0]) + "', '" + idnp + "', '" + name_surname + "', '" + str(id_liceu[0][0]) + "', '" + str(posta) +"');")

        cur.execute("SELECT * FROM sql7588695.parinti")

        # print all the first cell of all the rows
        for row in cur.fetchall():
            for i in range(len(row)):
                print(row[i], end = '   |   ')
            print()

        for i in range(30):
            print('#', end = '#')
        print()

        db.commit()

    except Error as error:
        print(error)

    finally:
        cur.close()
        db.close()

def deleteparinte(name):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT id_parinte FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
    id_prof = cur.fetchall()[0]

    cur.execute("DELETE FROM `sql7588695`.`parinti` WHERE(`nume_prenume` = '" + str(name) + "');")
    cur.execute("DELETE FROM `sql7588695`.`user_parinte` WHERE(`id_user_parinte` = '" + str(id_prof[0]) + "');")


    cur.execute("SELECT * FROM sql7588695.parinti")

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

# parametrii username pentru username
#            passwd pentru parola
def newuserparinte(username , passwd):
    db = newConnect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO `sql7588695`.`user_parinte` (`username`, `passwd`, `rol`) "
                "VALUES ('" + username + "', '" + hash_passwd  + "', 'parinte');")

    cur.execute("SELECT * FROM sql7588695.user_parinte")

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

#param copil e numele copilului , iar name e numele parintelui
def addChilds(copil,name):
    db = newConnect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`nume_prenume` = '" + copil + "')")
        id_copil = cur.fetchall()
        cur.execute("SELECT id_copii FROM sql7588695.parinti WHERE (`nume_prenume` = '" + name + "')")
        parinte_copii_id = cur.fetchall()[0][0]
        if parinte_copii_id == "None" :
            parinte_copii_id = ''

        cur.execute("INSERT INTO `sql7588695`.`parinti` (`id_copii`) "
                "VALUES ('"+ parinte_copii_id + "," + str(id_copil[0][0]) + "');")

        cur.execute("SELECT * FROM sql7588695.parinti")

        # print all the first cell of all the rows
        for row in cur.fetchall():
            for i in range(len(row)):
                print(row[i], end = '   |   ')
            print()

        for i in range(30):
            print('#', end = '#')
        print()

        db.commit()
    except Error as error:
        print(error)

    finally:
        cur.close()
        db.close()

def allChilds(name):
    db = newConnect()
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