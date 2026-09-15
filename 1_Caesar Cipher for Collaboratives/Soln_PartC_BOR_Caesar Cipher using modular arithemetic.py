''' 
To encrypt a message using Unicode with ord() function that returns the
number representing the unicode code of a specified character
and chr() function that returns the character that represents the
specified unicode.
By also using Python's modulo operator % (modular arithmetic)
we can have the coded message limited to letters in the English alphabet.
''' 

# setting Caeser Cipher key
key=3

#Function to encrypt message 
def caesarCipherEncrypt(ToCode, key):
    codedStr="" #this will contain the encrypted result
    
    #transverse the string one character at a time
    for i in range (len(ToCode)):
        char = ToCode[i]

        # Encrypt uppercase characters
        #uppercase ASCII letters go from 65 - 90, thus the use of 65 for uppercase characters.
        # Modulo 26 lets us treat the alphabet as a circle so that shifting past "A" or "Z" wraps around.
        # modulo % gives the remainder after division.
        # e.g. C=67, key=3, so (ord("C") + 3 - 65) % 26 + 65 = (67 + 3 - 65) % 26 + 65 = 5 % 26 +65 = 5+65 = 70, chr(70)=F
        if (char.isupper()):
            codedStr += chr((ord(char) + key-65) % 26 + 65) 

        # Encrypt lowercase characters
        #lowercase ASCII letters go from 97-122
        elif char.islower():
            codedStr += chr((ord(char) + key-97) % 26 + 97)
        else: #here spaces, numbers, punctuation go unchanged. 
            codedStr +=char        
             
    return codedStr


#Function to decrypt message 
def caesarCipherDecrypt(ToDecode, key):
    deCodedStr=""
    
    for i in range (len(ToDecode)):
        char = ToDecode[i]

        # Decrypt uppercase characters
        if (char.isupper()):
            deCodedStr += chr((ord(char) - key-65) % 26 + 65)

        # Decrypt lowercase characters
        elif (char.islower()):
            deCodedStr += chr((ord(char) - key-97) % 26 + 97)
        else:
            deCodedStr+=char
    #print("The coded message is: ",deCodedStr)#to see coded message in shell
    return deCodedStr
    



print("Encryption phase") 

#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded:  ")

# Calling the encryption function
encrypted_message=caesarCipherEncrypt(MessageToBeCoded,key)

print("The coded message is: ",encrypted_message)#to see coded message in shell
# 
print("Decryption phase")

 
#Calling Decryption function
Decrypt_result=caesarCipherDecrypt(encrypted_message,key)

print("The decoded message is: ",Decrypt_result)#to see decoded message in shell
