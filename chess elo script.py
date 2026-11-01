from tkinter import *
from tkinter import messagebox
import random
import re



repeat = True
elocalculate=False
first_playercheck = False
second_playercheck = False

def elochanger1(file, name):
    with open(file, 'r', encoding='utf-8') as file_handler:
                filereader= file_handler.read()
                elo_change = filereader.replace(f'{name}{winnerelo}',f'{name}{newelo1}')
    with open(file, 'w', encoding='utf-8') as file_handler:
        file_handler.write(elo_change)


def elochanger2(file, name):
    with open(file, 'r', encoding='utf-8') as file_handler:
                filereader= file_handler.read()
                elo_change = filereader.replace(f'{name}{loserelo}',f'{name}{newelo2}')
    with open(file, 'w', encoding='utf-8') as file_handler:
        file_handler.write(elo_change)



def elofinder1(file, name):
    with  open (file, 'r', encoding = 'utf-8') as file_handler:
        for line in file_handler:
            if name in line:
                rawstring = re.search(r'\d+', line)
                winnerelo = int(rawstring.group())
                return winnerelo

def elofinder2(file, name):
    with  open (file, 'r', encoding = 'utf-8') as file_handler:
        for line in file_handler:
            if name in line:
                rawstring = re.search(r'\d+', line)
                loserelo = int(rawstring.group())
                return loserelo




def name_finder_elo(file, name):
    with open(file, 'r', encoding = 'utf-8') as file_handler:
        for line in file_handler:
            if name in line:
                return True



        print('this name is not registered')
        return False




def name_finder(file,name):
    with open(file, 'r', encoding = 'utf-8') as file_handler:
        for line in file_handler:
            if name in line:
                print(f"{name} is already registered")
                return True

        file_handler = open(file, 'a', encoding = 'utf-8')
        file_handler.write(f'{name}800\n')
        file_handler.close()
        print('name registered successfully')
        return True

while repeat and not first_playercheck:
    register = input('Register a new player(type 1) or log a match?(type 2)')
    if register == '1':
        name_inserted = input('Type player First and last name').replace(" ","").lower()
        repeat = name_finder('member_info.txt',f'{name_inserted}')
    elif register == '2':
        name_inserted1 = input('Enter winner name').replace(" ", "").lower()
        first_playercheck = name_finder_elo('member_info.txt', f'{name_inserted1}')





while first_playercheck:
    name_inserted2 = input('Enter loser name').replace(" ","").lower()
    second_playercheck = name_finder_elo('member_info.txt', f'{name_inserted2}')
    if second_playercheck and name_inserted2 != name_inserted1:
        elocalculate=True
        first_playercheck = False
    elif second_playercheck and name_inserted2 == name_inserted1:
        print(f'{name_inserted1} was typed in already')
        second_playercheck = False



while elocalculate:
    winnerelo=elofinder1('member_info.txt',f'{name_inserted1}')
    loserelo=elofinder2('member_info.txt', f'{name_inserted2}')
    expectedscore1 = 1/(1+(10 ** ((loserelo - winnerelo)/100)))
    newelo1 = round(winnerelo +(32*(1-expectedscore1)))
    expectedscore2 = 1 / (1 + (10 ** ((winnerelo- loserelo) / 100)))
    newelo2 = round(loserelo + (32 * (0 - expectedscore2)))

    elochanger1('member_info.txt',f'{name_inserted1}')
    elochanger2('member_info.txt',f'{name_inserted2}')

    print(f'{name_inserted1} new elo is {newelo1}')
    print(f'{name_inserted2} new elo is {newelo2}')

    elocalculate = False










































