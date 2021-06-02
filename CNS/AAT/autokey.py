import detectEnglish

charToInt = {} # {'A': 0, 'B': 1, ... 'Z': 25}
intToChar = {} # {0: 'A', 1: 'B', ... 25: 'Z'}


for i in range(0, 26):
    index = i
    letter = chr(index + 65)
    intToChar[index] = letter
    charToInt[letter] = index


# Generates the key
def generate_key(message, key):
    if len(key) > len(message):
        return key[:len(message)]
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i]
            i += 1
    return key


# Generates the key 'n' characters at a time
# n -> length of the dictionary word used 
def generate_key_dict(ct, sk):
    spaces = [] 
    for index, ch in enumerate(ct):
        if ch == ' ':
            spaces.append(index)

    ct = ct.replace(' ', '')

    sk_len = len(sk)

    key_full = sk
    
    i = 0
    while len(key_full) < len(ct):   
        temp_ct = ct[sk_len*(i):sk_len*(i+1)]

        key_full += getOriginalText(temp_ct, sk)

        sk = key_full[sk_len*(i+1):sk_len*(i+2)]

        i += 1

    key_full = key_full[:len(ct)]

    return key_full


# Encrypts the text using the key
def getCipherText(message, key_full):
    cipher_text = ''
    i = 0
    for letter in message:
        if letter == ' ':
            cipher_text += ' '
        else:
            x = (charToInt[letter]+charToInt[key_full[i]]) % 26
            i += 1
            cipher_text += intToChar[x]
    return cipher_text


# Decrypts the encrypted text
def getOriginalText(cipher_text, key_full):
    or_txt = ''
    i = 0
    for letter in cipher_text:
        if letter == ' ':
            or_txt += ' '
        else:
            x = (charToInt[letter]-charToInt[key_full[i]]+26) % 26
            i += 1
            or_txt += intToChar[x]
    return or_txt


def dictionaryAttack(cipher_text):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        key = generate_key_dict(cipher_text, word.strip())
        decrypted_text = getOriginalText(cipher_text, key)

        if detectEnglish.isEnglish(decrypted_text, wordPercentage=70):
            print('\nFound! Key = ' + str(word) + 'Plaintext  = ' + decrypted_text[:100])
            print('\nEnter Q to exit, press Enter to continue trying:')
            response = input('> ')
            if response.upper().startswith('Q'):
                return decrypted_text


def main():
    message = input("Enter the message: ").upper()
    key = input("Enter the key: ").upper()

    key_full = generate_key(message, key)

    cipher_text = getCipherText(message, key_full)
    print("Cipher text generated =", cipher_text)
    print('-'*24)

    original_text = getOriginalText(cipher_text, key_full)
    print("Plain text using key =", original_text)
    print('-'*24)

    print("Attempting to decrypt using dictionary attack")
    decrypted_text = dictionaryAttack(cipher_text)
    print("Plain text using dictionary attack =",decrypted_text)


if __name__ == '__main__':
    main()
