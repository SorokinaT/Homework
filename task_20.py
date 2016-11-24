def sum_numbers_of_pow(a):
    accumulator = 0
    for i in range(0,1000000):
        if i%a==0:
            accumulator = accumulator + i
    return accumulator


a = 3
print("Sum of all the numbers that are powers of %d in range from 0 to 1000000 = %d" % (a,sum_numbers_of_pow((a))))

def sum_numbers_of_pow_(a, end_range):
    accumulator = 0
    power = 0
    number = 0
    while number<=end_range:
        number = pow(a, power)
        if number>end_range:
            continue
        accumulator = accumulator + number
        power = power + 1
    return accumulator

end_range = 1000000
print("Sum of all the numbers that are powers of %d in range from 0 to %d = %d" % (a, end_range, sum_numbers_of_pow_(a,end_range)))