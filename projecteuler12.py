def divisors(a): 
    d = 2
    l = []
    while(a>1): 
        if(a%d==0): 
            r = 0
            while(a%d==0): 
                a /= d
                r += 1
            l.append(r)
        else: 
            d += 1
    ans = 1
    for x in l: 
        ans *= (x+1)
    return(ans)
cur = 1
i = 1
while (True): 
    if (divisors(cur) > 500): 
        break
    i+=1
    cur += i

print(cur)
