import pickle  # Подключение библиотеки для работы с pkl файлами
import GetColumnsTypes  # Подключаем модуль получения типа данных столбцов

pickle.DEFAULT_PROTOCOL  # Устанавливаем стандартный протокол сериализации данных


def convert_to_dict(raw_data):  # Функция конвертации данных из списка в словарь
    # В этом методе сохранения файлов надо использовать словарь вида:
    # ключ: [все значения для этого ключа]

    complete_data = {}  # Полученный словарь

    for i in range(len(raw_data[0])):  # Цикл по столбцам
        value = []  # Текущая строка
        for j in raw_data[1:]:  # Цикл по строкам
            value.append(j[i])  # Добавляем нужный столбец
        complete_data[raw_data[0][i]] = value  # Сохраняем строку

    return complete_data  # Возвращаем полученный словарь


def save_table(data, max_rows, *filename):  # Функция сохранения данных в файл
    try:  # Пробуем выполнить сохранение данных
        filename = list(*filename)  # Превращаем полученные файлы в список для работы с ними
        if max_rows != 0:  # Если нужно разбивать на файлы
            if max_rows < 0 or len(data) // max_rows > len(filename):  # Если не получится разбить таблицу на файлы
                0 / 0  # Вызываем ошибку для выхода

            names = data[0]  # Названия столбцов
            del data[0]  # Удаляем названия столбцов

            complete_data = []  # Отформатированные дынные
            for i in filename:  # Цикл по кол-ву файлов
                a = []  # Данные для текущего файла
                for j in range(min(max_rows, len(data))):  # Цикл от 0 до длины списка данных или до максимального числа строк в файле
                    a.append(data[0])  # Сохраняем первый элемент
                    del data[0]  # Удаляем первый элемент в списке данных
                complete_data.append(a)  # Сохраняем данные для текущего файла

            if [] in complete_data or len(data) > 0:  # Если есть файл с пустыми данными или остались данные
                0 / 0  # Вызываем ошибку для выхода

            for i in range(len(complete_data)):  # Цикл по кол-ву файлов (через данные в файлах)
                file = open(filename[i] + '.pkl', 'wb')  # Открываем или создаем файл
                data = convert_to_dict([names] + complete_data[i])  # Конвертируем данные в словарь
                pickle.dump(data, file)  # Записываем данные в файл

                file.close()  # Закрываем файл
        else:
            file = open(filename[0] + '.pkl', 'wb')  # Открываем или создаем файл
            data = convert_to_dict(data)  # Конвертируем данные в словарь

            pickle.dump(data, file)  # Записываем данные в файл

            file.close()  # Закрываем файл

        return True  # Если все получилось, возвращаем True
    except:  # Если не удалось выполнить сохранение данных в файл
        return False  # Возвращаем False


def load_table(types=False, *filename):  # Функция импорта данных из файла
    try:  # Пробуем получить данные из файла
        filename = list(*filename)  # Превращаем полученные файлы в список для работы с ними
        complete_data = []  # Полученные данные

        for i in filename:  # Цикл по файлам
            file = open(i + '.pkl', 'rb')  # Открываем файл

            raw_data = pickle.load(file)  # Получаем данные из файла
            values = list(raw_data.values())  # Сохраняем значения в словаре данных

            if complete_data == []:  # Если еще не получены данные
                complete_data = [list(raw_data.keys())]  # Сначала сохраняем названия столбцов
            elif list(raw_data.keys()) != complete_data[0]:  # Если уже есть данные, то мы переходим к новому файлу
                # Если стобцы в новом файле отличаются от начального
                0 / 0  # То вызываем ошибку для выхода

            for i in range(len(values[0])):  # Цикл от 0 до кол-ва столбцов
                a = []  # Текущая строка
                for j in values:  # Цикл по значениям словаря данных
                    a.append(j[i])  # Добавляем нужный столбец строки
                complete_data.append(a)  # Сохраняем текущую строку

            file.close()  # Закрываем файл

        if types:  # Если нужно вернуть данные с типами данных столбцов
            a = GetColumnsTypes.get_column_types(complete_data, False)  # Получаем типы данных столбцов
            complete_data = [a] + complete_data  # Записываем их в начало списка
        else:  # Иначе
            complete_data = [0] + complete_data  # Добавляем ноль - разделитель

        return complete_data  # Возвращаем полученные данные
    except:  # Если не получилось импортировать данные из файла
        return False  # Возвращаем False


# raw_data = {
#     'fname': ['Ivan', 'Petr', 'Vadim'],
#     'sname': ['Petrov', 'Ivanov', 'Vasilyev'],
#     'city': ['Moscow', 'Saratov', 'Vladivostok']
# }
#
# name = 'test'

# complete_data = [
#     'fname sname city'.split(),
#     'Ivan Petrov Moscow'.split(),
#     'Petr Ivanov Saratov'.split(),
#     'Vadim Vasilyev Vladivostok'.split()
# ]
# name = 'test'
#
# save_table(complete_data, 2, 'test1', 'test2')
#
#
# save_table(complete_data, name)
# print(load_table(name))
