import random


lst = [i for i in range(1,100) if i%2]
print(lst)
random.shuffle(lst)
print(lst)
