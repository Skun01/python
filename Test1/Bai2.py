goal = int(input())
step = int((goal - goal%3)/3)
remain = goal%3
step += 1 if remain%2 == 0 else remain
print(step) 