from database.db_connector import new_connect
from mysql.connector import Error

# answer is [elev_name_surname , presence, error code ]
# 200 successful
# 404 not found

def check_elev_prezenta(tabel, idnp, data):
    db = new_connect()
    cur = db.cursor()
    ans = []
    nume_prenume_elev = ""
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("SELECT nume_prenume FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        nume_prenume_elev = cur.fetchall()[0][0]
        cur.execute("SELECT nume_prenume, `" + str(data) + "` FROM sql7588695." + tabel + " "
                                                                                          "WHERE ( `id_elev` = '" + str(
            id_copil) + "');")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except Error as error:
        # print(error)
        pres = cur.fetchall()
        if not pres:
            print("Error. Wrong idnp")
            ans = [nume_prenume_elev, '', 404]
    finally:
        cur.close()
        db.close()

    return ans


def prezenta_generala(idnp, data):
    ans = [check_elev_prezenta('prezenta_liceu', idnp, data)]
    ans[0].pop()
    ans[0].append("Prezenta in liceu")
    ans.append(check_elev_prezenta('romana', idnp, data))
    ans[1].pop()
    ans[1].append("Romana")
    ans.append(check_elev_prezenta('engleza', idnp, data))
    ans[2].pop()
    ans[2].append("Engleza")
    ans.append(check_elev_prezenta('matematica', idnp, data))
    ans[3].pop()
    ans[3].append("Matematica")
    ans.append(check_elev_prezenta('informatica', idnp, data))
    ans[4].pop()
    ans[4].append("Inforamtica")
    return ans


def check_prezenta_all(tabel, idnp):
    db = new_connect()
    cur = db.cursor()
    ans = []
    nume_prenume_elev = ""
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("SELECT nume_prenume FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        nume_prenume_elev = cur.fetchall()[0][0]
        cur.execute("Select * from sql7588695." + tabel + "  where ( `id_elev` = '" + str(id_copil) + "')")
        pres = cur.fetchall()[0]
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if not pres:
            print("Error. Wrong idnp")
            ans = [nume_prenume_elev, '', 404]
    finally:
        cur.close()
        db.close()

    return ans


def prezenta_semestru(idnp):
    ans = [check_prezenta_all('prezenta_liceu', idnp)]
    ans[0].pop()
    ans[0].append("Prezenta in liceu")
    ans.append(check_prezenta_all('romana', idnp))
    ans[1].pop()
    ans[1].append("Romana")
    ans.append(check_prezenta_all('engleza', idnp))
    ans[2].pop()
    ans[2].append("Engleza")
    ans.append(check_prezenta_all('matematica', idnp))
    ans[3].pop()
    ans[3].append("Matematica")
    ans.append(check_prezenta_all('informatica', idnp))
    ans[4].pop()
    ans[4].append("Informatica")
    return ans


def tuptolist_convert(tup):
    result = []
    for t in tup:
        for x in t:
            result.append(x)
    return result


def presence_obiect(tabel):
    db = new_connect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695." + str(tabel) + ";")
        pres = cur.fetchall()
        arr = list(pres)
        ans = [list(ele) for ele in arr]
    except:
        pres = cur.fetchall()
        print("Error")
    finally:
        cur.close()
        db.close()

    return ans
