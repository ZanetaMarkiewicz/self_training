#### https://www.practicepython.org/

# 1 ####################################################################################################################
import datetime

current_year = datetime.datetime.now().year
name = input("Enter name: ")
age = input("Enter age: ")

hundred_year = current_year + (100 - int(age))

print(name + ", in " + str(hundred_year) + " you will be 100 years old.")


# 2 ####################################################################################################################
number = input("Enter number: ")

if int(number) % 2 != 0:
    print("Given number is odd")
else:
    if int(number) % 4 == 0:
        print("Given number is even and is a multiple of 4")


num = input("Enter number: ")
check_num = input("Enter number: ")

if int(check_num) % int(num) == 0:
    print("Check_num divides evenly into num")
else:
    print("Check_num doesn't divide evenly into num")


# 3 ####################################################################################################################
random_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_num = input("Enter number: ")
new_list = []

for i in random_list:
    if i < int(user_num):
        new_list.append(i)
print(new_list)


# 4 ####################################################################################################################
input_num = input("Enter number:")
output_list = []

for i in range(1,1000):
    if int(input_num) % i == 0:
        output_list.append(i)
print(output_list)


# 5 ####################################################################################################################
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = list(range(1,20))
# b = list(range(10,30))
c =[]

for i in a:
    if i in b:
        c.append(i)
        new_list = set(c)
print(c)
print(new_list)


# 6 ####################################################################################################################
word = input("Enter word: ")
rev_word = word[::-1]

if word == rev_word:
    print("palindrome")
else:
    print("not a palindrome")


# 7 ####################################################################################################################
list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [x for x in list_a if x % 2 == 0]

print(new_list)


# 8 ####################################################################################################################
pleyer1_input = input("pleyer1 input:")
pleyer2_input = input("pleyer2 input:")

rock = "rock"
paper = "paper"
scissors = "scissors"

if pleyer1_input == pleyer2_input:
    print("No one wins, continue game")
elif pleyer1_input == rock and pleyer2_input == paper:
    print("paper wins, user2 wins!")
elif pleyer1_input == paper and pleyer2_input == rock:
    print("paper wins, user1 wins!")
elif pleyer1_input == paper and pleyer2_input == scissors:
    print("scissors wins, user2 wins!")
elif pleyer1_input == scissors and pleyer2_input == paper:
    print("scissors wins, user1 wins!")
elif pleyer1_input == rock and pleyer2_input == scissors:
    print("rock wins, user2 wins!")
elif pleyer1_input == scissors and pleyer2_input == rock:
    print("rock wins, user1 wins!")
else:
    print("incorrect input")


# 9 ####################################################################################################################
import random

count_of_guess = 0

while True:
    random_number = random.choice(range(1, 10))
    user_guess = input("Geuss a number: ")
    if not user_guess.isalpha():
        if float(user_guess) > random_number:
            print(f"You guessed too high. Random number: {random_number} your guess: {user_guess}")
            count_of_guess += 1
        elif float(user_guess) < random_number:
            print(f"You guessed too low. Random number: {random_number} your guess: {user_guess}")
            count_of_guess += 1
        elif float(user_guess) == random_number:
            print(f"You guessed exactly right!!! Random number: {random_number} your guess: {user_guess}")
            count_of_guess += 1
    elif user_guess.upper() == "EXIT":
        print("End of game!")
        break
    else:
        print(f"You entered incorrect value {user_guess}")

print(f"You have taken {count_of_guess} attempts :)")


# 10 ###################################################################################################################
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b:
        c.append(i)
print(set(c))


# 11 ###################################################################################################################
user_input = int(input("Enter number: "))

count_parzyste = 0
count_nieparzyste = 0

a = [i for i in range(2,user_input+1) if user_input % i == 0]
print(a)

if len(a) > 1:
    print(f"{user_input} is not a prime number.")
else:
    print(f"{user_input} is a prime number.")


# 12 ###################################################################################################################
import random


def list_of_numbers():
    base_list = random.sample(range(1,100), 10)
    a = (base_list[0], base_list[-1])
    new_list = []
    new_list.append(a)
    return new_list


print(list_of_numbers())


# 13 ###################################################################################################################
user_input = int(input("Enter number of numbers that you want to calculate: "))
fibonaccie_list = []

for i in range(0,user_input):
    if i == 0:
        fibonaccie_list.append(i)
    elif i == 1:
        fibonaccie_list.append(i)
    elif i == 2:
        fibonaccie_list.append(1)
    else:
        i = fibonaccie_list[-1] + fibonaccie_list[-2]
        fibonaccie_list.append(i)

print(fibonaccie_list)


# 14 ###################################################################################################################
# 1st solution
def list_of_uniques(testing_list):
    new_list = set(testing_list)
    return new_list


print(list_of_uniques([1,1,1,1,1,21,2,2,2]))


# 2nd solution
def list_of_uniques(testing_list):
    new_list = []
    for i in testing_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(list_of_uniques([1,1,1,1,1,21,2,2,2]))


# 15 ###################################################################################################################
def backwords_sentence(input_sentence):
    splitted_sentence = input_sentence.split(" ")
    sen = splitted_sentence[::-1]
    print(' '.join(sen))


backwords_sentence(input_sentence=input("Enter sentence: "))


# 16 ###################################################################################################################
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

for i in characters:
    password = "".join(random.sample(characters, 8))
print(f"Generated password is: {password}")


"""" 17 #############################################################################################################"""
import requests
from bs4 import BeautifulSoup


def data_download():
    data_url = "https://www.nytimes.com"
    nyt_data = requests.get(data_url)
    soup = BeautifulSoup(nyt_data.text, "html.parser")

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print(story_heading.contents[0].strip())

    title = soup.find_all('span', recursive=False, )
    # print(soup.prettify())
    print(title)

data_download()


"""" 18 #############################################################################################################"""
import random

number = str(random.randint(1000, 9999))
print(number)
number_of_guesses = 0

while True:
    user_guess = input("Guess the number: ")
    cowsbulls = [0, 0]
    for i, v in enumerate(number):
        if len(user_guess) == 4:
            if i == 0 and v in user_guess[0]:
                cowsbulls[0] += 1
            elif i == 1 and v in user_guess[1]:
                cowsbulls[0] += 1
            elif i == 2 and v in user_guess[2]:
                cowsbulls[0] += 1
            elif i == 3 and v in user_guess[3]:
                cowsbulls[0] += 1
            else:
                cowsbulls[1] += 1
        else:
            print(f"You entered incorrect number! Try again!")
            break
    number_of_guesses += 1

    if cowsbulls[0] == 4:
        print(f"Random number: {number}, your score is {cowsbulls[0]} cows & {cowsbulls[1]} bulls.\n"
              f"End of game.\n"
              f"You have taken {number_of_guesses} attempts.")
        break
    else:
        print(f"Random number: {number}, your score is {cowsbulls[0]} cows & {cowsbulls[1]} bulls.\n"
              f"You have taken {number_of_guesses} attempts.")


"""" 19 #############################################################################################################"""
"""" 20 #############################################################################################################"""
def number_search():
    number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    user_number = int(input("Enter number: "))

    if user_number in number_list:
        return True
    else:
        return False


print(f"Given number availability on the list = {number_search()}")


"""" 21 #############################################################################################################"""
import os

os.rename('tekst.txt', 'tekst_2.txt')


"""" 22 #############################################################################################################"""
path = r"C:\Users\zanet\PycharmProjects\self_training\a.txt"

with open(path, "r") as file_with_names:
    initial_list = [line.rstrip('\n') for line in file_with_names.readlines()]
    print(initial_list)

    final_list = {}

    for i in initial_list:
        if i in final_list:
            final_list[i] += 1
        else:
            final_list[i] = 1

    for k, v in final_list.items():
        print(f"{k} - {v}")


"""" 23 #############################################################################################################"""
path_one = r"C:\Users\zanet\PycharmProjects\self_training\one.txt"
path_two = r"C:\Users\zanet\PycharmProjects\self_training\two.txt"

with open(path_one, "r") as file_one:
    list_one = [line.rstrip('\n') for line in file_one.readlines()]
    print(list_one, "\n================")

with open(path_two, "r") as file_two:
    list_two = [line.rstrip('\n') for line in file_two.readlines()]
    print(list_two, "\n================")

overlaps = []

for i in list_one:
    if i in list_two:
        overlaps.append(i)
print(overlaps)


"""" 24 #############################################################################################################"""
board_game = (input("what type of board game do you want to play: ")).upper()

if board_game == "TIC TAC TOE":
    print((3 * "-" + "\n" + 4 * "|" + "\n")*3 + 3 * "-")
elif board_game == "CHESS":
    print((9 * "-" + "\n" + 8 * "|" + "\n")*9 + 9 * "-")
elif board_game == "GO":
    print((19 * "-" + "\n" + 18 * "|" + "\n")*19 + 19 * "-")
else:
    print("Incorrect board game name !!!")


"""" 25 #############################################################################################################"""
import random

user_number = int(input("my number: "))

# comp_guess = random.choice(range(1,100))
# print(comp_guess)


if user_number >= 50:
    comp_guess = random.choice(range(50,100))
    print(comp_guess)
    if user_number == comp_guess:
        print("yes", comp_guess)
elif user_number < 50:
    comp_guess = random.choice(range(0, 50))
    print(comp_guess)
    if user_number == comp_guess:
        print("yes", comp_guess)
else:
    print("nothing")


"""" 33 #############################################################################################################"""
birthday_dictionary = {"Ala": 22.06, "Piotr": 22.01, "Ania": 26.08, "Wiktoria": 22.01, "Michal": 22.01}


def birthday_dict(birthday_dictionary):
    user_question = (input("Welcome to the birthday dictionary!!! \n"
                           "Enter name of person who's birthday you want to check: ")).capitalize()

    if user_question in birthday_dictionary.keys():
        print(f"{user_question}'s birthday is on {birthday_dictionary[user_question]}.")
    else:
        print(f"Dictionary don't store birthday date of person named {user_question}.")


birthday_dict(birthday_dictionary)

