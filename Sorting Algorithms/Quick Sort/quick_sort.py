#Partition method used is Hoare's since it has better avg time complexity
def partition(arr, low, high):
 
    pivot = arr[low]
    i = low - 1
    j = high + 1
 
    while (True):
 
        i += 1
        while (arr[i] < pivot):
            i += 1

        j -= 1
        while (arr[j] > pivot):
            j -= 1
 
        if (i >= j):
            return j
 
        arr[i], arr[j] = arr[j], arr[i]
 
 

def quickSort(arr, low, high):
    if (low < high): 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)
 
 
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
 