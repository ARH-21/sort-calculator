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
    pass

def heap_sort(arr):
   pass
