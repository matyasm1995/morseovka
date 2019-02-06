def decode_morse(message):
    """
    funkce pro dekodovani morseovky
    :param message: textovy retezec pro dekodovani
    :return: prelozeny kod
    """
    sep_message = message.split(' ')  # rozdeleni textoveho retezce do skupin odpovidajicim jednotlivym znakum
    decode_message = ''  # prazdny retezec pro prelozeny kod
    for char in sep_message:
        if char in inverse_morse_alphabet:  # vyhledani odpovidajiciho znaku v slovniku
            decode_message += inverse_morse_alphabet[char]  # pripsani znaku do vystupni zpravy
        elif char == '':  # osetreni vice za sebou jdoucich mezer
            continue
        else:  # pokud nebyl nalezen odpovidajici znak ve slovniku
            decode_message += '<CNF>'  # CNF = Character not found
    return decode_message


def encode2morse(message):
    """
    funkce pro zakodovani zpravy do morseovky
    :param message: textovy retezec pro zakodovani
    :return: zakodovana zprava
    """
    encoded_message = ""
    for char in message:
        if char.upper() in morse_alphabet:
            encoded_message += morse_alphabet[char.upper()] + " "
        else:
            encoded_message += '<CNF>'  # CNF = Character not found
    return encoded_message

morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
}
inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())  # prehozeni klicu a hodnot

test_code = 'Toto je testovaci kod. Program vezme tento kod, prelozi ho do morseovky a nasledne ho zpetne desifruje pro kontrolu.'
print('testovaci kod: ' + test_code)
print('zakodovana zprava: ' + encode2morse(test_code))
print('dekodovana zprava: ' + decode_morse(encode2morse(test_code)))
