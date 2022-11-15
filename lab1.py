# 1. Гипотенуза
# a = int(input())
# b = int(input())
# c = a**2 + b**2
# print(c**0.5)

# 2.Число десятков
# a = int(input())
# a = a / 10 % 10
# print(int(a))

# 3. Следующее четное
# a = int(input())
# b = a % 2
# print(a - b + 2)

# 4. Конец уроков
# a = int(input())
# a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
# print(a // 60 + 9, a % 60)

# 5. Какое из чисел больше?
# a = int(input())
# b = int(input())
# if a > b:
#     print(1)
# elif a < b:
#     print(2)
# else:
#     print(0)

# 6. ​​Максимум из трех
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# 7. Ладья
# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
# if x1 == y1 or x2 == y2:
#     print('YES')
# else:
#     print('NO')

# 8. Существует ли треугольник?
# a = int(input())
# b = int(input())
# c = int(input())
# if a < b + c and b < a + c and c < b + a:
#     print('YES')
# else:
#     print('NO')

# 9. Количество равных из трех
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a == b or a == c or c == b:
#     print(2)
# else:
#     print(0)

# 10. Упорядочить три числа
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b: a, b = b, a
# if a > c: a, c = c, a
# if b > c: b, c = c, b
# print(a, b, c)

# ДОП ЗАДАЧИ
# 1.Тип треугольника
# a = int(input())
# b = int(input())
# c = int(input())
# max = a
# side1 = b
# side2 = c
# if max < b:
#     max = b
#     side1 = a
# if max < c:
#     max = c
#     side2 = b

# if max**2 == side1**2 + side2**2: print('right')
# elif max**2 > side1**2 + side2**2: print('obtuse')
# else: print('acute')

# 2. Квадратное уравнение
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2 - 4 * a * c
# answer1 = ((-b) + d**0.5) / (2 * a)
# answer2 = ((-b) - d**0.5) / (2 * a)
# if answer1 == answer2:
#     print(answer1)
# else:
#     print(f'answer 1: {answer1}')
#     print(f'answer 2: {answer2}')

# 3. Максимум
# a = int(input())
# b = int(input())
# print((a * (a // b) + b * (b // a)) / (b // a + a // b))