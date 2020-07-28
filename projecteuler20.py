def fact(n): 
    ans = 1
    for i in range(1, n+1): 
        ans *= i
    return (ans)
x = str(fact(100))
ans = 0
for d in x: 
    ans += int(d)
print(ans)
