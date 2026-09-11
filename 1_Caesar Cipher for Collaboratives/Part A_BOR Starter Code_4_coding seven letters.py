#Using Unicode with ord()function that returns the
#number representing the unicode code of a specified
#character and chr() function that returns the
#character that represents the specified unicode

# Asking the user for the cipher key
key=int(input("Please enter the caesar cipher key:  "))

print("Encryption phase")

MessageToBeCoded = input("Enter any 6 letter word: ")

#CaesarCipher To encrypt message
codedStr = chr(ord(MessageToBeCoded[0])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[1])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[2])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[3])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[4])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[5])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[6])+key)
print("The coded message is: ",codedStr)

print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#decoding message received ising the same cipher key as used for encryption
deCodedMessage= chr(ord(codedStr[0])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[1])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[2])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[3])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[4])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[5])-key)
deCodedMessage = deCodedMessage + chr(ord(codedStr[6])-key)
# Print out decoded message
print("The decoded message is: ",deCodedMessage)

