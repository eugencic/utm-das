from DBfiles.DbConnector import newConnect
from mysql.connector import Error
import hashlib


# parametrii username pentru username
#            passwd pentru parola
def newuserelev(username , passwd):
    db = newConnect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO `sql7588695`.`user_elevi` (`username`, `passwd`, `rol`) "
                "VALUES ('" + username + "', '" + hash_passwd  + "', 'elev');")

    cur.execute("SELECT * FROM sql7588695.user_elevi")

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

# parametrii name_surname pentru numele si prenumele eleului like "john Week"
#            clasa in care invata
#            liceu - numele liceului
#            parinte - numele parintelui
#            username-ul de la logare
def newelev(idnp, name_surname , clasa, liceu, parinte, username):
    db = newConnect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_elev_user FROM sql7588695.user_elevi WHERE (`username` = '" + username + "')")
        id_elev = cur.fetchall()[0][0]
        cur.execute("SELECT id_liceu FROM sql7588695.licee WHERE (`denumire` = '" + liceu + "')")
        id_liceu = cur.fetchall()[0][0]
        cur.execute("SELECT id_parinte FROM sql7588695.parinti WHERE (`nume_prenume` = '" + parinte + "')")
        id_parinte = cur.fetchall()[0][0]

        cur.execute("INSERT INTO `sql7588695`.`elevi` (`id_elev`,`idnp`,`nume_prenume`,`clasa`, `id_liceu`, `parinte`) "
                "VALUES ('"+ str(id_elev) + "', '" + idnp + "', '" + name_surname + "', '" + str(clasa) + "', '" + str(id_liceu) + "', '" + str(id_parinte) + "');")

        insertTables(str(id_elev),name_surname,db)

        cur.execute("SELECT * FROM sql7588695.elevi")

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

# INSERT INTO `sql7588695`.`matematica` (`id_elev`, `nume_prenume`, `01.09`) VALUES ('6', 'Iana L', 'p');


def deleteelev(name):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`nume_prenume` = '" + name + "')")
    id_elev = cur.fetchall()[0][0]

    deleteTables(str(id_elev),db)

    cur.execute("DELETE FROM `sql7588695`.`elevi` WHERE(`nume_prenume` = '" + str(name) + "');")
    cur.execute("DELETE FROM `sql7588695`.`user_elevi` WHERE(`id_elev_user` = '" + str(id_elev) + "');")



    cur.execute("SELECT * FROM sql7588695.elevi")

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

def insertTables(id_elev, nume_prenume, db):
    cur = db.cursor()
    try:
        cur.execute("INSERT INTO `sql7588695`.`matematica` (`id_elev`, `nume_prenume`) VALUES ('"+ id_elev + "', '" + str(nume_prenume) + " ');")
        cur.execute("INSERT INTO `sql7588695`.`romana` (`id_elev`, `nume_prenume`) VALUES ('"+ id_elev + "', '" + str(nume_prenume) + " ');")
        cur.execute("INSERT INTO `sql7588695`.`engleza` (`id_elev`, `nume_prenume`) VALUES ('"+ id_elev + "', '" + str(nume_prenume) + " ');")
        cur.execute("INSERT INTO `sql7588695`.`informatica` (`id_elev`, `nume_prenume`) VALUES ('"+ id_elev + "', '" + str(nume_prenume) + " ');")

        db.commit()
    except Error as error:
        print(error)

    finally :
        cur.close()

def deleteTables(id_elev,db):
    cur = db.cursor()
    try:
        cur.execute("DELETE FROM `sql7588695`.`matematica` WHERE (`id_elev` = '" + id_elev + "');")
        cur.execute("DELETE FROM `sql7588695`.`romana` WHERE (`id_elev` = '" + id_elev + "');")
        cur.execute("DELETE FROM `sql7588695`.`engleza` WHERE (`id_elev` = '" + id_elev + "');")
        cur.execute("DELETE FROM `sql7588695`.`informatica` WHERE (`id_elev` = '" + id_elev + "');")

        db.commit()
    except Error as error:
        print(error)

    finally:
        cur.close()