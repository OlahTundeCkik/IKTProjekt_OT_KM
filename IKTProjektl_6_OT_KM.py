# Oláh Tünde, Kiss Marcell 10/B
#Python első beadandó
n = 8
t = [27.3, 26.8, 25.7, 26.3, 27.3, 27.2, 27, 27.3]
max_ho = t[0] 
max_szam = 1   
for i in t[1:]:  
    if i > max_ho:
        max_ho = i    
        max_szam = 1  
    elif i == max_ho:
        max_szam += 1

print(max_szam, "alkalommal.")


n1 = 8
t1 = [27.3, 30.2, 19.2, 26.3, 27.3, 27.2, 27, 10.2]
legkisebb = t1[0]  
legnagyobb = t1[0]  
for i in t1:
    if i < legkisebb:
        legkisebb = i 
    if i > legnagyobb:
        legnagyobb = i
terjedelem = legnagyobb - legkisebb
print(int(terjedelem),".")


t2 = [27.3, 30.2, 19.2, 26.3, 27.3, 27.2, 27, 10.2]
összesen = 0
szam1 = 0
for i in t2: 
    összesen += i  
    szam1 += 1  
átlag = összesen / szam1
átlagalatt = 0
átlagfelett = 0
for i in t2:  
    if i < átlag:
        átlagalatt += 1  
    elif i > átlag:
        átlagfelett += 1  
if átlagfelett > átlagalatt:
    print("Az átlagnál nagyobb elemekből van több.")
elif átlagalatt > átlagfelett:
    print("Az átlagnál kisebb elemekből van több.")
else:
    print("Az átlagnál kisebb és nagyobb elemek száma egyenlő.")


