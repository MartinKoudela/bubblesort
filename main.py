import random
import time

# TODO: tkinter GUI for input and output, implement quicksort

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
            if choice == 1:
                print("Bubble sort algorithm:")
                bubble_sort(nums)
                break
            if choice == 2:
                print("Quick sort algorithm:")
                quick_sort(nums)
                break
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break


def bubble_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.perf_counter()
    print(f"Bubble sort completed in {end - start:.4f} s")

def quick_sort(arr, low, high):
    start = time.perf_counter()




    end = time.perf_counter()
    print(f"Quick sort completed in {end - start:.4f} s")


input_num()

choose_sorting_algorithm()

print("Sorted numbers:", nums)