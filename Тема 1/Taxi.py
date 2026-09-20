def Taxi(lst):
    for i in range(len(lst)):
        min_ind = i
        for j in range(i+1, len(lst)):
            if lst[min_ind] > lst[j]:
                min_ind = j
        lst[min_ind], lst[i] = lst[i], lst[min_ind]


dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

Taxi(dists)
Taxi(prices)

summ = 0
for i in range(1, len(prices)+1):
    summ += dists[i-1] * prices[-i]

print(summ)