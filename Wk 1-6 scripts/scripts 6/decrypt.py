encryptedText = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

plainText = ""

for ch in encryptedText:
    code = ord(ch)

    code = code - distance

    while code < 32:
        code = 127 - (32 - code)

    plainText += chr(code)

print("Plaintext:", plainText)
