def Anagram(word):
    lst = [0] * 255
    for let in word:
        lst[ord(let)] += 1

    return lst


a = input()
b = input()

if Anagram(a) == Anagram(b):
    print('YES')
else:
    print('NO')