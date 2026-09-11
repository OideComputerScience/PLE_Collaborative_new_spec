#Using Unicode with ord()function that returns the
#number representing the unicode code of a specified
#character and chr() function that returns the
#character that represents the specified unicode

# Asking the user for the cipher key

key=int(input("Please enter the Caesar cipher key:  "))

print("Encryption phase")

MessageToBeCoded = input("Enter any 6 letter word: ")

#CaesarCipher To encrypt message
codedStr = chr(ord(MessageToBeCoded[0])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[1])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[2])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[3])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[4])+key)
codedStr = codedStr + chr(ord(MessageToBeCoded[5])+key)

print("The coded message is: ",codedStr)