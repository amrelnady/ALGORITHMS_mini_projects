import random
import time

# Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Test different input sizes
sizes = [100, 500, 1000, 2000]

for size in sizes:

    numbers = []

    for i in range(size):
        numbers.append(random.randint(1, 10000))

    start = time.perf_counter()

    insertion_sort(numbers)

    end = time.perf_counter()

    print("Array Size:", size)
    print("Execution Time:", round(end - start, 6), "seconds")
    print("-------------------------")