def file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            content = "".join(lines)

        num_lines = len(lines)

        words = content.split()
        num_words = len(words)

        num_chars = sum(1 for c in content if not c.isspace())

        print(f"characters : {num_chars}")
        print(f"words      : {num_words}")
        print(f"lines      : {num_lines}")

        return True

    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return False

def main():
    while True:
        file_input = input( "파일명을 입력(종료하려면 'q' 입력): ").strip()

        if file_input.lower() == "q":
            print("프로그램을 종료합니다.")
            break

        success = file(file_input)
        if success:
            break
        else:
            print("다시 시도해주세요.\n")

if __name__ == "__main__":
    main()