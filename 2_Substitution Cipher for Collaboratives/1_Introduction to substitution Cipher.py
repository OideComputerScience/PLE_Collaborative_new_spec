#Substitution Cipher for letters only
import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creating a cipher alphabet
# returns a new list with shuffled elements
cipher_alphabet = random.sample(alphabet_list, len(alphabet_list))

# Display both alphabets- testing
print("Normal Alphabet:")
print(alphabet_list)

print("Cipher Alphabet:")
print(cipher_alphabet)

# Ask the user for a message
MessageToBeCoded = input("Enter a message to encrypt: ")

# Convert message to lowercase
MessageToBeCoded = MessageToBeCoded.lower()

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
print("The plain text message " + MessageToBeCoded + " has been encryted to " +encrypted_message)



