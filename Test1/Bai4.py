n = int(input('Nhap so luong phan tu: '))
arr = []
for i in range(n):
    tmp = input()
    for chara in tmp:
        arr.append(chara)

print(list(set(arr)))