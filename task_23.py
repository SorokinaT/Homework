
def avr_list(lst):
    sum_list = 0
    for i in range(len(lst)):
        sum_list = sum_list + lst[i]
    avr = sum_list/len(lst)
    return avr

lst = [1,264,35,50]
print(avr_list(lst))