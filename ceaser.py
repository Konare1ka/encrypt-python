import alphabets

def ceaserEncrypt(text, shift):
    text = text.upper()
    #get alphabet
    language: str = alphabets.detect(text)
    if language == 'no':
        print("Text language is not defined")
        exit()
    alphabet = getattr(alphabets, language)
    #encrypt
    crypted = [''] * len(text)
    for index in range(len(text)):
        found: bool = False
        for letter in range(len(alphabet)):
            if text[index] == alphabet[letter]:
                crypted[index] = alphabet[(letter+shift) % len(alphabet)]
                found = True
        if not found:
            crypted[index] = text[index]
            
    
    result = ''.join(crypted)
    print("Successful encryption, result:")
    print(result)