import random, os  # Подключаем необходимые библиотеки

Letters = 'abcdefgh'  # Возможные ходы по вертикали
Numbers = '12345678'  # Возможные ходы по горизонтали

Board = ['-'] * 64  # Доска
Player = False  # False - первый игрок, True - второй игрок
IsWin = False  # Выиграл ли кто-то
PlayerWin = 0  # Победивший игрок


def RestartGame():  # Метод перезапуска игры
    global Board, Player, IsWin, PlayerWin  # Задаем глобальные переменные

    Board = ['-'] * 64  # Очищаем доску
    Player = False  # Даем первый ход первому игроку
    IsWin = False  # В начале игры никто не выиграл
    PlayerWin = 0  # То никакой игрок не выиграл


def PrintBoard():  # Метод вывода доски
    print('\nИгра "Супер ним"')  # Вывод названия игры
    print('  a b c d e f g h')  # Вывод навигационного текста
    for i in range(8):  # Цикл от 0 до 7 для прохода по строкам
        print(str(i + 1), end=' ')  # Выводим навигационный текста (цифры от 1 до 8)
        for j in range(8):  # Цикл от 0 до 7 для прохода по столбцам
            print(Board[i * 8 + j], end=' ')  # Выводим текущий элемент с пробелом в конце
        print()  # Разделяем строки
    print()  # Разделяем доску и другой текст


def GenerateBoard():  # Метод генерации доски со случайным кол-ом фишек
    for i in range(random.randint(20, 60) + 1):  # Цикл от 0 до случайного числа (от 20 до 60)
        a = random.randint(0, 63)  # Выбираем случайный индекс (место) для текущей фишки
        while Board[a] == '*':  # Пока выбранное место занято
            a = random.randint(0, 63)  # Заново выбираем индекс
        Board[a] = '*'  # После нахождения свободного места записываем в него фишку


def PrintOrder():  # Метод вывода номера игрока, который сейчас ходит
    global IsWin, Player, PlayerWin  # Задаем глобальные переменные

    if not IsWin:  # Если игра продолжается
        a = 1  # Номер игрока, который сейчас ходит (по умолчанию - 1)
        if Player:  # Если же сейчас ходит второй игрок
            a = 2  # То записываем это
        print('Ходит игрок', a)  # Выводим номер игрока, который ходит
        print('Выберите букву или цифру (вертикаль или горизонталь соответственно): ',
              end='')  # Выводим сообщение, в котором просим пользователя ввести свой ход
    else:  # Если какой-то игрок уже выиграл
        print('Игра завершена\nПобедил игрок', PlayerWin)  # То выводим соотв. сообщение и номер победившего игрока


def CheckWin():  # Функция проверки выигрыша
    for i in Board:  # Цикл по всем элементам доски
        if i == '*':  # Если нашлась хотя бы одна фишка
            return False  # То игра еще идет
    else:  # Если за весь цикл не нашлась фишка
        return True  # То игра закончилась


def Game():  # Основной метод игры
    global IsWin, Player, PlayerWin  # Задаем глобальные переменные

    PrintBoard()  # Выводим доску

    while True:  # Бесконечный цикл для начала игры
        # a = 'да'
        a = input('Начинаем игру? (y - да, n - нет)\n')  # Спрашиваем пользователя о начале игры
        if a.lower() == 'y':  # Если пользователь ввел символ для начала игры
            os.system('cls')  # Очищаем консоль
            GenerateBoard()  # Генерируем доску
            PrintBoard()  # Выводим полученную доску
            break  # Останавливаем цикл while
        elif a.lower() == 'n':  # Если пользователь не хочет играть и вводит соотв. символ
            print(':(')  # Выводим соотв. сообщение
            input('Для выхода из программы нажмите "Enter" на клавиатуре')  # Ждем нового ввода, чтобы программа сразу не закрывалась и пользователь мог все прочитать
            exit()  # Выходим из программы
        else:  # Если вводится другой символ или строка
            print('Неправильный ввод! Можно ввести только "y" - да или "n" - нет',
                  end='\n\n')  # То выводим соотв. сообщение

    PrintOrder()  # После вывода доски выводим номер игрока, который сейчас ходит

    while not IsWin:  # Пока никто не выиграл
        a = input()  # Получаем ход игрока
        IsCorrectInput = False  # Переменная для определения корректности ввода
        if a in Letters:  # Если полученный ход - это заранее заданная буква
            b = Letters.index(a)  # Получаем индекс этой буквы в алфавите
            for i in range(8):  # Цикл от 0 до 7 для прохода по столбцу
                Board[i * 8 + b] = '-'  # Убираем фишки с вертикали
            IsCorrectInput = True  # Значит получен корректный ввод
        elif a in Numbers:  # Если полученный ход - это заранее заданная цифра
            for i in range(8):  # Цикл от 0 до 7 для прохода по строке
                Board[(int(a) - 1) * 8 + i] = '-'  # Убираем фишки с горизонтали
            IsCorrectInput = True  # Значит получен корректный ввод
        else:  # Если получен неизвестный символ
            print('Неправильный ввод! Можно ввести только буквы "a-h" и цифры "1-8"')  # Выводим соотв. сообщение и возможные ходы
            PrintOrder()  # Снова выводим кто сейчас ходит

        if IsCorrectInput:  # Если был получен корректный ввод
            os.system('cls')  # Очищаем консоль
            PrintBoard()  # Выводим полученную доску
            IsWin = CheckWin()  # Проверяем выиграл ли какой-то игрок и записываем это в глобальную переменную
            if IsWin:  # Если игра закончена
                PlayerWin = 1  # Сохраняем выигравшего игрока (по умолчанию - 1)
                if Player:  # Если ходил второй игрок, то он выиграл
                    PlayerWin = 2  # Записываем номер второго игрока

                PrintOrder()  # Выводим номер игрока, который будет ходить или выигравшего игрока

                a = input('Начать новую игру? (y - да, n - нет) ')  # Спрашиваем пользователя о начале новой игры
                if a == 'y':  # Если пользователь вводит символ старта новой игры
                    os.system('cls')  # Очищаем консоль
                    RestartGame()  # Запускаем метод перезапуска игры
                    Game()  # Заново начинаем игру
                else:  # Если пользователь ввел что-то другое
                    print(':(')  # Выводим соотв. сообщение
                    input('Для выхода из программы нажмите "Enter" на клавиатуре')  # Ждем ввода пользователя, чтобы он мог прочитать что-то
            else:  # Если еще остались фишки
                Player = not Player  # Передаем ход другому игроку
                PrintOrder()  # Выводим номер игрока, который будет ходить или выигравшего игрока



Game()  # Начинаем игру
