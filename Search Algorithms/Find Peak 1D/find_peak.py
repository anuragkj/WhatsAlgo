def find_peak(l,r,arr):
    mid = (l+r)//2
    if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid]<arr[mid-1]:
        find_peak(l, mid-1, arr)
    else:
        find_peak(mid+1, r, arr)

#simple output could be to return the index of max element

l = int(input())
arr = list(map(int, input().split()))
if arr[0]>arr[1]:
    print(0)
elif arr[-1]>arr[-2]:
    print(len(arr)-1)
else:
    find_peak(l, len(arr)-1, arr)
