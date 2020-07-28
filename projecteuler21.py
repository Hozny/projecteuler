d = []
mx = 0
bang = 50000
for i in range(0, bang+1):
    s = 0
    for j in range(1, i):
        if (i % j == 0): 
            s += j
    d.append(s)
    mx = max(d[i], mx)

x = {}
for i in range(0, 10000):
    if (d[i] < bang and i == d[d[i]]):
        x[d[i]] = 1
ans = 0
for e in x: 
    print(e)
print(x)
print(ans)
