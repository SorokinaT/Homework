
import random

random_num = random.randint(1,10)
# print(random_num)
n = int(input("Guess number from 1 to 10: " ))

if n==random_num:
    print("The correct number! :) ")
while n!=random_num:
    if n < random_num:
        print("More...")
    else:
        print("Less...")
    n = int(input("Guess number from 1 to 10: "))
    if n == random_num:
        print("Guessed :) ")

