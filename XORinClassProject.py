import math

characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]


def XOR (bit1, bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"



def XORonByte(byte, key): 

    ebyte = ""

    for i in range(len(byte)):
        ebyte += XOR(byte[i], key[i])
    
    return ebyte


def XORonLetter(Letter, keyLetter):
    BinaryA = encode(Letter)
    BinaryB = encode(keyLetter)

    encryptedLetter = XORonByte(BinaryA, BinaryB)

    return decode(encryptedLetter)


def XORonsentance(sentence, key):

    genkey = generatekey(sentence, key)

    esentence = ""

    for i in range(len(sentence)):
        esentence+= XORonLetter(sentence[i], genkey[i])

    return esentence

def generatekey(message, key):
    

    if(len(message) == len(key)):
        return key
    elif len(message) < len(key):
        return key[0: len(message)]
    else:
        tempkey = ""
        repetitions = math.floor(len(message)/len(key))
        remainder = len(message) % len(key)

        for i in range(repetitions):
            tempkey += key

        tempkey += key[0 : remainder]


        return tempkey


message = input("Please enter your message that you either want to encrypt or decrypt.")
key = input("Please enter the key")

print("Here is your encrypted/decrypted message", XORonsentance(message, key))

