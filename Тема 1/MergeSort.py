def MergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = MergeSort(arr[:middle])
        right = MergeSort(arr[middle:])

        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:] + right[j:]

        return result
    
    else:
        return arr


n = int(input())
arr = list(map(int, input().split()))

print(* MergeSort(arr))