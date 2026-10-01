from backend import ALGORITHMS, generate_numbers, run_sort


def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def input_numbers() -> list[int]:
    nums: list[int] = []
    while True:
        entry = input("Enter a number (type 'done' to finish or 'random' to input random numbers): ")
        if entry.lower() == "done":
            break
        if entry.lower() == "random":
            count = input_int("How many random numbers? ")
            low = input_int("From: ")
            high = input_int("To: ")
            nums.extend(generate_numbers(count, low, high))
            print("Random numbers generated:", nums)
            break
        try:
            nums.append(int(entry))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return nums


def choose_algorithm() -> str:
    names = list(ALGORITHMS)
    options = ", ".join(f"{i + 1} for {name}" for i, name in enumerate(names))
    while True:
        choice = input_int(f"What sorting algorithm would you like to use? ({options}): ")
        if 1 <= choice <= len(names):
            return names[choice - 1]


def main() -> None:
    try:
        nums = input_numbers()
        algorithm = choose_algorithm()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return

    print(f"{algorithm} algorithm:")
    result = run_sort(algorithm, nums)
    print(f"Sorted in {result.seconds:.4f} s")
    print("Sorted numbers:", result.numbers)


if __name__ == "__main__":
    main()
