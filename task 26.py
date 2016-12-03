import random

def create_list(lst):
    for i in range(5):
        random_num = [random.randint(0,5)]
        lst += random_num
    return lst

lst1 = []
lst2 = []

print(create_list(lst1))
print(create_list(lst2))

def average_lst(lst):
    accumulator = 0
    for i in range(len(lst)):
        accumulator = accumulator + lst[i]
    average_lst = accumulator/len(lst)
    return average_lst

if average_lst(lst1)>average_lst(lst2):
    print("The average of numbers of list 1 more than the average of numbers of list 2")
elif average_lst(lst1)<average_lst(lst2):
    print("The average of numbers of list 1 less than the average of numbers of list 2")
else:
    print("The average of numbers of list 1 is equal to the average of numbers of list 2")