import random, os  # Подключаем необходимые библиотеки

CurrentWays = ['↓', '↑', '→', '←']  # Возможные ходы
IsWin = False  # Выиграл ли пользователь
WinBoard = [  # Выигрышная доска
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12',
    '13', '14', '15', '□'
]
Board = [  # Текущая доска
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12',
    '13', '14', '15', '□'
]


def GenerateBoard():  # Метод генерации доски
    global Board  # Задаем глобальную переменную

    steps = []  # Возможные ходы для квадрата
    b = Board.index('□')  # Получает индекс квадрата
    c = b // 4  # Получаем номер строки, на которой находится квадрат

    if b + 1 < (c + 1) * 4:  # Проверяем возможные ходы
        steps.append('r')  # Если ход возможен, то записываем его
    if b - 1 >= c * 4:
        steps.append('l')
    if b + 4 < 16:
        steps.append('d')
    if b - 4 > -1:
        steps.append('u')

    d = random.randint(0, len(steps) - 1)  # Выбираем случайный из найденных ход
    if steps[d] == 'r':  # Ищем выбранный ход
        MoveRight()
    elif steps[d] == 'l':
        MoveLeft()
    elif steps[d] == 'u':
        MoveUp()
    else:
        MoveDown()


def MoveToStart():  # Метод перемещения квадрата в начальную позицию (справа снизу)
    global Board  # Задаем глобальную переменную

    b = Board.index('□')  # Находим индекс квадрата
    while b + 4 < 16:  # Пока возможно двигаться вниз
        MoveDown()
        b += 4  # Задаем новый индекс квадрата
    while b + 1 < 16:  # Пока возможно двигаться вправо
        MoveRight()
        b += 1  # Задаем новый индекс квадрата


def PrintBoard():  # Метод вывода доски
    print('\nИгра "Пятнашки"')  # Выводим название игры
    for i in range(4):  # Цикл по строкам
        for j in range(4):  # Цикл по столбцам
            a = Board[i * 4 + j]  # Получаем символ на текущей позиции
            print(a + ' ' * (2 - len(a)), end=' ')  # Выводим текущий символ. Если символ один, то к нему добавляется пробел
        print()  # Разделяем строки


def MoveLeft():  # Метод движения квадрата влево
        a = Board.index('□')  # Получаем индекс квадрата
        Board[a] = Board[a - 1]  # Меняем символы местами
        Board[a - 1] = '□'


def MoveRight():  # Метод движения квадрата вправо
        a = Board.index('□')  # Получаем индекс квадрата
        Board[a] = Board[a + 1]  # Меняем символы местами
        Board[a + 1] = '□'


def MoveUp():
        a = Board.index('□')  # Получаем индекс квадрата
        Board[a] = Board[a - 4]  # Меняем символы местами
        Board[a - 4] = '□'


def MoveDown():
        a = Board.index('□')  # Получаем индекс квадрата
        Board[a] = Board[a + 4]  # Меняем символы местами
        Board[a + 4] = '□'


def ind():
    return Board.index('□')


def MoveInLine(line: int, k: int, x: str):
    while k != WinBoard.index(x):
        while ind() > line:
            MoveUp()
        while ind() >= k + 4:
            MoveLeft()
        MoveUp()
        MoveRight()
        MoveDown()
        k = Board.index(x)
    MoveToStart()


def MoveInRight(line: int, k: int, x: str):
    while k > line:
        if ind() != 6 and ind() != 10 and ind() != 14:
            MoveLeft()
        while ind() > k - 4 - 1:
            MoveUp()
        MoveRight()
        MoveDown()
        k = Board.index(x)
    MoveToStart()


def MoveLastInLine(line: int, x: str):
    k = Board.index(x)
    while k != line:
        if k > line - 4 and k <= line:
            while (ind() // 4) * 4 > (k // 4) * 4:
                MoveUp()
            MoveLeft()
            MoveLeft()
            MoveLeft()
        elif k == 11:
            MoveLeft()
            MoveUp()
            MoveRight()
        else:
            while (ind() // 4) * 4 > (k // 4) * 4:
                MoveUp()
            MoveUp()
            while ind() > k - 4:
                MoveLeft()
            MoveDown()
        k = Board.index(x)
        MoveToStart()
        PrintBoard()
def MoveForLine(line: int):
    return True


def Game():
    global IsWin  # Задаем глобальную переменную

    for i in range(1000):  # Делаем тысячу перестановок на доске
        GenerateBoard()  # Вызывая метод генерации доски
    MoveToStart()  # Запускаем метод перемещения квадрата в начальное положение

    PrintBoard()  # Выводим доску

    for i in range(1, 4):
        k = Board.index(str(i))
        while k != i - 1:
            if k < 4:
                MoveInLine(7, k, str(i))
            elif k == 7 or k == 11:
                MoveInRight(3, k, str(i))
            elif k == 15:
                MoveUp()
                MoveRight()
                MoveDown()
            else:
                while (ind() // 4) * 4 > (k // 4) * 4:
                    MoveUp()
                MoveLeft()
                MoveLeft()
                MoveLeft()
                if k > 11:
                    MoveUp()
                    MoveRight()
                    MoveRight()
                    MoveRight()
                MoveToStart()
            k = Board.index(str(i))
        PrintBoard()

    MoveLastInLine(7, '4')

    if Board[3] != '4':
        MoveForLine(7)


Game()  # Запускаем игру
# for i in range(1000):
#     try:
#         Game()
#         if Board[0] != '1' or Board[1] != '2' or Board[2] != '3':
#             print('ERROR1')
#             break
#     except:
#         print('ERROR')
#         break
