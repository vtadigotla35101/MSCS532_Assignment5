import sys
import random
import time

# --- Section 1: Deterministic Quicksort ---

def quicksort(arr):
    # It's good practice to increase the recursion limit
    sys.setrecursionlimit(20000)
    arr_copy = list(arr)
    _quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def _quicksort_helper(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quicksort_helper(arr, low, pi - 1)
        _quicksort_helper(arr, pi + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Section 2: Randomized Quicksort ---

def randomized_quicksort(arr):
    arr_copy = list(arr)
    _randomized_quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def _randomized_quicksort_helper(arr, low, high):
    if low < high:
        pi = _randomized_partition(arr, low, high)
        _randomized_quicksort_helper(arr, low, pi - 1)
        _randomized_quicksort_helper(arr, pi + 1, high)

def _randomized_partition(arr, low, high):
    rand_pivot_index = random.randint(low, high)
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]
    return _partition(arr, low, high)

# --- Section 3: Empirical Analysis and Execution ---

def run_sorting_experiment():
    sizes = [1000, 2000, 5000, 9999]
    print("="*70)
    print("             Quicksort Performance Analysis             ")
    print("="*70)

    for n in sizes:
        print(f"\n--- Running for input size n = {n} ---")
        
        # Generate the three types of datasets
        random_arr = [random.randint(0, n) for _ in range(n)]
        sorted_arr = list(range(n))
        reverse_sorted_arr = list(range(n, 0, -1))
        
        datasets = {
            "Random": random_arr,
            "Sorted": sorted_arr,
            "Reverse-Sorted": reverse_sorted_arr
        }

        for name, data in datasets.items():
            # Time deterministic quicksort
            start_time = time.time()
            try:
                quicksort(data)
                det_time = time.time() - start_time
            except RecursionError:
                det_time = float('inf') # Mark as failed due to recursion depth

            # Time randomized quicksort
            start_time = time.time()
            randomized_quicksort(data)
            rand_time = time.time() - start_time
            
            print(f"  Dataset: {name:<16} | Deterministic: {det_time:<10.6f}s | Randomized: {rand_time:<10.6f}s")
    print("="*70)

# This line makes the script runnable
if __name__ == "__main__":
    run_sorting_experiment()