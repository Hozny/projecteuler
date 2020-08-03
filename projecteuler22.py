f = open("names.txt", "r")
x = str(f.read()).replace("\"","").replace("\n","").split(",")
x.sort()
ans = 0
 
for i in range(0, len(x)): 
    cur = 0
    for l in x[i]: 
        cur += (ord(l) - ord('A') + 1)
    ans += cur*(i+1)

print(x)
