def find_peak_2d(mat):
    row_top = 0
    row_bottom = len(mat)-1
    col_left = 0
    col_right = len(mat[0])-1

    while(row_top < row_bottom or col_left < col_right):
        if (row_bottom-row_top >= col_right-col_left):
            mid = row_top + (row_bottom-row_top)//2
            max = -1
            for i in range(col_left, col_right+1):
                if mat[mid][i]>max:
                    max = mat[mid][i]
                    pos = i
            if mat[mid][pos]>=mat[mid+1][pos]:
                row_bottom = mid
                continue
            else:
                row_top = mid+1
                continue
            
        else:
            mid = col_left + (col_right-col_left)//2
            max = -1
            for i in range(row_top,row_bottom+1):
                if(mat[i][mid] > max):
                    max = mat[i][mid]
                    pos = i
            if mat[pos][mid] >= mat[pos][mid+1]:
                col_right = mid
                continue
            else:
                col_left = mid + 1
                continue
    return row_bottom, col_right 



row, col = map(int, input().split())
mat = []
for i in range(row):
    mat.append(list(map(int, input().split())))
print(find_peak_2d(mat))