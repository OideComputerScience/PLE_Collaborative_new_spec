
#In this example we are working with lower case only.
# It reads in a message and shifts it according to the key input. 
alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#index =  [0,   1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

message=input("Enter message to be encrypted:  ")

keyshift=int(input("key shift:  "))

encrypted_list=[]

for i in message:
    index_position=alphabet.index(i)
    cipher_index=(index_position+keyshift)%26
    encrypted_list.append(alphabet[cipher_index])
    
#encrypted_text=
print(encrypted_list)

# Convert list to string using a loop
encrypted_text = ""                 
for letter in encrypted_list :
    encrypted_text += letter + " "
print(encrypted_text.strip())   