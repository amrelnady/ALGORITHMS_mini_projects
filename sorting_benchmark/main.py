import random
import time

# Generate random numbers
numbers = [random.randint(1, 1000) for _ in range(1000)]

# Copy the list
arr = numbers.copy()

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Measure execution time
start = time.perf_counter()

insertion_sort(arr)

end = time.perf_counter()

print("Insertion Sort Results")
print("Number of elements:", len(numbers))
print("Execution time:", end - start, "seconds")

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
 # Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
# Compare Sorting Algorithms

algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Python sorted()": sorted
}

print("\n===== Sorting Benchmark =====")

for name, algorithm in algorithms.items():

    arr = numbers.copy()

    start = time.perf_counter()

    algorithm(arr)

    end = time.perf_counter()

    execution_time = end - start

    print(name, ":", execution_time, "seconds")