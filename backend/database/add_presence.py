from database.db_connector import new_connect
from mysql.connector import Error

# 200 successful
# 404 not found
# prezenta se adauga prin indicarea tabelului, idnp-ului, si datei

def prezent(tabel, idnp, data):
    db = new_connect()
    cur = db.cursor()
    ans = 200
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("UPDATE sql7588695." + tabel + " SET `" + data + "` = 'p'"
                                                                     "where ( `id_elev` = '" + str(id_copil) + "');")
        db.commit()
    except Error as err:
        print(err)
        ans = 404
    finally:
        cur.close()
        db.close()

    return ans


def absent(tabel, idnp, data):
    db = new_connect()
    cur = db.cursor()
    ans = 200
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("UPDATE sql7588695." + tabel + " SET `" + data + "` = 'a'"
                                                                     "where ( `id_elev` = '" + str(id_copil) + "');")
        db.commit()
    except Error as err:
        print(err)
        ans = 404
    finally:
        cur.close()
        db.close()

    return ans


def exit_school(idnp, data):
    db = new_connect()
    cur = db.cursor()
    ans = 200
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("UPDATE sql7588695.prezenta_liceu SET `" + data + "` = 'e'"
                                                                      "where ( `id_elev` = '" + str(id_copil) + "');")
        db.commit()
    except Error as err:
        print(err)
        ans = 404
    finally:
        cur.close()
        db.close()

    return ans


def prezent_liceu(idnp, data):
    db = new_connect()
    cur = db.cursor()
    ans = 200
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]

        cur.execute("SELECT `" + data + "` FROM sql7588695.prezenta_liceu WHERE `id_elev` = '" + str(id_copil) + "'")
        prezenta = cur.fetchall()[0][0]

        if prezenta == 'p':
            cur.execute("UPDATE sql7588695.prezenta_liceu SET `" + data + "` = 'e'"
                                                                          "where ( `id_elev` = '" + str(
                id_copil) + "');")
        else:
            cur.execute("UPDATE sql7588695.prezenta_liceu SET `" + data + "` = 'p'"
                                                                          "where ( `id_elev` = '" + str(
                id_copil) + "');")
        db.commit()
    except Error as err:
        print(err)
        ans = 404
    finally:
        cur.close()
        db.close()

    return ans
