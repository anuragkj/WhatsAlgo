def merge(l, mid, r, arr):
    i = l
    j = mid + 1
    k = 0
    ret = []
    
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            ret.append(arr[i])
            i += 1
        else:
            ret.append(arr[j])
            j += 1
    
    while i <= mid:
        ret.append(arr[i])
        i += 1
    
    while j <= r:
        ret.append(arr[j])
        j += 1
    
    arr[l:r+1] = ret


def merge_sort(l, r, arr):
    if(l>=r): return
    mid = (l+r)//2
    merge_sort(l, mid, arr)
    merge_sort(mid+1, r, arr)
    merge(l, mid, r, arr)

    return arr

arr = [2,1,4,3]
print(merge_sort(0,3,arr))