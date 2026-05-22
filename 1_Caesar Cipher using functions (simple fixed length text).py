#Using Unicode with ord()that returns the number representing the unicode code of a specified character
#and char() function that returns the character that represents the specified unicode

#A Cipher Key of 1
#Method to code message (using for in range)
def caesarCipher(ToCode):
    codedStr = chr(ord(ToCode[0])+1)#first character already 
    
    for i in range (len(ToCode)-1):#first character already coded
        codedStr = codedStr + chr(ord(ToCode[i+1])+1)
    print(codedStr)#to see coded message in shell
    return codedStr

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

#add message to be coded to list
MessageToBeCodedList = list(MessageToBeCoded)

# Calling Function that codes the message
result=caesarCipher(MessageToBeCodedList)


'''
print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#decription
#decoding message received ising the same cipher key as used for encryption
deCodedMessage= chr(ord(codedStr[0])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[1])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[2])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[3])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[4])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[5])-1)

# Print out decoded message
print("The decoded message is: ",deCodedMessage)'''