first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(item[0]) - len(item[1]) for item in list(zip(first, second)) if len(item[0]) != len(item[1]))
print(list(first_result))
second_result = (len(first[item]) == len(second[item]) for item in list(range(0, len(first))))
print(list(second_result))