str = input()
ans = 0
tmp = ""
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
for i in range(0, len(str) + 1):
    if i == len(str) or str[i] not in number:
        if len(tmp) == 0: continue
        ans += int(tmp)
        tmp = ""
    else: 
        tmp += str[i]
print(ans)
