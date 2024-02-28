import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n>>> ")
text = input("Type your message:\n>>> ").lower()
shift = int(input("Type the shift number:\n>>> "))


def caesar(shift_amt, dir, input_text):
    cipher_text = ""
    new_shift_amt = 0

    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if dir == 'decode':
                new_shift_amt = shift_amt * -1
                cipher_index = (alphabet.index(letter) + new_shift_amt)
            else:
                cipher_index = (alphabet.index(letter) + shift_amt) % 26

            cipher_text += alphabet[cipher_index]
        else:
            cipher_text += letter
    print(f"The {dir}d text is : {cipher_text}")
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n>>> ")
    if repeat == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n>>> ")
        text = input("Type your message:\n>>> ").lower()
        shift = int(input("Type the shift number:\n>>> "))
        caesar(dir=direction, input_text=text, shift_amt=shift)


caesar(dir=direction, input_text=text, shift_amt=shift)


# def encrypt(text,shift):
#     cipher_text = ""
#     if shift == 0:
#         cipher_text= text
#     elif shift>0:
#         for char in text:
#             if char in alphabet:
#                 new_char_index = (alphabet.index(char)+shift)%26
#                 cipher_text += alphabet[new_char_index]
#             else:
#                 cipher_text += char
#     print(f"Encrypted text : {cipher_text}")
#     return cipher_text
#
# def decrypt(cipher_text, shift):
#     decrypted_text = ""
#     if shift == 0:
#         decrypted_text= text
#     elif shift>0:
#         for char in cipher_text:
#             if char in alphabet:
#                 new_char_index = (alphabet.index(char)-shift)
#                 decrypted_text += alphabet[new_char_index]
#             else:
#                 decrypted_text += char
#     print(f"Decoded text : {decrypted_text}")
#
# if direction == 'encode':
#     encrypted_text = encrypt(text,shift)
# elif direction == 'decode':
#     decrypt(text,shift)
