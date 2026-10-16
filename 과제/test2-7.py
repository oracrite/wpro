import random

word_list = ["hangman", "python", "computer", "developer", "algorithm"]

while True:
    secret_word = random.choice(word_list)
    word_length = len(secret_word)

    hidden_word = ["_" for _ in range(word_length)]

    trials = 6
    is_success = False

    print(f"새로운 게임을 시작합니다! (기회: {trials}번)")

    # 한 판의 게임 진행 반복문
    while trials > 0:
        print(" ".join(hidden_word))

        guess = input("글자를 입력하세요: ").lower()

        if len(guess) != 1:
            print("한 글자만 입력해주세요.")
            continue

        if guess in secret_word:
            print(f"Good! '{guess}'가 포함되어 있습니다.")
            for i in range(word_length):
                if secret_word[i] == guess:
                    hidden_word[i] = guess
        else:
            trials -= 1
            print(f"Nope! {trials} trials left")

        print("-" * 25)

        if "_" not in hidden_word:
            print(" ".join(hidden_word))
            print("Good Job!")
            is_success = True
            break

    if not is_success:
        print(f"Fail! 정답은 '{secret_word}'였습니다.")

    choice = input("\n게임을 다시 하시겠습니까? (y/n): ").lower()
    if choice != 'y':
        print("게임을 종료합니다.")
        break