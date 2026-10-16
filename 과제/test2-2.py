print("1. 명단 작성")
students = {}
while True:
    id = int(input("학번 입력(0: 종료): "))
    if id == '0':
        break

    name = input("이름 입력 ('None' 입력시 종료): ")
    if name == 'None':
        break

    students[id] = name

print(students)
print("\n2.학번으로 이름 출력하기")
while True:
    students_id = input("학번 입력 ('quit' 입력 시 종료): ")

    if students_id == 'quit':
        print("프로그램을 종료합니다.")
        break
    elif students_id in students:
        print(students[students_id])
    else:
        print("not found!")


