import mysql.connector

from DBfiles.DBElevi import *
from DBfiles.DBParinti import *
from DBfiles.DBProfi import *
from DBfiles.NewDays import *
from DBfiles.DbConnector import *
from DBfiles.LoghIN import *
from DBfiles.DBLicee import *
from DBfiles.Presence import *
from DBfiles.SendingEmail import *
from DBfiles.AddPresence import *

def main():
    db = newConnect()

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
# adaugarea lunilor in registru
    # NewDays.newdata("romana", "03.09")
    # NewDays.deletedata("romana", "03.09")

# adaugarea/stergerea liceelor
    # DBLicee.newliceu("\a","troica")
    # DbConnector.viewTable("licee")
    # DBLicee.deleteliceu("Ion Creanga")
    # DbConnector.viewTable("licee")

# crearea userului prof si a informatiilor despre acesta, si stergerea datelor
    # DBProfi.newuserprof("Aceaus","Aceaus")
    # DBProfi.newprof("Austenie Ceausescu","romana","Aceaus")
    # DBProfi.deleteprof("Austenie Ceausescu")

# crearea userului parinte si a informatiilor despre acesta, si stergerea datelor
   # DBParinti.newuserparinte("laurentiu", "laurentiu")
    # DBParinti.newparinte("123456789111", "Grigore Vasile", "P. Rares", "laurentiu","grisaVas@mail.com")
    # DBParinti.deleteparinte("Grigore Vasile")
    # print(DBParinti.allChilds("Eugen Nistru"))
    # DBParinti.addChilds("Coseru Catalin", "Eugen Nistru ")
    # DBParinti.changeemail("katko@gmail.com", "Eugen Nistru ")

# crearea userului elev si a informatiilor despre acesta / stergerea datelor personale si username-ului
    # DBElevi.newuserelev("laur","laur")
    # DBElevi.newelev("123456789000","Ion Vasile", "12", "P. Rares", "Grigore Vasile", "laur")
    # DBElevi.deleteelev("Ion Vasile")

# singIN
#     print (LoghIN.signIn("laur2","laur1"))
#     print(LoghIN.signIn("laur","laur"))

# prezenta
#     print(Presence.prezentaGenerala("123456789105","01.09"))
#     print(Presence.prezentaSemestru("123456789105"))
#     print(Presence.presenceObiect("engleza"))

# sending emails
    # SendingEmail.sendEmail("First Try","kat.ko.sk.23@gmail.com")
    sendParinti("Eugen Nistru")
    # SendingEmail.sendProfesori("Austenie Ceausescu", "kat.ko.sk.23@gmail.com")
    sendDayParinti("Eugen Nistru", "01.09")

# add presence
#     prezenta se adauga prin indicarea tabelului, idnp-ului, si a datei
#     print(Presence.presenceObiect("romana"))
#     AddPresence.prezent('romana', "123456789105", '01.09')
#     print(Presence.presenceObiect("romana"))
#     AddPresence.absent('romana', "123456789105", '01.09')
#     print(Presence.presenceObiect("romana"))
#     AddPresence.exitSchool("123456789105", '01.09')