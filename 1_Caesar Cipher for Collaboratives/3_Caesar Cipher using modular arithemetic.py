'''
To encrypt a message using Unicode with ord() function that returns the
number representing the unicode code of a specified character
and chr() function that returns the character that represents the
specified unicode.
By also using Python's modulo operator % (modular arithmetic)
we can have the coded message limited to letters in the English alphabet.


'''
# setting Caeser Cipher key
key=4

#Function to encrypt message 
def caesarCipherEncrypt(ToCode, key):
    codedStr=""
    
    #transverse string
    for i in range (len(ToCode)):
        char = ToCode[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            codedStr += chr((ord(char) - key-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            codedStr += chr((ord(char) - key-97) % 26 + 97)
             
    return codedStr


#Function to decrypt message 
def caesarCipherDecrypt(ToDecode, key):
    deCodedStr=""
    
    for i in range (len(ToDecode)):
        char = ToDecode[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            deCodedStr += chr((ord(char) + key-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            deCodedStr += chr((ord(char) + key-97) % 26 + 97)
    #print("The coded message is: ",deCodedStr)#to see coded message in shell
    return deCodedStr
    



print("Encryption phase")
#Using Caeser Cipher Key of 1 to decode message   

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded,key)

print("The coded message is: ",encrypted_message)#to see coded message in shell
# 
print("Decryption phase")

 
#Calling Decryption function
Decrypt_result=caesarCipherDecrypt(encrypted_message,key)

print("The decoded message is: ",Decrypt_result)#to see decoded message in shell
