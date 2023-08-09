alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
#
#
# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(shifts, plain_text):
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
#     #  amount and print the encrypted text.
#
#     # e.g.
#     # plain_text = "hello"
#     # shift = 5
#     indices = []
#     # cipher_text = "mjqqt"
#     # print output: "The encoded text is mjqqt"
#     for x in plain_text:
#         indices.append((alphabet.index(x) + shifts))
#     encode = []
#     for ind in indices:
#         encode.append(alphabet[ind])
#     strings = "".join(encode)
#     return strings
#
#     # HINT: How do you get the index of an item in a list:
#     # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
#
# # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
# #  message.
#
#
# # Decrypting
#
#
# # plain_txt = "hello"
# indices_cipher = []
#
#
# def decrypt(shifts, texts):
#     for j in texts:
#         indice = alphabet.index(j) - shifts
#         indices_cipher.append(alphabet[indice])
#     decodeds = "".join(indices_cipher)
#     return decodeds
#
#
# running = False
#
# while running:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     if direction == 'encode':
#         text = input("Type your message to encrypt:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         encoded = encrypt(shifts=shift, plain_text=text)
#         print(encoded)
#     elif direction == 'decode':
#         cipher_text = input("Type your message to Decrypt:\n").lower()
#         shifted = int(input("Type the shift number:\n"))
#         decoded = decrypt(shifts=shifted, texts=cipher_text)
#         print(decoded)
#     else:
#         running = False
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message to encrypt:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(texts, directin, shifts):
    indexes = []
    textall = []
    if directin == "encode":
        for letter in texts:
            indice = alphabet.index(letter) +shifts
            indexes.append(alphabet[indice])
        textall = "".join(indexes)
    elif directin == "decode":
        for letter in texts:
            indice = alphabet.index(letter) - shifts
            indexes.append(alphabet[indice])
        textall = "".join(indexes)
    print(textall)


caesar(texts=text, shifts=shift, directin=direction)
