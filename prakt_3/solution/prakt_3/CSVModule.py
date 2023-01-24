import csv  # Подключение библиотеки для работы с csv файлами
import GetColumnsTypes  # Подключаем модуль получения типа данных столбцов


def convert_to_dict(raw_data):  # Функция конвертации данных из списка в словарь
    complete_data = []  # Полученные словари в списке

    for value in raw_data[1:]:  # Цикл по строкам данных
        complete_dict = dict(zip(raw_data[0], value))  # Создаем словарь
        complete_data.append(complete_dict)  # Записываем словарь

    return complete_data  # Возвращаем полученный словарь


def save_table(data, max_rows=0, *files):  # Функция сохранения данных в файл
    try:  # Пробуем выполнить сохранение данных
        if max_rows != 0:  # Если нужно разбивать на файлы
            files = list(*files)  # Превращаем полученные файлы в список для работы с ними

            if max_rows < 0 or len(data[1:]) // max_rows > len(files):  # Если не получится разбить таблицу на файлы
                0 / 0  # Вызываем ошибку для выхода

            names = data[0]  # Названия столбцов
            del data[0]  # Удаляем названия столбцов

            complete_data = []  # Отформатированные дынные
            for i in files:  # Цикл по кол-ву файлов
                a = []  # Данные для текущего файла
                for j in range(min(max_rows, len(data))):  # Цикл от 0 до длины списка данных или до максимального числа строк в файле
                    a.append(data[0])  # Сохраняем первый элемент
                    del data[0]  # Удаляем первый элемент в списке данных
                complete_data.append(a)  # Сохраняем данные для текущего файла

            if [] in complete_data or len(data) > 0:  # Если есть файл с пустыми данными или остались данные
                0 / 0  # Вызываем ошибку для выхода

            for i in range(len(complete_data)):  # Цикл по кол-ву файлов
                file = open(files[i] + '.csv', 'w')  # Создаем или открываем файл

                data = convert_to_dict([names] + complete_data[i])  # Конвертируем данные в словарь
                writer = csv.DictWriter(file, delimiter=';',
                                        fieldnames=list(data[0].keys()))  # Создаем объект для записи данных в файл
                writer.writeheader()  # Записываем названия столбцов

                for row in data:  # Цикл по данным
                    writer.writerow(row)  # Записываем текущую строку

                file.close()  # Закрываем файл
        else:
            file = open(files[0][0] + '.csv', 'w')  # Создаем или открываем файл

            data = convert_to_dict(data)  # Конвертируем данные в словарь
            writer = csv.DictWriter(file, delimiter=';',
                                    fieldnames=list(data[0].keys()))  # Создаем объект для записи данных в файл
            writer.writeheader()  # Записываем названия столбцов

            for row in data:  # Цикл по данным
                writer.writerow(row)  # Записываем текущую строку

            file.close()  # Закрываем файл

        return True  # Если все получилось, возвращаем True
    except:  # Если не удалось выполнить сохранение данных
        return False  # Возвращаем False


def load_table(types=False, *filenames):  # Функция импорта данных из файла
    try:  # Пробуем получить данные из файла
        filenames = list(*filenames)  # Превращаем полученные файлы в список для работы с ними
        complete_data = []  # Полученные данные

        for i in filenames:  # Цикл по файлам
            file = open(i + '.csv', 'r')  # Открываем файл

            reader = csv.DictReader(file, delimiter=';')  # Создаем объект для чтения данных из файла

            for i, line in enumerate(reader):  # Цикл по строкам файла
                if i == 0:  # Если список полученных данных пуст, то есть получаем первую строку
                    names = list(line.keys())  # Получаем первую строку

                    if complete_data == []:  # Если список полученных данных пуст
                        complete_data.append(names)  # Записываем название столбцов, так как это первая строка
                    elif complete_data[0] != names:  # Если в списке уже есть значения и
                        # текущие названия столбцов не равны уже сохраненным
                        0 / 0  # Вызываем ошибку для выхода

                value = list(line.values())  # Текущая строка
                if value not in complete_data:  # Если такой строкаи нет в полученных данных
                    complete_data.append(value)  # Сохраняем текущую строку

            file.close()  # Закрываем файл

        if types:  # Если нужно вернуть данные с типами данных столбцов
            a = GetColumnsTypes.get_column_types(complete_data, False)  # Получаем типы данных столбцов
            complete_data = [a] + complete_data  # Записываем их в начало списка
        else:  # Иначе
            complete_data = [0] + complete_data  # Добавляем ноль - разделитель

        return complete_data  # Возвращаем полученные данные
    except:  # Если не получилось импортировать данные из файла
        return False  # Возвращаем False


# raw_data = [
#     'fname sname date'.split(),
#     'Ivan Petrov 03.04.2003'.split(),
#     'Petr Ivanov 15.09.2019'.split(),
#     'Vadim Vasilyev 10.03.1989'.split()
# ]

# complete_data = []
#
# for value in raw_data[1:]:
#     complete_dict = dict(zip(raw_data[0], value))
#     complete_data.append(complete_dict)

# name = 'testdate'
#
# save_table(raw_data, 0, [name])
# save_table(complete_data, 2, 'test1', 'test2')
# save_table(complete_data, 3, 'test4')

# print(False, load_table(name))
# print(load_table(False, 'test1', 'test2'))
# print(load_table(False, 'test1', 'test2', 'test4'))
