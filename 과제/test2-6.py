for n in range(1, 101):
    if n < 2:
        continue
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(f"{n}은 소수입니다.")