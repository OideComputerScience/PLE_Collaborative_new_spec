#This code differs to 1_Caesar cipher by making use of functions.
#It also makes use of for loops and so the program is not restricted
#to a particular length.
#The ord() and chr() functions are still being used to allow the program
#to work with unicode. 


#A Cipher Key of 1
#Function to encrypt message 
def caesarCipherEncrypt(ToCode):
    codedStr=""
    
    #no restriction on length of string here as we are using a for loop
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
    print("The decoded message is: ",deCodedStr)#to see coded message in shell
    #return codedStr
    
    
print("Encryption phase")
#Using Caeser Cipher Key of 1 to decode message   

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded)

print("The coded message is: ",encrypted_message)#to see coded message in shell

print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#Calling Decrytion function
caesarCipherDecrypt(encrypted_message)
