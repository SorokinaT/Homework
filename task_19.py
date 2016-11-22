k = 0

for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            k = k + 1
    if k ==0:
        print(i)
    else:
        k = 0
