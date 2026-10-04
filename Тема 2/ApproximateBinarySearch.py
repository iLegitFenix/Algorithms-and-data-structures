def ApproximateBinarySearch(arr, num):
    left = -1
    right = len(arr)
    a, b = arr[0], arr[0]
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] == num:
            return arr[middle]
        elif arr[middle] < num:
            if right == len(arr):
                a, b = arr[middle], arr[middle]
            else:
                a, b = arr[middle], arr[middle+1]
            left = middle
        else:
            if left == -1:
                a, b = arr[middle], arr[middle]
            else:
                a, b = arr[middle-1], arr[middle]
            right = middle
            
    if abs(a - num) > abs(b - num):
        return b
    elif abs(a - num) == abs(b - num):
        return min(a, b)
    else:
        return a


n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for el in arr_k:
    print(ApproximateBinarySearch(arr_n, el))