import random
import string

len_password = 8

def passw ():
    pw = ""
    for x in range(len_password):
        pw += random.choice(string.ascii_letters + string.digits + "_")
    return pw

print(passw())
