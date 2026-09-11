# setting Caeser Cipher key
key=1

#Function to encrypt message 
def caesarCipherEncrypt(ToCode):
    codedStr=""
    
    #transverse string
    for i in range (len(ToCode)):
        char = ToCode[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            codedStr += chr((ord(char) + 1-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            codedStr += chr((ord(char) + 1-97) % 26 + 97)
             
    return codedStr


print("Encryption phase")


#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded)

#to see coded message in shell
print("The coded message is: ",encrypted_message)

