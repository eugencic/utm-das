import smtplib, ssl
import DBParinti

from DBfiles.DBElevi import *
from DBfiles.DBParinti import *
from DBfiles.DBProfi import *
from DBfiles.LoghIN import *
from DBfiles.Presence import *
import Presence


def sendEmail(message, receiver_email):
    port = 465  # for ssl
    smtp_server = "smtp.gmail.com"
    sender_email = "daspbltum@gmail.com"
    password = "btzniijtzwnfwdtp"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# numeprenume parinte
def sendParinti(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT posta FROM sql7588695.parinti WHERE (`nume_prenume` = '" + str(nume_prenume) + "')")
    receiver_email = str(cur.fetchall()[0][0])
    cur.close()
    db.close()
    for i in DBParinti.allChilds(nume_prenume):
        db = newConnect()
        cur = db.cursor()
        cur.execute("SELECT nume_prenume FROM sql7588695.elevi WHERE (`id_elev` = '" + i + "')")
        nume_elev = str(cur.fetchall()[0][0])
        cur.close()
        db.close()
        arr = []
        tempraw = Presence.prezentaSemestru(nume_elev)
        # print(tempraw)
        temp = []
        for list in tempraw:
            temp.append([str(x) for x in list])
        for list in temp:
            arr.append(' '.join(list))
        message = '\n'.join(arr)
        import smtplib, ssl
        port = 465  # for ssl
        smtp_server = "smtp.gmail.com"
        sender_email = "daspbltum@gmail.com"
        password = "btzniijtzwnfwdtp"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def sendProfesori(nume_prenume, receiver_email):
    db = newConnect()
    cur = db.cursor()
    cur.execute("SELECT obiect FROM sql7588695.profesori WHERE (`nume_prenume` = '" + nume_prenume + "')")
    obiect = str(cur.fetchall()[0][0])
    cur.close()
    db.close()
    arr = []
    tempraw = Presence.presenceObiect(obiect)
    print(tempraw)
    # print(tempraw)
    temp = []
    for list in tempraw:
        temp.append([str(x) for x in list])
    for list in temp:
        arr.append(' '.join(list))
    message = '\n'.join(arr)
    import smtplib, ssl
    port = 465  # for ssl
    smtp_server = "smtp.gmail.com"
    sender_email = "daspbltum@gmail.com"
    password = "btzniijtzwnfwdtp"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)