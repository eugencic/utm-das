from DBfiles.DbConnector import newConnect
from mysql.connector import Error
import numpy as np

# ans is [elev_name_surname , presence, error code ]
# 200 succesfull
# 404 not found

def checkElevPrezenta(tabel, idnp, data):
    db = newConnect()
    cur = db.cursor()
    ans = []
    nume_prenume_elev = ""
    try:
        cur.execute("SELECT id_elev FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        id_copil = cur.fetchall()[0][0]
        cur.execute("SELECT nume_prenume FROM sql7588695.elevi WHERE (`idnp` = '" + idnp + "')")
        nume_prenume_elev = cur.fetchall()[0][0]
        cur.execute("SELECT nume_prenume, `" + str(data) + "` FROM sql7588695." + tabel + " "
                    "WHERE ( `id_elev` = '" + str(id_copil) + "');")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except Error as error:
        # print(error)
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong idnp")
            ans = [nume_prenume_elev, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def prezentaGenerala(idnp, data):
    ans = []
    ans.append(checkElevPrezenta('prezenta_liceu',idnp, data))
    ans[0].pop()
    ans[0].append("Prezenta in liceu")
    ans.append(checkElevPrezenta('romana', idnp, data))
    ans[1].pop()
    ans[1].append("Romana")
    ans.append(checkElevPrezenta('engleza', idnp, data))
    ans[2].pop()
    ans[2].append("Engleza")
    ans.append(checkElevPrezenta('matematica', idnp, data))
    ans[3].pop()
    ans[3].append("Matematica")
    ans.append(checkElevPrezenta('informatica', idnp, data))
    ans[4].pop()
    ans[4].append("Inforamtica")
    return ans

def CheckPrezentaAll(tabel , idnp):
    db = newConnect()
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
        if (pres == []):
            print("Error wrong idnp")
            ans = [nume_prenume_elev, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def prezentaSemestru(idnp):
    ans = []
    ans.append(CheckPrezentaAll('prezenta_liceu', idnp))
    ans[0].pop()
    ans[0].append("Prezenta in liceu")
    ans.append(CheckPrezentaAll('romana', idnp))
    ans[1].pop()
    ans[1].append("Romana")
    ans.append(CheckPrezentaAll('engleza', idnp))
    ans[2].pop()
    ans[2].append("Engleza")
    ans.append(CheckPrezentaAll('matematica', idnp))
    ans[3].pop()
    ans[3].append("Matematica")
    ans.append(CheckPrezentaAll('informatica', idnp))
    ans[4].pop()
    ans[4].append("Informatica")
    return ans

def tuptolistConvert(tup):
    result = []
    for t in tup:
        for x in t:
            result.append(x)
    return result

def presenceObiect(tabel):
    db = newConnect()
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