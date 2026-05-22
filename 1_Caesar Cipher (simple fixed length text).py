
#Using Unicode with ord()function that returns the number representing the unicode code of a specified character
#and chr() function that returns the character that represents the specified unicode

# A Cipher Key of 1
print("Encryption phase")

MessageToBeCoded = input("Enter any 6 letter word: ")

#CaesarCipher To encrypt message
codedStr = chr(ord(MessageToBeCoded[0])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[1])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[2])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[3])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[4])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[5])+1)

print("The coded message is: ",codedStr)


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
print("The decoded message is: ",deCodedMessage)

