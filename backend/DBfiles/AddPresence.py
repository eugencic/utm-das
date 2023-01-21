from DbConnector import newConnect
from mysql.connector import Error

# 200 succesfull
# 404 not found
##### prezenta se adauga prin indicarea tabelului, idnp-ului, si a datei

def prezent(tabel, idnp, data):

    db = newConnect()
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

    db = newConnect()
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

def exitSchool(idnp, data):

    db = newConnect()
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
