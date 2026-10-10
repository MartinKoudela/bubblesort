import random


# Bubble sort
# Princip: prochází se pole a porovnávají se sousední prvky, když jsou ve
# špatném pořadí, prohodí se. Po každém průchodu je největší prvek na konci.
# Implementace: vnější cyklus počítá průchody, vnitřní jde jen po neseřazenou
# část (n - i - 1), protože konec už je seřazený. Třídím přímo v poli.
def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Quick sort
# Princip: vybere se pivot a pole se rozdělí na prvky menší/rovné pivotu
# (vlevo) a větší (vpravo). Pivot je pak na svém místě a stejně se rekurzivně
# seřadí obě části.
# Implementace: pivot volím náhodně, aby to nebylo pomalé na už seřazených
# datech, a dám ho na konec úseku. Pak jdu přes úsek a menší prvky přehazuju
# na začátek (index i). Nakonec pivot dám na pozici i a rekurzivně volám
# funkci na levou a pravou část. low a high určují, jaký úsek se třídí.
def quick_sort(arr: list[int], low: int = 0, high: int | None = None) -> None:
    if high is None:
        high = len(arr) - 1
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


# Merge sort
# Princip: pole se rozdělí na dvě poloviny, každá se rekurzivně seřadí
# a pak se obě seřazené poloviny slijí dohromady.
# Implementace: polovinu udělám přes slicing (left, right) a seřadím je.
# Při slévání porovnávám left[i] a right[j] a menší zapíšu zpátky do arr[k].
# Když jedna polovina dojde, zbytek druhé jen dokopíruju na konec.
def merge_sort(arr: list[int]) -> None:
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Selection sort
# Princip: v neseřazené části se najde nejmenší prvek a dá se na její
# začátek. Seřazená část tak roste zleva.
# Implementace: pro každou pozici i hledám ve zbytku pole index nejmenšího
# prvku (min_index) a pak ho prohodím s arr[i]. Poslední prvek už je
# na místě sám, proto cyklus jde jen do n - 1.
def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Insertion sort
# Princip: pole se bere prvek po prvku a každý se vloží na správné místo do už seřazené části vlevo.
# Implementace: aktuální prvek si uložím do key, pak posouvám větší prvky
# ze seřazené části o jedno doprava, dokud nenajdu místo, kam key patří.
# Začínám od indexu 1, protože jeden prvek je sám o sobě seřazený.
def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Heap sort
# Princip: z pole se udělá max-halda, největší prvek se prohodí na konec,
# halda se zmenší o jedna a opraví se. Opakuje se, dokud halda nezmizí.
# Implementace: děti prvku i jsou na 2 * i + 1 a 2 * i + 2. Vnořená funkce
# heapify posouvá prvek dolů, dokud není větší než jeho děti.
def heap_sort(arr: list[int]) -> None:
    def heapify(size: int, root: int) -> None:
        while True:
            largest = root
            for child in (2 * root + 1, 2 * root + 2):
                if child < size and arr[child] > arr[largest]:
                    largest = child
            if largest == root:
                return
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(end, 0)


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Heap Sort": heap_sort,
}
