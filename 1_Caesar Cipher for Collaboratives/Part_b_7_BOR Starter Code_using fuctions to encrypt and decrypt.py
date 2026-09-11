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
        
print("Encryption phase")

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded, key)

#to see coded message in shell
print("The coded message is: ",encrypted_message)



