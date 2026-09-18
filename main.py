import random
import time

# TODO: tkinter GUI for input and output

nums = []

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_num():
    while True:
        try:
            entry = input("Enter a number (type 'done' to finish or 'random' to input random numbers): ")
            if entry.lower() == 'done':
                break
            if entry.lower() == 'random':
                count = input_int("How many random numbers? ")
                low = input_int("From: ")
                high = input_int("To: ")
                if low > high:
                    low, high = high, low
                nums.extend([random.randint(low, high) for _ in range(count)])
                print("Random numbers generated:", nums)
                break
            try:
                nums.append(int(entry))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break

def choose_sorting_algorithm():
    while True:
        try:
            choice = input_int("What sorting algorithm would you like to use? (1 for Bubble Sort, 2 for Quick Sort): ")
            start = time.perf_counter()
            if choice == 1:
                print("Bubble sort algorithm:")
                bubble_sort(nums)
            elif choice == 2:
                print("Quick sort algorithm:")
                quick_sort(nums, 0, len(nums) - 1)
            else:
                continue
            end = time.perf_counter()
            print(f"Sorted in {end - start:.4f} s")
            break
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)

input_num()

choose_sorting_algorithm()

print("Sorted numbers:", nums)