# read text file and sort
# copy() save original unsorted data for each press

# need to add moves and comparisons

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(arr)

    # Track Moves

    # Swaps (moves) (Which is bigger number)
    swaps = 0

    # Comps (How many times number is moved)
    comps = 0

    for i in range(n):
        for j in range(0, n - i - 1):

            comps += 1

            if a[j] > a[j + 1]:
                # swap the elements
                a[j], a[j + 1] = a[j + 1], a[j]
                
                swaps += 1

        return a, swaps, comps

# if 5 > 8 no swap
# if 8 > 5 swap


# Selection Sort

def selection_sort(arr):
    a = arr.copy()
    swaps = 0
    comps = 0
    n = len(a)

    for i in range(n):
        min_index = i 

        for j in range(i + 1, n):
            comps += 1

            if a[j] < a[min_index]:
                min_index = j
        
        if min_index != i:
            (a[i], a[min_index]) = (a[min_index], a[i])
            swaps += 1
    
    return a, swaps, comps


# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    swaps = 0
    comps = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        comps += 1

        while j >= 0 and key < a[j]:
            # shift elements to the right
            a[j + 1] = a[j]
            
            swaps += 1
            j -= 1

            if j >= 0:
                comps += 1

        a[j + 1] = key
        moves += 1
    
    return a, swaps, comps
        


# Merge Sort

def merge_sort(arr):
    pass


# Quicksort

def quick_sort(arr):
    pass


# Heapsort
def heapsort(arr):
    pass

