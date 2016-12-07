line = input("Enter the line for encrypt: ")
encryption_table = "abcdjk25947"

def encrypt(line):
    new_text = ''
    for i in range(len(line)):
        if line[i] in encryption_table:
            find_index = encryption_table.index(line[i])
            print(find_index)
            new_text = new_text + encryption_table[(find_index+5)%len(encryption_table)]
    return new_text

print("The encryption text is %s" % encrypt(line))

