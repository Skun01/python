k = int(input())

i = 19
ans = 0
def totalNum(num):
    ans = 0
    while(num):
        ans += num%10
        num = int(num/10)
    return ans


while(k != 0):
    if(totalNum(i) == 10):
        k -=1
        ans = i
    i +=1
print(ans)



