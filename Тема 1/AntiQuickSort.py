def AntiQuickSort(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        arr = list(range(1, n+1))

        arr[1], arr[2] = arr[2], arr[1]
        for i in range(3, n):
            middle = i // 2
            arr[middle], arr[i] = arr[i], arr[middle]
        
        return arr


n = int(input())
arr = AntiQuickSort(n)
print(* arr)