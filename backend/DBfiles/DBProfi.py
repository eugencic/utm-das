from DBfiles.DbConnector import newConnect
from mysql.connector import Error
import hashlib

# parametrii name_surname pentru numele si prenumele profesorului like "john Week"
#            obiect pentru obiectul care il preda :D
def newprof(name_surname , obiect, username):
    db = newConnect()
    cur = db.cursor()
    try:
        cur.execute("SELECT id_user_profesor FROM sql7588695.user_profesor WHERE (`username` = '" + username + "')")
        id_prof = cur.fetchall()
        cur.execute("INSERT INTO `sql7588695`.`profesori` (`id_profesori`,`nume_prenume`, `obiect`) "
                "VALUES ('"+ str(id_prof[0][0]) + "', '" + name_surname + "', '" + obiect + "');")

        cur.execute("SELECT * FROM sql7588695.profesori")

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

def deleteprof(name):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT id_profesori FROM sql7588695.profesori WHERE (`nume_prenume` = '" + name + "')")
    id_prof = cur.fetchall()[0]

    cur.execute("DELETE FROM `sql7588695`.`profesori` WHERE(`nume_prenume` = '" + str(name) + "');")
    cur.execute("DELETE FROM `sql7588695`.`user_profesor` WHERE(`id_user_profesor` = '" + str(id_prof[0]) + "');")


    cur.execute("SELECT * FROM sql7588695.profesori")

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
def newuserprof(username , passwd):
    db = newConnect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO `sql7588695`.`user_profesor` (`username`, `passwd`) "
                "VALUES ('" + username + "', '" + hash_passwd + "');")

    cur.execute("SELECT * FROM sql7588695.user_profesor")

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