# Блок 1.9 Логические операции, операции сравнения
a = int(input())
print(a > 0)
#
a = int(input())
print(10 <= a < 100)
#
x1, x2, x3 = False, True, False
print(not x1 or x2 and x3)
#
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
#
a = True
b = False
print(a and b or not a and not b)
