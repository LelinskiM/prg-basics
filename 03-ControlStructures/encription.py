###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
x=""
encrypted_text = ''
key = int(input("Enter the key: "))

for char in plain_text:
    # read the character's code (use ord())
    x = ord(char)
    # add one to the character's code
    if x!=32:
        x = x + key
        print(x)
        # replace new character code with its
        # corresponding character (use chr())
        x = chr(x)
        encrypted_text = encrypted_text + x
        # add encrypted character to encrypted text
        print(encrypted_text)
    else:
        x = chr(x)
        encrypted_text = encrypted_text + x

print(plain_text)
print(encrypted_text)
print(ord(" "))
