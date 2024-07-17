cezar = input("Введити направление(шифровать/дешифровать):")
ENG_or_RUS = input("Выберите язык алфавита(английский/русский):")
step = int(input("Укажите шаг сдвига:"))
text = input("Какой текст нужно использовать?:")

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def cezar_procces(derection, language, step, text):
    for i in range(len(text)):
        if ENG_or_RUS == 'русский':
            alphas = 32
            low_alphabet = rus_lower_alphabet
            upper_alphabet = rus_upper_alphabet
        if ENG_or_RUS == 'английский':
            alphas = 26
            low_alphabet = eng_lower_alphabet
            upper_alphabet = eng_upper_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upper_alphabet.index(text[i])
            if derection == 'дешифровать':
                index = (place - int(step)) % alphas
            elif derection == 'шифровать':
                index = (place + int(step)) % alphas

            if text[i] == text[i].lower():
                print(low_alphabet[index], end = '')
            if text[i] == text[i].upper():
                print(upper_alphabet[index], end = '')

    else:
            print(text[i], end = '')

cezar_procces(cezar, ENG_or_RUS, step, text)
            

