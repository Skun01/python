n = int(input())
ans = ""
minPoint = 1000000000

for i in range(n):
    str = input().split(" ")
    print(str)
    name = str[0]
    point = int(str[1])
    if point < minPoint:
        minPoint = point
        ans = name
print(ans)

# 5
# khanh 73
# hoang 51
# phuong 58
# duy 93
# hoa 81