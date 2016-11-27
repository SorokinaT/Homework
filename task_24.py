
def sum_os_numbers(lst):
    sum_of_evens = 0
    sum_of_odd = 0
    for i in range(len(lst)):
        if lst[i]%2:
            sum_of_evens = sum_of_evens + lst[i]
        else:
            sum_of_odd = sum_of_odd + lst[i]
    diff = sum_of_evens - sum_of_odd
    return diff

lst = [5.25,10,1,3,9,4]
print("The difference sums of even and odd in lst %s = %.2f" % (lst, sum_os_numbers(lst)))
