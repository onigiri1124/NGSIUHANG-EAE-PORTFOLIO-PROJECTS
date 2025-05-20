import random
import string
#modules needed for this encryption project

chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
#includes punctuation letters, ASCII digits, and ASCII uppercase and lowercase letters

chars = list(chars)
#converts chars into a list of individual elements, in this case, each alphabet, digit, and element
key = chars.copy()
#creates a separate copy called key with a copy of the elements in chars

random.shuffle(key)
#rearrange elements in key in a random order, ELEMENTS IN CHARS REMAIN UNCHANGED AS chars.copy IS USED

print(f"chars: {chars}")
print(f"key: {key}")

#-------------------------------------------------------------------------------------------
#encryption

plain_text = input("input message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) #retrives the value of index of the elements in plain_text in terms of chars
    cipher_text += key[index] #adds the element of the corresponding index of chars in elements of key under cipher_text


print(f"encrypted message: {cipher_text}") #prints the encrypted message

#-------------------------------------------------------------------------------------------
#decryption

encrypted_text = input("input message to decrypt: ")
decrypted_text = ""
#new variables are created to avoid confusion/conflict in code

for letter in encrypted_text:
    index = key.index(letter)  #retrives the value of index of the elements in encrypted_text in terms of key
    decrypted_text += chars[index] #adds the element of the corresponding index of key in elements of char under-
                                   #-decrypted text

print(f"decrypted message: {decrypted_text}") #prints the decrypted message

#--------------------------------------------------------------------------------------------