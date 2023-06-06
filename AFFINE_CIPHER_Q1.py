def affine_encrypt(message, a, b):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                encrypted_char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message
def affine_decrypt(message, a, b):
    decrypted_message = ""
    mod_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            mod_inverse = i
            break
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((mod_inverse * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                decrypted_char = chr((mod_inverse * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


message = input("Enter the message:")
a = int(input("Enter the multiplicative key:"))
b = int(input("Enter the additive key:"))

encrypted_message = affine_encrypt(message, a, b)
print("Encrypted message:", encrypted_message)

decrypted_message = affine_decrypt(encrypted_message, a, b)
print("Decrypted message:", decrypted_message)