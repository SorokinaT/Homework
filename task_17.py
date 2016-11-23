
def factorial_number(a):
    if a==0:
        result = 1
    else:
        result = a * factorial_number(a-1)
    return result

print(factorial_number(10))
