import random
import time

nums = []

def input_num():
    while True:
        try:
            entry = input("Enter a number (type 'done' to finish or 'random' to input random numbers): ")
            if entry.lower() == 'done':
                break
            if entry.lower() == 'random':
                nums.extend([random.randint(1, 100) for _ in range(10)])
                print("Random numbers generated:", nums)
                break
            try:
                nums.append(int(entry))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


input_num()

start = time.perf_counter()

bubble_sort(nums)

end = time.perf_counter()

print("Sorted numbers:", nums)
print(f"Sorted in {end - start:.4f} s")
