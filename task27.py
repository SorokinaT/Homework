import random

def create_list(lst):
    for i in range(11):
        lst += [random.randint(-1,1)]
    return lst

lst = []
print(create_list(lst))

def max_from_lst(lst):
    n = [0,0,0]
    for i in range(len(lst)):
        if lst[i] == -1:
            n[0] += 1
        elif lst[i] == 0:
            n[1] += 1
        else:
            n[2] += 1
    return n

print(max_from_lst(lst))


i = max_from_lst(lst)
max_from_i = max(i)
if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
    pass
elif max_from_i == i[0]:
    print("There are more '-1' in list %s: %d " % (lst, i[0]))
elif max_from_i == i[1]:
    print("There are more '0' in list %s: %d " % (lst, i[1]))
else:
    print("There are more '1' in list %s: %d " % (lst, i[2]))

