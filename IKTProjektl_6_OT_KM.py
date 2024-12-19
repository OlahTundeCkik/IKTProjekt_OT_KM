n = 8
t = [27.3, 26.8, 25.7, 26.3, 27.3, 27.2, 27, 27.3]

max_ho = t[0]
max_szam = 0

for ho in t:
    if ho > max_ho:
        max_ho = ho
        max_szam = 1
    elif ho == max_ho:
        max_szam+=1

print(max_szam,"alkalommal.")