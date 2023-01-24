import GetColumnsTypes  # Подключаем модуль получения типа данных столбцов


def save_table(data, filename):  # Функция сохранения данных в файл
    try:  # Пробуем выполнить сохранение данных
        file = open(filename + '.txt', 'w+')  # Открываем или создаем файл
        file.write('')  # Очищаем файл
        file.close()  # Закрываем файл

        file = open(filename + '.txt', 'a')  # Открываем файл для добавления строк
        max_len = 0  # Максимальная длина столбца.
        for i in data:  # Цикл по данным
            for j in i:  # Цикл по столбцам данных
                if len(j) > max_len:  # Если найдена запись, которая больше предыдущей найденной
                    max_len = len(j)  # Сохраняем ее длину

        first = ''  # Названия столбцов
        for i in data[0]:  # Цикл по названиям столбцов
            first += i + ' ' * (max_len - len(i)) + '\t'  # Сохраняем текущее название и отступ
        first = first[:-1] + '\n'  # Убираем последний отступ и переносим на следующую строку
        file.write(first)  # Записываем названия столбцов

        for i in data[1:]:  # Цикл по строкам данных
            complete_data = ''  # Отформатированные данные
            for j in i:  # Цикл по элементам строки данных
                complete_data += j + ' ' * (max_len - len(j)) + '\t'  # Сохраняем элемент и отступ
            complete_data = complete_data[:-1] + '\n'  # Убираем последний отступ и переносим на следующую строку
            file.write(complete_data)  # Записываем строку

        file.close()  # Закрываем файл

        return True  # Если получилось сохранить данные, возвращаем True
    except:  # Если не удалось выполнить сохранение данных в файл
        return False  # Возвращает False


def load_table(types, filename):  # Функция импорта данных из файла
    try:  # Пробуем получить данные из файла
        file = open(filename + '.txt', 'r')  # Открываем файл

        raw_data = file.read().split('\n')  # Получаем строки из файла
        complete_data = []  # Полученные данные

        for i in raw_data:  # Цикл по считанным строкам
            data = i.replace('\t', '').split()  # Превращаем строку в список, убирая отступы
            complete_data.append(data)  # Сохраняем отформатированную строку

        while [] in complete_data:  # Если в полученных данных содержится пустой список
            del complete_data[complete_data.index([])]  # Удаляем его

        file.close()  # Закрываем файл

        if types:  # Если нужно вернуть данные с типами данных столбцов
            a = GetColumnsTypes.get_column_types(complete_data, False)  # Получаем типы данных столбцов
            complete_data = [a] + complete_data  # Записываем их в начало списка
        else:  # Иначе
            complete_data = [0] + complete_data  # Добавляем ноль - разделитель

        return complete_data  # Возвращаем полученные данные
    except:  # Если не удалось получить данные из файла
        return False  # Возвращаем False


# raw_data = [
#     'fname sname city'.split(),
#     'Ivan Petrov Moscow'.split(),
#     'Petr Ivanov Saratov'.split(),
#     'Vadim Vasilyev Vladivostok'.split()
# ]
# name = 'test'
#
#
# save_table(raw_data, name)
# print(load_table(name))
