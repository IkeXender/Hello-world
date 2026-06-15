plainText = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))

encryptedText = ""

for ch in plainText:
    code = ord(ch)

    code = code + distance

    while code > 126:
        code = 32 + (code - 127)

    encryptedText += chr(code)

print("Encrypted text:", encryptedText)
