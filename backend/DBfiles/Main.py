import mysql.connector

import DBElevi
import DBParinti
import DBProfi
import NewDays
import DbConnector
import LoghIN
import DBLicee
import Presence
import SendingEmail

def main():
    db = DbConnector.newConnect()

    cur = db.cursor()
    cur.execute("SELECT * FROM sql7588695.romana")
    for row in cur.fetchall():
        for i in range(len(row)):
            print(row[i], end = '   |   ')
        print()
    for i in range(30):
        print('#', end = '#')
    print()

    db.close()

if __name__=="__main__":
    main()
#adaugarea lunilor in registru
    # NewDays.newdata("romana", "03.09")
    # NewDays.deletedata("romana", "03.09")

#adaugarea/stergerea liceelor
    # DBLicee.newliceu("\a","troica")
    # DbConnector.viewTable("licee")
    # DBLicee.deleteliceu("Ion Creanga")
    # DbConnector.viewTable("licee")

#crearea userului prof si a informatiilor despre acesta , si stergerea datelor
    # DBProfi.newuserprof("Aceaus","Aceaus")
    # DBProfi.newprof("Austenie Ceausescu","Programarea in retea","Aceaus")
    # DBProfi.deleteprof("Austenie Ceausescu")


#crearea userului parinte si a informatiilor despre acesta , si stergerea datelor
    # DBParinti.newuserparinte("laurentiu", "laurentiu")
    # DBParinti.newparinte("123456789111", "Grigore Vasile", "P. Rares", "laurentiu")
    # DBParinti.deleteparinte("Grigore Vasile")

#crearea userului elev si a informatiilor despre acesta / stergerea datelor personale si username-ului
    # DBElevi.newuserelev("laur","laur")
    # DBElevi.newelev("123456789000","Ion Vasile", "12", "P. Rares", "Grigore Vasile", "laur")
    # DBElevi.deleteelev("Ion Vasile")

# singIN
#     print (LoghIN.signIn("laur2","laur1"))
#     print(LoghIN.signIn("laur","laur"))
#     print(Presence.prezentaGenerala("Coseru Catalin","01.09"))
#     print(Presence.prezentaSemestru("Coseru Catalin"))

#sending emails
    # SendingEmail.sendEmail("First Try","kat.ko.sk.23@gmail.com")