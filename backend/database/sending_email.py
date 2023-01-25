import smtplib
import ssl

from database.db_parinti import *
from database.presence import *


def send_email(message, receiver_email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "daspbltum@gmail.com"
    password = "btzniijtzwnfwdtp"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# nume, prenume parinte

def send_parinti(nume_prenume):
    db = new_connect()
    cur = db.cursor()
    cur.execute("SELECT posta FROM sql7588695.parinti WHERE (`nume_prenume` = '" + str(nume_prenume) + "')")
    receiver_email = str(cur.fetchall()[0][0])
    cur.close()
    db.close()
    for i in all_children(nume_prenume):
        db = new_connect()
        cur = db.cursor()
        cur.execute("SELECT idnp FROM sql7588695.elevi WHERE (`id_elev` = '" + i + "')")
        idnpcopil = str(cur.fetchall()[0][0])
        cur.close()
        db.close()
        arr = []
        tempraw = prezenta_semestru(idnpcopil)
        temp = []
        for list in tempraw:
            temp.append([str(x) for x in list])
        for list in temp:
            arr.append(' '.join(list))
        message = '\n'.join(arr)
        import smtplib
        import ssl
        port = 465  # for ssl
        smtp_server = "smtp.gmail.com"
        sender_email = "daspbltum@gmail.com"
        password = "btzniijtzwnfwdtp"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


def send_profesori(nume_prenume, receiver_email):
    db = new_connect()
    cur = db.cursor()
    cur.execute("SELECT obiect FROM sql7588695.profesori WHERE (`nume_prenume` = '" + nume_prenume + "')")
    obiect = str(cur.fetchall()[0][0])
    cur.close()
    db.close()
    arr = []
    tempraw = presence_obiect(obiect)
    temp = []
    for list in tempraw:
        temp.append([str(x) for x in list])
    for list in temp:
        arr.append(' '.join(list))
    message = '\n'.join(arr)
    import smtplib
    import ssl
    port = 465  # for ssl
    smtp_server = "smtp.gmail.com"
    sender_email = "daspbltum@gmail.com"
    password = "btzniijtzwnfwdtp"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# nume, prenume parinte
def send_day_parinti(nume_prenume, data):
    db = new_connect()
    cur = db.cursor()
    cur.execute("SELECT posta FROM sql7588695.parinti WHERE (`nume_prenume` = '" + str(nume_prenume) + "')")
    receiver_email = str(cur.fetchall()[0][0])
    cur.close()
    db.close()
    for i in all_children(nume_prenume):
        db = new_connect()
        cur = db.cursor()
        cur.execute("SELECT idnp FROM sql7588695.elevi WHERE (`id_elev` = '" + i + "')")
        idnp = str(cur.fetchall()[0][0])
        cur.close()
        db.close()
        arr = []
        tempraw = prezenta_generala(idnp, data)
        temp = []
        for list in tempraw:
            temp.append([str(x) for x in list])
        for list in temp:
            arr.append(' '.join(list))
        message = '\n'.join(arr)
        port = 465  # for ssl
        smtp_server = "smtp.gmail.com"
        sender_email = "daspbltum@gmail.com"
        password = "btzniijtzwnfwdtp"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
