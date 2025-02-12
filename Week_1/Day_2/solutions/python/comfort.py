def hourglassSum(arr):
    # Write your code here
    sums_arr=[]
    for i in range(4):
        sums=[]
        for j in range(4):
            p1 = arr[i][j]
            p2 = arr[i][j+1]
            p3 = arr[i][j+2]
            p4 = arr[i+1][j+1]
            p5 = arr [i+2][j]
            p6 = arr[i+2][j+1]
            p7 = arr[i+2][j+2]
            sum = p1+p2+p3+p4+p5+p6+p7
            sums.append(sum)
        sums_arr.append(sums)
    max_sum = sums_arr[0][0]
    for i in sums_arr:
        for j in i:
            if j>max_sum:
                max_sum = j
    return max_sum
        
