# player1 = int(input("player1 :"))
# player2 = int(input("player1 :"))
# player3 = int(input("player1 :"))

game = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

# for i in game:
#     print(i[0])
#     if i[0] == i[1] == i[2] == 1:
#         print("player 1 won")
#     elif i[0] == i[1] == i[2] == 2:
#         print("player 2 won")

for i in game[0]:
    print(game[0])
    if i == 1:
        print("player 1 won")
    elif i == 2:
        print("player 2 won")


# print(game[0][0])
#
# for i in game:
#     if game[0][0] == game[1][0] == game[2][0]:
#         if i == 1:
#             print("player 1 won")
#         else:
#             print("player 2 won")
#     elif game[0][1] == game[1][1] == game[2][1]:
#         if i == 1:
#             print("player 1 won")
#         else:
#             print("player 2 won")
#     elif game[0][2] == game[1][2] == game[2][2]:
#         if i == 1:
#             print("player 1 won")
#         else:
#             print("player 2 won")