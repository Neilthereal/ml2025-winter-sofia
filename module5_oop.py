class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, count):
        print(f"Enter {count} numbers:")
        for i in range(count):
            while True:
                try:
                    number = int(input(f"Number {i + 1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Re-enter a valid integer.")

    def search_number(self, target):
        return self.numbers.index(target) + 1 if target in self.numbers else -1


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Input must be a positive integer.")
        except ValueError:
            print("Invalid input. You can enter a new valid integer.")


def main():
    n = get_positive_integer("Enter a positive integer N: ")
    processor = NumberProcessor()
    processor.read_numbers(n)
    x = int(input("Enter an integer X to search: "))
    print(processor.search_number(x))


if __name__ == "__main__":
    main()
