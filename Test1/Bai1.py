ocurr = [0]*1000000000
arr = []

n = int(input("Nhap so luong phan tu:"))
str = input().split(" ")
for i in range(n):
    x = int(int(str[i]))
    ocurr[x] += 1
    arr.append(x)
for num in arr:
    if ocurr[num]%5 == 0 and ocurr[num]%10 != 0:
        print(num, end = " ")
