# Counter Variables
# Swap = 0 (which number is bigger), Comps = 0 (how many times the number is moved/swapped)
# Copy() so every time button is pressed it has the original data

def bubble_sort(arr):
    a = arr.copy()
    n = len(arr)

    swaps = 0
    comps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return a, swaps, comps


def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    swaps = 0
    comps = 0

    for i in range(n):
        min_index = i 
        for j in range(i + 1, n):
            comps += 1

            if a[j] < a[min_index]:
                min_index = j
        
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1
    
    return a, swaps, comps


def insertion_sort(arr):
    a = arr.copy()
    n = len(a)

    swaps = 0
    comps = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            comps += 1 # Increment if comparison is made (tracking)
            a[j + 1] = a[j] 
            swaps += 1 # Increment count if shift "moves"
            j -= 1

        # Final comparison check if the loop stops
        if j >= 0:
            comps += 1

        a[j + 1] = key
        swaps += 1 # The key placement is a move so it is counted
    
    return a, swaps, comps

# The other 3 sorts have nested functions so they can be imported easier to the other
def merge_sort(arr):
    def merge(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr, 0, 0  
        
        mid = len(sub_arr) // 2

        # Swaps and Comps need to be tracked here as well
        left, left_swaps, left_comps = merge(sub_arr[:mid])
        right, right_swaps, right_comps = merge(sub_arr[mid:])
        
        merged = []
        i = j = 0
        swaps = left_swaps + right_swaps
        comps = left_comps + right_comps
        
        while i < len(left) and j < len(right):
            comps += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            swaps += 1  
        
        while i < len(left):
            merged.append(left[i])
            swaps += 1
            i += 1
        while j < len(right):
            merged.append(right[j])
            swaps += 1
            j += 1
        
        return merged, swaps, comps
    
    sorted_arr, swaps, comps = merge(arr.copy())
    return sorted_arr, swaps, comps
        

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr.copy(), 0, 0
    
    a = arr.copy()
    swaps = 0
    comps = 0

    def quick_sort_dc(sub_arr, low, high, swaps, comps):
        if low < high:
            pivot_index, swaps, comps = partition(sub_arr, low, high, swaps, comps)
            swaps, comps = quick_sort_dc(sub_arr, low, pivot_index - 1, swaps, comps)
            swaps, comps = quick_sort_dc(sub_arr, pivot_index + 1, high, swaps, comps)
        return swaps, comps

    def partition(sub_arr, low, high, swaps, comps):
        pivot = sub_arr[high]
        i = low - 1

        for j in range(low, high):
            comps += 1
            if sub_arr[j] <= pivot:
                i += 1
                if i != j: 
                    sub_arr[i], sub_arr[j] = sub_arr[j], sub_arr[i]
                    swaps += 1

     
        i += 1
        if i != high:  
            sub_arr[i], sub_arr[high] = sub_arr[high], sub_arr[i]
            swaps += 1

        return i, swaps, comps

    swaps, comps = quick_sort_dc(a, 0, len(a) - 1, swaps, comps)
    return a, swaps, comps


def heap_sort(arr):
    def heapify(sub_arr, n, i, swaps, comps):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2


        if left < n:
            comps += 1
            if sub_arr[left] > sub_arr[largest]:
                largest = left


        if right < n:
            comps += 1
            if sub_arr[right] > sub_arr[largest]:
                largest = right

        
        if largest != i:
            sub_arr[i], sub_arr[largest] = sub_arr[largest], sub_arr[i]
            swaps += 1
            swaps, comps = heapify(sub_arr, n, largest, swaps, comps)

        return swaps, comps

    a = arr.copy()
    n = len(a)
    swaps = 0
    comps = 0

    # max heap
    for i in range(n // 2 - 1, -1, -1):
        swaps, comps = heapify(a, n, i, swaps, comps)

    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        swaps += 1
        swaps, comps = heapify(a, i, 0, swaps, comps)

    return a, swaps, comps
