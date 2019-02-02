def decode_morse(message):
    sep_message = message.split(' ')
    decode_message = ''
    for char in sep_message:
        if char in inverse_morse_alphabet:
            decode_message += inverse_morse_alphabet[char]
        elif char == '':
            continue
        else:
            # CNF = Character not found
            decode_message += '<CNF>'
    return decode_message


# encode a message in morse code, spaces between words are represented by '/'
def encode2morse(message):
    encoded_message = ""
    for char in message[:]:
        if char.upper() in morse_alphabet:
            encoded_message += morse_alphabet[char.upper()] + " "
        else:
            encoded_message += '<CNF>'
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
inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())

test_code = 'Toto je testovaci kod. Program vezme tento kod, prelozi ho do morseovky a nasledne ho zpetne desifruje pro kontrolu.'
print('testovaci kod: ' + test_code)
print('zakodovana zprava: ' + encode2morse(test_code))
print('dekodovana zprava: ' + decode_morse(encode2morse(test_code)))
