def count_vowel(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def main():
    value_input = input()
    value = count_vowel(value_input)
    print(value)

if __name__ == "__main__":
    main()