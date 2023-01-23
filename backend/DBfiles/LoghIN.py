from DBfiles.DbConnector import newConnect
from mysql.connector import Error
import hashlib

# return va fi compus din id_user, rol, code of answer (aici va fi eroare daca vor exista erori)
# coduri -
# 200 its OK
# 404 user not found
# 401 wrong passwd

def signIn(username, passwd):
    db = newConnect()
    cur = db.cursor()
    hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    ans = []
    try:
        cur.execute("select passwd, id, rol from "  +
                    "(select id_elev_user as id , username, passwd, rol from sql7588695.user_elevi " +
                    "union " +
                    "select * from sql7588695.user_parinte " +
                    "union " +
                    "select * from sql7588695.user_profesor) as users " +
                    "where ( username = '" + username + "')")
        user = cur.fetchall()[0]
        # print(user)
        if(user[2] == 'elev'):
            cur.execute("select idnp from sql7588695.elevi WHERE (`id_elev` = '" + str(user[1]) + "');")
        idnp_user = cur.fetchall()[0][0]
        # print(idnp_user)
        if (user[0] == "None"):
            ans = [0, "", 404]
        elif (user[0] == hash_passwd):
            ans = [idnp_user, user[2], 200]
        else:
            ans = [idnp_user, user[2], 401]
    except Error as error:
        # print(error)
        user = cur.fetchall()
        if (user == []):
            ans = [0, "", 404]
    finally:
        cur.close()
        db.close()

    return ans