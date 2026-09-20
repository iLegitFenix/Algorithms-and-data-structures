from random import randint

def QuickSort(arr, left, right):
    if left < right:
        middle = arr[randint(left, right)]
        i, j = left, right
        while i <= j:
            while arr[i] < middle:
                i += 1
            while arr[j] > middle:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j-= 1

        QuickSort(arr, left, j)
        QuickSort(arr, i, right)

        return arr
    else:
        return arr

n = int(input())
arr = list(map(int, input().split()))

print(* QuickSort(arr, 0, n-1))