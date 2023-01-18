from DbConnector import newConnect
from mysql.connector import Error
import numpy as np


# ans is [elev_name_surname , presence, error code ]
# 200 succesfull
# 404 not found

def engleza(nume_prenume, data):

    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select nume_prenume, `" + data + "` from sql7588695.engleza " +
                    "where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans


def romana(nume_prenume, data):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select nume_prenume, `" + data + "` from sql7588695.romana " +
                                                      "where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans


def matematica(nume_prenume, data):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select nume_prenume, `" + data + "` from sql7588695.matematica " +
                                                      "where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans


def informatica(nume_prenume, data):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select nume_prenume, `" + data + "` from sql7588695.informatica " +
                                                      "where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def prezenta_liceu(nume_prenume, data):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select nume_prenume, `" + data + "` from sql7588695.prezenta_liceu " +
                                                      "where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = [pres[0], pres[1], 200]
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def prezentaGenerala(nume_prenume, data):
    ans = []
    ans.append(prezenta_liceu(nume_prenume, data))
    ans[0].append("Prezenta in liceu")
    ans.append(romana(nume_prenume, data))
    ans[1].append("Romana")
    ans.append(engleza(nume_prenume, data))
    ans[2].append("Engleza")
    ans.append(matematica(nume_prenume, data))
    ans[3].append("Matematica")
    ans.append(informatica(nume_prenume, data))
    ans[4].append("Inforamtica")
    return ans

def prezenta_liceuAll(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695.prezenta_liceu where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def romanaAll(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695.romana where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        # print(pres)
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def englezaAll(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695.engleza where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        # print(pres)
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def matematicaAll(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695.matematica where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def informaticaAll(nume_prenume):
    db = newConnect()
    cur = db.cursor()
    ans = []
    try:
        cur.execute("Select * from sql7588695.informatica where ( nume_prenume = '" + nume_prenume + "')")
        pres = cur.fetchall()[0]
        ans = list(pres)
        ans.pop(0)
        ans.append(200)
    except:
        pres = cur.fetchall()
        if (pres == []):
            print("Error wrong name")
            ans = [nume_prenume, '', 404]
    finally:
        cur.close()
        db.close()

    return ans

def prezentaSemestru(nume_prenume):
    ans = []
    ans.append(prezenta_liceuAll(nume_prenume))
    ans[0].append("Prezenta in liceu")
    ans.append(romanaAll(nume_prenume))
    ans[1].append("Romana")
    ans.append(englezaAll(nume_prenume))
    ans[2].append("Engleza")
    ans.append(matematicaAll(nume_prenume))
    ans[3].append("Matematica")
    ans.append(informaticaAll(nume_prenume))
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

