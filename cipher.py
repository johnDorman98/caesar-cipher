# This is the first step for the caesar cipher this section handles the encryption of a string.

# To start with the program works for only string inputs.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Getting user input.
direction = input("Type 'encode' to encrypt your word.\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Decryption function to encrypt string to given shift.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    
    # Loops through each letter that the use enters and changes it via the shift amount.
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount

        if new_index > len(alphabet) -1:
            new_index -= len(alphabet)

        cipher_text += alphabet[new_index]

    print(f"The encoded text is {cipher_text}")

encrypt(text, shift)