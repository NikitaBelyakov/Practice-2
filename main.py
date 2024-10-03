import random

#                                               БЫКИ И КОРОВЫ
# digits = random.sample("1234567890",4)
# number = int("".join(digits))
# if number < 1000:
#     number = number * 10
#
# number_list = []
# for i_elem in str(number):
#     number_list.append(i_elem)
#
# steps = 1
# while True:
#     my_num = input('Введите число: ')
#     my_num_list = []
#     for i_elem in my_num:
#         my_num_list.append(i_elem)
#     if my_num_list == number_list:
#         print(f'Вы угадали! Использовано {steps} попыток.')
#         break
#     cow = 0
#     cow_list = []
#     for index in range(4):
#         if number_list[index] == my_num_list[index]:
#             cow += 1
#             cow_list.append(my_num_list[index])
#     bull = 0
#     for i_elem in my_num_list:
#         if i_elem in number_list and i_elem not in cow_list:
#             bull += 1
#     print(f'У вас {cow} коров(а/ы) и {bull} бык(ов/а)')
#     steps += 1



#                                                   5 БУКВ
# all_words = []
# with open('words.txt', 'r', encoding='utf-8') as words_file:
#     for i_line in words_file:
#         all_words.append(i_line)
#
# digit = random.randint(0, 58)
# secret_word_list = []
# for i_elem in all_words[digit]:
#     secret_word_list.append(i_elem)
# secret_word_list.remove(secret_word_list[-1])
#
# steps = 1
# while True:
#     my_word = input('Введите слово: ').lower()
#     my_word_list = []
#     for i_elem in my_word:
#         my_word_list.append(i_elem)
#     if my_word_list == secret_word_list:
#         print(f'Вы угадали! Использовано {steps} попыток.')
#         break
#     letter_list = []
#     for index in range(5):
#         if secret_word_list[index] == my_word_list[index]:
#             my_word_list[index] = f'[{secret_word_list[index]}]'
#             letter_list.append(my_word_list[index])
#     for i_elem in my_word_list:
#         if i_elem in secret_word_list and i_elem not in letter_list:
#             my_word_list[my_word_list.index(i_elem)] = f'({i_elem})'
#     print(f'Ваш результат: {my_word_list}')
#     steps += 1



#                                               К-Н-Б-Я-С
# list_of_sign = ['камень', 'ножницы', 'бумага']
#
# while True:
#     rand_cifer = random.randint(0, 2)
#     secret_sign = list_of_sign[rand_cifer]
#     my_sign = input('Камень-ножницы-бумага!: ').lower()
#     if my_sign == 'камень' and secret_sign == 'камень':
#         print('Хех, ничья)')
#     elif my_sign == 'ножницы' and secret_sign == 'камень':
#         print('Ха, ты проиграл!)')
#     elif my_sign == 'бумага' and secret_sign == 'камень':
#         print('Что ж, поздравляю с победой, кожаный.')
#     elif my_sign == 'камень' and secret_sign == 'ножницы':
#         print('Что ж, поздравляю с победой, кожаный.')
#     elif my_sign == 'бумага' and secret_sign == 'ножницы':
#         print('Ха, ты проиграл!')
#     elif my_sign == 'ножницы' and secret_sign == 'ножницы':
#         print('Хех, ничья)')
#     elif my_sign == 'бумага' and secret_sign == 'бумага':
#         print('Хех, ничья)')
#     elif my_sign == 'камень' and secret_sign == 'бумага':
#         print('Ха, ты проиграл!')
#     elif my_sign == 'ножницы' and secret_sign == 'бумага':
#         print('Что ж, поздравляю с победой, кожаный.')



#                                               Делители и простой число
# def func(x):
#     all_dev = []
#     for num in range(1, x+1):
#         if (x % num) == 0:
#             all_dev.append(num)
#
#     return all_dev
#
# digit = random.randint(0, 100000)
# our_deviders = func(digit)
# print(f'Наше число: {digit}\nЕго делители: {our_deviders}')
# if len(our_deviders) == 2:
#     print(f'{digit} - простое число.')