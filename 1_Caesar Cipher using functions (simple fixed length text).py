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

