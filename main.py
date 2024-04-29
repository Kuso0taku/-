from random import randint as rnd, choice as ch
from time import sleep as slp


def begin():
    print('''
    Здравствуй, дорогой друг! Я бросаю тебе вызов в игре

                        Камень, Ножницы, Бумага
            Правила:
                    делай выбор:
                        1 - камень
                        2 - ножницы
                        3 - бумага
        Удачи!
    ''')

with open('text.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n\n')
    win = lines[0][5:].split('; ')
    lose = lines[1][6:].split('; ')
    tie = lines[2][5:].split('; ')
    phLvl = lines[3][5:].split('; ')

with open('log.txt', 'r+', encoding = 'UTF-8') as f:
    lines = f.readlines()
    if ':' in lines[0]:
        score = list(map(int, lines[0].split(':')))
    else:
        score = [0,0]

    if 'level:' in lines[1]:
        level = int(lines[1][7:])
    else:
        level = 0

comp0 = rnd(1,3)

def level1(user):
    comp = comp0

    return [user, comp]

def level2(user):
    comp = rnd(*ch([[1,2], [2,3], [0]]))
    if comp == 0:
        comp = ch(1, 3)

    return [user, comp]

def level3(user):
    comp = rnd(1,3)
    
    return [user, comp]

def level4(user):
    comp = ch([[1,2], [2,3], [1,3]])

    win = rnd(0,1)

    if win == 1:
        if user == 1 and 3 in comp:
              comp = 3
        elif user == 2 and 1 in comp:
              comp = 1
        elif user == 3 and 2 in comp:
              comp = 2

        else:
            comp = rnd(*comp)
    else:
        comp = rnd(*comp)

    return [user, comp]
    

def level5(user):
    comp = rnd(1,3)

    win = rnd(0,1)

    if win == 1:
        if user == 1:
              comp = 3
        elif user == 2:
              comp = 1
        elif user == 3:
              comp = 2
    
    return [user, comp]

Levels = {0:level, 1:level1, 2:level1, 3:level3, 4:level4, 5:level5}

if score != [0,0] or level != 1:
    print('''
    Вы хотите:
        1 - продолжить
        0 - начать заново
    ''')
    choice = input().lower()
    while choice not in ['1', '0', 'продолжить', 'начать заново']:
        print('Продолжить или начать заново?')
        choice = input()
    slp(0.5)

    if choice in ['0', 'начать заново']:
        score = [0,0]
        begin()
    else:
        print('''
        делай выбор:
            1 - камень
            2 - ножницы
            3 - бумага
        ''')
else:
    begin()

while True:
    slp(0.5)

    print(f'\tУровень {level}')
    
    user = input('Твой выбор -> ').lower()
    
    if user in ['камень', 'ножницы', 'бумага']:
        if user == 'камень':
            user = 1
        if user == 'ножницы':
            user = 2
        else:
            user = 3
    elif user in ['1', '2', '3']:
        user = int(user)
    else:
        while user not in ['камень', 'ножницы', 'бумага', '1', '2', '3']:
            print('Некорректный ввод! Попробуй еще раз!')
            user = input('-> ')

    slp(0.25)

    players = Levels[level](user)

    user = players[0]
    comp = players[1]

    if comp == user:
        print(ch(tie))
    elif comp == 1 and user == 2 or comp == 2 and user == 3 or comp == 3 and user == 1:
        score[1] = score[1]+1
        print(ch(lose))
    else:
        print(ch(win))
        score[0] = score[0]+1

    if score[0] >= 2 and level <=5 and score[0] > score[1]:
        level += 1
        print(ch(phLvl))
        score = [0,0]
    
    finish = input('\nЕще партейку? -> ').lower()
    while finish not in ['да', '1', '+', 'нет', '0', '-']:
        print('\nДа или нет?')
        finish = input('-> ').lower()

    if finish in ['да', '1', '+']:
        print('Отлично!\n')
    if finish in ['нет', '0', '-']:
        print('Слабак!')
        break

with open('log.txt', 'w+', encoding = 'UTF-8') as f:
    f.write(f'{score[0]}:{score[1]}\nlevel: {level}')

slp(0.25)
