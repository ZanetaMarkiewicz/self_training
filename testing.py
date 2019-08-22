# # player1 = int(input("player1 :"))
# # player2 = int(input("player1 :"))
# # player3 = int(input("player1 :"))
# #
# # game = [[2, 2, 0],
# #         [2, 1, 0],
# #         [2, 1, 1]]
#
# # for i in game:
# #     print(i[0])
# #     if i[0] == i[1] == i[2] == 1:
# #         print("player 1 won")
# #     elif i[0] == i[1] == i[2] == 2:
# #         print("player 2 won")
#
# # for i in game[0]:
# #     print(game[0])
# #     if i == 1:
# #         print("player 1 won")
# #     elif i == 2:
# #         print("player 2 won")
# #
# #
# # # print(game[0][0])
# # #
# # # for i in game:
# # #     if game[0][0] == game[1][0] == game[2][0]:
# # #         if i == 1:
# # #             print("player 1 won")
# # #         else:
# # #             print("player 2 won")
# # #     elif game[0][1] == game[1][1] == game[2][1]:
# # #         if i == 1:
# # #             print("player 1 won")
# # #         else:
# # #             print("player 2 won")
# # #     elif game[0][2] == game[1][2] == game[2][2]:
# # #         if i == 1:
# # #             print("player 1 won")
# # #         else:
# # #             print("player 2 won")
#
# # imie = "JOanna"
# # print(imie[6])
# #
# # a = 5
# # b = 6
# # a == 7
# # b = 8
# #
# # print(a)
#
#
# # imie = "Kamila"
# #
# # if imie[0].isupper() and not imie[-1].isupper():
# #         print("aaa")
# # else:
# #         print("dd")
#
#
# # indeks = 0
# #
# # for litera in "Kotek":
# #         print("Litera nr. {} to {}".format(indeks, litera))
# #         break
# #         indeks += 1
# # print(indeks)
#
#
# # i = 100
# # while i >= 100:
# #         print(i)
# # i -= 1
# # print(i)
#
#
# # for i in range(0, 99, 33):
# #         print(i)
#
#
# # grupa = ["mlody", "sredni", "dojrzaly"]
# # wiek = 30
# #
# # if wiek <30:
# #         grupa_osoby = grupa[0]
# # elif 30 <= wiek < 60:
# #         grupa_osoby = grupa[1]
# # else:
# #         grupa_osoby = grupa[2]
# #
# # print(grupa_osoby)
#
# grupa = ["mlody", "sredni", "dojrzaly"]
# wiek = 30
#
# def okresl_grupe(wiek):
#         if wiek <30:
#                 grupa_osoby = grupa[0]
#         elif 30 <= wiek < 60:
#                 grupa_osoby = grupa[1]
#         else:
#                 grupa_osoby = grupa[2]
#         return grupa_osoby
#
# okresl_grupe(wiek)
# print(grupa_osoby)
#
with open(r"D:\!_Python_trainig\scripts_IS\ccc.txt", "r+") as art_plik:
    # article_content = art_plik.read()
    write_file = art_plik.write("ala ma kota")
#


# # # dziedziczenie diamentowe, od lewej do prawej, wiec jesli 2 takie same funkcje wystepuja w roznych klasach
# # # z ktorych dziedziczy, to wezmie ta def tylko z pierwszej
# # try:
# #         with open(r"D:\!_Python_trainig\self_training\Dane.csv","r+") as plik:
# #                 line = plik.readline()
# #                 print("To jest kod bez bledu w try")
# # except FileNotFoundError:
# #         print("Nie prawda nie ma pliku")
# # except IOError:
# #         print("jednak nie mozna przeczytac linijki w trybie w")
# # finally:
# #         print("plik zostal zmankniety")
#
# #
# # class Zwierz(object):
# #         def mow(self):
# #                 print("jestem zwierz")
# #
# # class Orka(Zwierz):
# #         def mow(self):
# #                 print("jestem Orka")
# #
# # class Delfin(Zwierz):
# #         def mow(self):
# #                 print("jestem delfin")
# #
# # class Orkin(Orka, Delfin):
# #         pass
# #
# # x = Orkin()
# # x.mow()
# #
#
# # class Samochod(object):
# #         def __init__(self, marka, kolor):
# #                 self.producent = marka
# #                 self.kolor = kolor
# #
# # auto1 = Samochod("Volvo", "czarny")
# # auto1.model = "XC60"
# #
# # print(auto1.model)