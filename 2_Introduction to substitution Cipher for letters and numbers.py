#Substitution Cipher for letters only

import random
import string

#hard coded 
# alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#                  'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#                  'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
#                  '8', '9']

# A list containing all characters and numbers
alphabet_list = string.ascii_letters+string.digits


# Creating a cipher alphabet
# returns a new list with shuffled elements
cipher_alphabet = random.sample(alphabet_list, len(alphabet_list))

# Display both alphabets- testing
print("Normal Alphabet:")
print(list(alphabet_list))
print("")

print("Cipher Alphabet:")
print(cipher_alphabet)
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Ask the user for a message
MessageToBeCoded = input("Enter a message to encrypt: ")

# Variable to store encrypted message
encrypted_message = ""

# Loop through each letter in the message
for letter in MessageToBeCoded:

    # Check if the character is in the alphabet
    if letter in alphabet_list:

        # Find the position of the letter
        position = alphabet_list.index(letter)

        # Get the matching encrypted letter
        encrypted_letter = cipher_alphabet[position]

        # Add encrypted letter to message
        encrypted_message = encrypted_message + encrypted_letter

    else:
        # Keep spaces or symbols unchanged
        encrypted_message = encrypted_message + letter

# Display encrypted message
print("Encrypted Message:")
print("The text " + MessageToBeCoded + " has been encryted to " +encrypted_message)

#Decryption Section

# Variable to store decrypted message
decrypted_message = ""

# Loop through each character
for letter in encrypted_message:

    # Check if character exists in cipher alphabet
    if letter in cipher_alphabet:

        # Find position in cipher alphabet
        position = cipher_alphabet.index(letter)

        # Get original letter from normal alphabet
        original_letter = alphabet_list[position]

        # Add original letter to decrypted message
        decrypted_message = decrypted_message + original_letter

    else:
        # Keep spaces and symbols unchanged
        decrypted_message = decrypted_message + letter

# Display decrypted message
print("Decrypted Message:")
print(decrypted_message)


