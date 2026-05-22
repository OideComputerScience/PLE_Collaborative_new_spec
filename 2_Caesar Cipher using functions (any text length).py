#Using Unicode with ord()function that returns the number representing the unicode code of a specified character
#and chr() function that returns the character that represents the specified unicode

#A Cipher Key of 1
#Function to encrypt message 
def caesarCipherEncrypt(ToCode):
    codedStr=""
    
     #transverse string
    for i in range (len(ToCode)):
        codedStr = codedStr + chr(ord(ToCode[i])+1)
    #print("The coded message is: ",codedStr)#to see coded message in shell
    return codedStr


#Function to decrypt message 
def caesarCipherDecrypt(ToDecode):
    deCodedStr=""
    
    for i in range (len(ToDecode)):
        deCodedStr = deCodedStr + chr(ord(ToDecode[i])-1)
    print("The coded message is: ",deCodedStr)#to see coded message in shell
    #return codedStr
    
    
print("Encryption phase")
#Using Caeser Cipher Key of 1 to decode message   

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
result=caesarCipherEncrypt(MessageToBeCoded)

print("The coded message is: ",result)#to see coded message in shell

print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#Calling Decrytion function
caesarCipherDecrypt(result)
