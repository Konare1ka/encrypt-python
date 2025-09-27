ru = (
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 
    'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 
    'Ы', 'Ь', 'Э', 'Ю', 'Я',
)

en = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
)

#Determine language in which text is written
def detect(text):
    if any('а' <= char <= 'я' or char == 'ё' for char in text.lower()):
        return 'ru'
    elif any('a' <= char <= 'z' for char in text.lower()):
        return 'en'
    else: 
        print("Language not detected")
        return 'no'