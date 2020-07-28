suf = ["hundred"]
dig = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
teen = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ans = 0
c = 0
for w in tens: 
    ans += len(w)
    c += 1
    for i in range(0, len(dig)-1): 
        d = dig[i]
        ans += len(w) + len(d)
        c += 1
chunk = ans
for w in dig: 
    ans += len(w)
for w in teen: 
    ans += len(w)

for h in dig: 
    if (h == "ten"): 
        break
    ans+=len(h)+len(suf[0])
    for w in dig: 
        ans += len(h) + len(suf[0]) + len("and") + len(w)
    for w in teen: 
        ans += len(h) + len(suf[0]) + len("and") + len(w)
    ans += (len(h)+len(suf[0])+len("and"))*c + chunk

ans += len("onethousand")

print(ans)
