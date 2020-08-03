import math
a = []
s = set()
for i in range(1, 28124): 
    d = 1;
    for j in range(2, int(math.sqrt(i))+1): 
        if (i % j == 0): 
            d += j
            if (j != i / j):
                d += int(i / j)
    
    if (d > i): 
        a.append(i)
        s.add(i)
ans = 0
for i in range(1, 28124): 
    j = 0
    f = False
    while(j < len(a) and a[j] < i ): 
        if ((i - a[j]) in s): 
            f = True
            break
        j += 1
    if (f == False): 
        ans += i
print(ans)
