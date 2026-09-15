#Recall from Python Manual p.77 the use of ord() and chr() functions.
# The purpose of ord() is to convert a character to its unicode equivalent.
# The purpose of chr() is to do the opposite. i.e. convert unicode to a
# character. They are used in coding the caeser cipher as with ord() you can simply
# shift characters by a certain number of positions in the alphabet. 


# We are using a Cipher Key of 1
print("Encryption phase")

MessageToBeCoded = input("Enter any 6 letter word: ")

#CaesarCipher To encrypt message
#Restricted to 6 letters and so 6 statements follow.
#Using Unicode with ord()function that returns the
#number representing the unicode code of a specified
#character and chr() function that returns the
#character that represents the specified unicode
codedStr = chr(ord(MessageToBeCoded[0])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[1])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[2])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[3])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[4])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[5])+1)

print("The coded message is: ",codedStr)


print("Decryption phase")
#Using Caeser Cipher Key of 1 to decode message

#decoding message received uing the same cipher key as used for encryption
deCodedMessage= chr(ord(codedStr[0])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[1])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[2])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[3])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[4])-1)
deCodedMessage = deCodedMessage + chr(ord(codedStr[5])-1)

# Print out decoded message
print("The decoded message is: ",deCodedMessage)

