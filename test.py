
# # Тестовые данные.
# TEST_DATA: list = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]


# BONUS: float = 1.1
# ANTIBONUS: float = 0.8


# def add_rep(current_rep, rep_points, buf_effect):
#     current_rep += rep_points
#     if buf_effect:
#         return current_rep * BONUS
#     return current_rep


# def remove_rep(current_rep, rep_points, debuf_effect):
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep


# def main(duel_res):
#     current_rep: float = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, '
#             f'репутация персонажа — {current_rep:.3f} очков.')



# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard. 


# """Документация модуля. Описывает работу классов и функций.
# Размещается в верхней части файла (начиная с первой строки).
# """
# # Импортируйте модуль inspect.
# import inspect


# def tricky_func(self):
#     """Описывает работу функции tricky_func."""
#     ...


# class Test:
#     """Класс Test используется для демонстрации docstring."""

#     def first(self):
#         """Описывает метод first и демонстрирует перенос строки
#         документации.
#         """
#         ...


# print('Без применения cleandoc:')
# print(Test.first.__doc__)
# print('С применением cleandoc:')
# # Выведите докстринг, используя метод cleandoc().
# print(inspect.cleandoc(Test.first.__doc__))


from math import sqrt

print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    '''Проверяет, чтобы число было больше 0 и выдаёт ответ в виде строки'''
    if your_number <= 0:
        return
    answer = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {calculate_square_root(answer)}')


calc(25.5)
