def num_include(a,b):
    lst = []
    for i in range(0,1001):
        if str(a) in str(i) and str(b) in str(i):
            lst.append(i)
    return lst

a = 1
b = 7
print(num_include(a,b))

