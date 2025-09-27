import alphabets

def vigenereEncrypt(text, raw_key):
    text = text.upper()
    raw_key = raw_key.upper()
    #get alphabet
    language: str = alphabets.detect(text)
    if language == 'no':
        print("Text language is not defined")
        exit()
    alphabet = getattr(alphabets, language)
    #get language from key
    languageKey: str = alphabets.detect(raw_key)
    if languageKey != language:
        print("Different language of text and key")
        exit()
    #decrypt key
    key = [''] * len(raw_key)
    for index, char in enumerate(raw_key):
        for num, letter in enumerate(alphabet):
            if char == letter:
                key[index] = num + 1    
    #encrypt text
    crypted = [''] * len(text)
    keyNum: int = 0
    for index in range(len(text)):
        found: bool = False
        if keyNum == len(key):
            keyNum = 0
        for letter in range(len(alphabet)):
            if text[index] == alphabet[letter]:
                crypted[index] = alphabet[(letter+key[keyNum]) % len(alphabet)]
                found = True
                keyNum += 1
        if not found:
                crypted[index] = text[index]
                
    result = ''.join(crypted)
    print("Successful encryption, result:")
    print(result)