#Using Unicode with ord()function that returns the number
#representing the unicode code of a specified character
#and chr() function that returns the character that represents
#the specified unicode.

#A Cipher Key of 1
#Function to encrypt message 
def caesarCipherEncrypt(ToCode):
    codedStr=""
    
     #transverse string
    for i in range (len(ToCode)):
        codedStr = codedStr + chr(ord(ToCode[i])+1)
    #print("The coded message is: ",codedStr)#to see coded message in shell
    return codedStr
    
print("Encryption phase")
#Using Caeser Cipher Key of 1 to decode message   

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded)

print("The coded message is: ",encrypted_message)#to see coded message in shell


