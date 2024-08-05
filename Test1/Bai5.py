n = int(input())
strArr = input()
arr = strArr.split(" ")
for i in range(n):
    arr[i] = int(arr[i])
ans = 1
for num in arr:
    if num == ans:
        ans += 2
    else: ans += 1
print(ans - 1)