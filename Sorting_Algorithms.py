def bucket_sort(arr):

    # Secondary sorting algorithm it uses
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            var = bucket[i]
            j = i - 1
            while j >= 0 and var < bucket[j]:
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var

    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket
    max_value = max(arr)
    size = max_value / len(arr)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list = []
    for x in range(len(arr)):
        buckets_list.append([])

    # Put list elements into different buckets based on the size
    for i in range(len(arr)):
        j = int(arr[i].height / size)
        if j != len(arr):
            buckets_list[j].append(arr[i].height)
        else:
            buckets_list[len(arr) - 1].append(arr[i].height)

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(arr)):
        insertion_sort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(arr)):
        final_output = final_output + buckets_list[x]
    return final_output


def selection_sort(arr):  # works, sorts bars
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx].height > arr[j].height:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# _______________QUICK SORT _______________
# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
