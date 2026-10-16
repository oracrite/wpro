#1. input()을 두번사용+f스트링방식
a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

#2. input()을 한번사용+f스트링방식
x, y = map(int, input("정수를 입력하세요: ").split())

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} x {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

#3. input()을 두번사용+format방식
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} x {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))

#4. input()을 한번사용+format방식
n1, n2 = map(int, input("정수를 입력하세요: ").split())
print("{} + {} = {}".format(n1, n2, n1 + n2))
print("{} - {} = {}".format(n1, n2, n1 - n2))
print("{} x {} = {}".format(n1, n2, n1 * n2))
print("{} / {} = {}".format(n1, n2, n1 / n2))
