# from add_presence import *
# from db_connector import *
# from db_elevi import *
# from db_licee import *
# from db_parinti import *
# from db_profi import *
# from log_in import *
# from new_days import *
# from presence import *
# from sending_email import *
#
#
# def main():
#     db = new_connect()
#
#     cur = db.cursor()
#     cur.execute("SELECT * FROM sql7588695.romana")
#     for row in cur.fetchall():
#         for i in range(len(row)):
#             print(row[i], end='   |   ')
#         print()
#     for i in range(30):
#         print('#', end='#')
#     print()
#
#     db.close()
#
#
# if __name__ == "__main__":
#     main()

# # adaugarea lunilor in registru
# new_data("prezenta_liceu", "23.01")
# delete_data("romana", "03.09")
#
# # adaugarea / stergerea liceelor
# new_liceu("\a","troica")
# view_table("licee")
# delete_liceu("Ion Creanga")
# view_table("licee")
#
# # crearea userului prof si a informatiilor despre acesta, si stergerea datelor
# new_user_prof("Aceaus", "Aceaus")
# new_prof("Austenie Ceausescu", "romana", "Aceaus")
# delete_prof("Austenie Ceausescu")
#
# # crearea userului parinte si a informatiilor despre acesta, si stergerea datelor
# new_user_parinte("laurentiu", "laurentiu")
# new_parinte("123456789111", "Grigore Vasile", "P. Rares", "laurentiu", "grisaVas@mail.com")
# delete_parinte("Grigore Vasile")
# print(all_children("Eugen Nistru"))
# add_children("Coseru Catalin", "Eugen Nistru ")
# change_email("katko@gmail.com", "Eugen Nistru ")
#
# # crearea userului elev si a informatiilor despre acesta / stergerea datelor personale si username-ului
# new_user_elev("laur", "laur")
# new_elev("123456789000", "Ion Vasile", "12", "P. Rares", "Grigore Vasile", "laur")
# delete_elev("Ion Vasile")
#
# # sing in
# print(sign_in("laur2", "laur1"))
# print(sign_in("laur", "laur"))
#
# # prezenta
# print(prezenta_generala("123456789105", "01.09"))
# print(prezenta_semestru("123456789105"))
# print(presence_obiect("engleza"))
#
# # sending emails
# send_email("First Try", "kat.ko.sk.23@gmail.com")
# send_parinti("Eugen Nistru")
# send_profesori("Austenie Ceausescu", "kat.ko.sk.23@gmail.com")
# send_day_parinti("Eugen Nistru", "01.09")
#
# #  presence
# #  prezenta se adauga prin indicarea tabelului, idnp-ului, si a datei
# print(presence_obiect("romana"))
# prezent('romana', "123456789105", '01.09')
# print(presence_obiect("romana"))
# absent('romana', "123456789105", '01.09')
# print(presence_obiect("romana"))
# exit_school("123456789105", '01.09')
