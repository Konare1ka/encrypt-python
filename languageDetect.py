#Determine language in which text is written
def detect(text):
    if any('а' <= char <= 'я' or char == 'ё' for char in text.lower()):
        return 'ru'
    elif any('a' <= char <= 'z' for char in text.lower()):
        return 'en'
    else: 
        print("Language not detected")
        return 'no'