# Updated to allow for encryption and decryption of letters, symbols and numbers.

# This is a list of valid characters
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '@', '~', '#',
            ',' , '.', '/', '<', '>', '?',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Getting user input for the cipher section..
def get_user_inputs(characters):
    direction_options = ["encrypt", "decrypt"]
    direction = input("Type 'encrypt' to encrypt your word, or 'decrypt'.\n").lower()
    
    while direction not in direction_options:
        direction = input("Please type 'encrypt' to encrypt your word, or 'decrypt'.\n").lower()
        
        
    user_message = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))
    characters_length = len(characters)
        
    return direction,user_message,user_shift,characters_length


# Depending on if the user choses to encrypt or decrypt the text this will print out the text that been encrypted or 
# decrypted based on the number of shift.
def cipher(text, shift, direction):
    output = ""
    
    # If the user has selected decrypt it converts the number into a minus varient so that it can shift backwards.
    if direction == "decrypt":
        shift *= -1
    
    # Loops throught the users message and will change the character to the new character based on the given shift 
    # value, for instance 'mjqqt' with a shift of 5 would be come 'hello'.
    for char in text:
        if (char in characters) and (char != ""):
            character_index = characters.index(char)
            new_index = character_index + shift
            
            if new_index > characters_length:
                new_index -= characters_length
            
            output += characters[new_index]
        else:
            output += char
            
    print(f"\nYour {direction}ed text is: {output}\n")
    

print("Welcome to the caesar cipher encrypter and decrypter.")

# Displays a menu for the user to select from.
while True:
    user_input = input('''Welcome, please select one of the numbers below.
          1. Check the valid characters.
          2. Encrypt or decrypt a message.
          3. Exit the menu.
          ''')
    
    # Displays the current valid characters that the user can choose from.
    if user_input == "1":
        print("Below is a list of all the valid characters:\n" + str(characters))
    
    # Passes in the users input and calls the 'cipher' function to encrypt or decrypt a text.
    elif user_input == "2":
        direction, user_message, user_shift, characters_length = get_user_inputs(characters)
        
        if user_shift > characters_length:
            user_shift %= characters_length

        cipher(user_message, user_shift, direction)
    
    # Exits the menu.
    elif user_input == "3":
        print("Thank you for using my caesar cipher program.")
        break
    
    # Catches anything other than 1 - 3.
    else:
        print("Please enter 1 - 3 to select one of the choices.")
