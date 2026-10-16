def min_max(numbers):
    if not numbers:
        return None, None
    return (min(numbers), max(numbers))

def main():
    value_input = input()
    numbers = [int(x) for x in value_input.split()]
    value = min_max(numbers)
    print(value)

if __name__ == "__main__":
    main()