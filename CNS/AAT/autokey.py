import detectEnglish

# Dictionary to lookup the index of alphabets
charToInt = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

intToChar = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


# This function generates the key
def generate_key(message, key):
    if len(key) > len(message):
        # print(key[:len(message)])
        return key[:len(message)]
    i = 0
    while True:
        # print('i:', str(i))
        # print(message[i])
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i]
            i += 1
        # print(key)
    return key

def generate_key_dict(ct, sk):
    # we have the short key

    # ct = HXRAVD IU DWVTM
    # sk = HEY
    spaces = [] 
    for index, ch in enumerate(ct):
        if ch == ' ':
            spaces.append(index)
    
    # print(spaces)
    ct = ct.replace(' ', '')

    # print('ct: ', ct)
    # print('sk: ', sk)
    sk_len = len(sk) # HEY = 3

    key_full = sk
    
    i=0
    while len(key_full) < len(ct):
        # print('i =', str(i))      
        
        temp_ct = ct[sk_len*(i):sk_len*(i+1)]
        # print('temp_ct: ', temp_ct)

        key_full += getOriginalText(temp_ct, sk)
        # print('key_full: ', key_full)

        sk = key_full[sk_len*(i+1):sk_len*(i+2)]
        # print('sk: ', sk)

        i+=1

    key_full = key_full[:len(ct)]
    
    # for index, ch in enumerate()

    return key_full




    # if len(sk) > len(ct):
    #     return key[:len(ct)]
    
    


# This function returns the encrypted text
# generated with the help of the key
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


# This function decrypts the encrypted text
# and returns the original text
def getOriginalText(cipher_text, key_full):
    # if key_full[:3] == 'HEY':
    #     print(cipher_text, ' --- ', key_full)
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
        # key = generate_key(cipher_text, word.strip())
        key = generate_key_dict(cipher_text, word.strip())
        decrypted_text = getOriginalText(cipher_text, key)
        # if word.strip() == 'HEY':
        #     # print(word.strip(), ' ', decrypted_text)
        
        #     key = generate_key_dict(cipher_text, word.strip())

        #     print('ct: ', cipher_text)
        #     print('key:', key)
        #     decrypted_text = getOriginalText(cipher_text, key)
        # if 'ATTACK' in decrypted_text:
        #     print(decrypted_text)

        if detectEnglish.isEnglish(decrypted_text, wordPercentage=70):
            print()
            print('Found! Key = ' + str(word) + 'Plaintext  = ' + decrypted_text[:100])
            print()
            print('Enter Q to exit, press Enter to continue trying:')
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
