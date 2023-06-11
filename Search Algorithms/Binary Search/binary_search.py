def bin_search(l, r, target, arr):
    if(l == r):
        if(arr[l] == target):
            return l
        else:
            return -1
    else:
        mid = (l + r)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            return bin_search(l, mid-1, target, arr)
        else:
            return bin_search(mid+1, r, target, arr)



len, target = map(int,(input().split()))
arr = list(map(int,(input().split())))
print(bin_search(0, len-1, target, arr))