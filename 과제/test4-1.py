import os

def file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        numbered_lines = []
        for index, line in enumerate(lines, start=1):
            formatted_line = f"{index} {line.rstrip('\n')}"
            numbered_lines.append(formatted_line)
            print(formatted_line)

        base_name, _ = os.path.splitext(file_path)
        sav_filename = f"{base_name}.sav"

        with open(sav_filename, "w") as sav_file:
            for line in numbered_lines:
                sav_file.write(line + "\n")
        print(f"\n[저장 완료: {sav_filename}]")
        return True

    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return False

def main():
    while True:
        user = input(
            "읽을 파일명을 입력(종료하려면 'q' 입력): "
        ).strip()

        if user.lower() == "q":
            print("프로그램을 종료합니다.")
            break

        success = file(user)
        if success:
            break
        else:
            print("다시 시도해주세요.\n")

if __name__ == "__main__":
    main()