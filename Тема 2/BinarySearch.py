def BinarySearch(arr, num):
    right = len(arr) - 1
    left = 0
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] != num:
            if num > arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            return True
        
    return False


n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for el in arr_k:
    if BinarySearch(arr_n, el):
        print('YES')
    else:
        print('NO')