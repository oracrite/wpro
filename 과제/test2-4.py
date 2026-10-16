for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n}은 3과 5의 배수입니다.")
    elif n % 3 == 0:
        print(f"{n}은 3의 배수입니다.")
    elif n % 5 == 0:
        print(f"{n}은 5의 배수입니다.")