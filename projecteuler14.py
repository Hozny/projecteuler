def collatz(n, c): 
    if (n == 1):
        return c
    if (n % 2 == 0):
        return collatz(n/2, c+1)
    return collatz(3*n + 1, c+1)
mx = 0
num = 0
for i in range(1, 10**6 + 1):
    t = collatz(i, 1)
    if (t > mx): 
        mx = t
        num = i
print(num)
