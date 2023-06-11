def linear_search(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

length, target = map(int,input().split())
arr = list(map(int, input().split()))
print(linear_search(target, arr))