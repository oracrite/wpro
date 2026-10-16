import math

a, b, c = 3, 4, 5
value = 1 / (1 + a / b + c)
print(value)

a, b, c = 1, 1, -6
n = b**2 - 4 * a * c
r1 = (-b + math.sqrt(n)) / (2 * a)
r2 = (-b - math.sqrt(n)) / (2 * a)
print(r1, r2)

r = 5
area = math.pi * (r ** 2)
print(area)

b = 2.0
g = 3.2
value = b * math.exp(-g)
print(value)

x = 0
y = 1.5
p = 2.0

n1 = 1 / (p * math.sqrt(2 * math.pi))
n2 = math.exp(-((x - y) ** 2) / (2 * (p ** 2)))

value = n1 * n2
print(value)