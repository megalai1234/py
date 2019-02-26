def Series(n): 
    sums = 0.0
    for i in range(1, n + 1): 
        ser = 1 / (i**i) 
        sums += ser 
    return sums 
   
n = 3
res = round(Series(n), 5) 
print(res) 
