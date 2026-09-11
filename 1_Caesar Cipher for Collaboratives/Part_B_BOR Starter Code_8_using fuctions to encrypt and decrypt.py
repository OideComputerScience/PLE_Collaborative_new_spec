#Using Unicode with ord()function that returns the number
#representing the unicode code of a specified character
#and chr() function that returns the character that represents
#the specified unicode.

# Asking the user for the cipher key
key=int(input("Please enter the caesar cipher key:  "))

#Function to encrypt message 
def caesarCipherEncrypt(ToCode,cipherkey):
    codedStr=""
    
     #transverse string
    for i in range (len(ToCode)):
        codedStr = codedStr + chr(ord(ToCode[i])+cipherkey)
    return codedStr


#Function to decrypt message 
def caesarCipherDecrypt(ToDecode, cipherkey):
    deCodedStr=""
    
    for i in range (len(ToDecode)):
        deCodedStr = deCodedStr + chr(ord(ToDecode[i])-cipherkey)
    print("The coded message is: ",deCodedStr)#to see coded message in shell
    #return codedStr
    
    
print("Encryption phase")


#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded, key)

print("The coded message is: ",encrypted_message)#to see coded message in shell

print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#Calling Decrytion function
caesarCipherDecrypt(encrypted_message, key)

