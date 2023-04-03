# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


# def print_operation_table(operation):
#     for i_col in range(1, 7):
#         for i_str in range(1, 7):
#             print(operation(i_col, i_str), end=' ')
#         print()

# print_operation_table(lambda x, y: x * y)

def print_operation_table(operation):
    for i_col in range(1, 7):
        row = ''
        for i_str in range(1, 7):
            value = operation(i_col, i_str)
            # Выравнивание по ширине поля в 4 символа
            row += '{:<4}'.format(value)
        print(row)

print_operation_table(lambda x, y: x * y)