# Morse Code translator Project

def translate(words):
    words = words.lower()
    new_word = []
    for i in words:
        if i in alphabet:
            new_word.append(alphabet[i])
    return new_word

def decypher(message):
    decoded_message = ""
    morse_to_char = {morse: char for char, morse in alphabet.items()}
    input = message.split(" ")
    for word in input:
        chars = word.split()
        for i , char in enumerate(chars):
            if i == 0:
                decoded_message += morse_to_char.get(char, '').upper()
            else:
                decoded_message += morse_to_char.get(char, '').lower()
        decoded_message += " "
    return decoded_message.strip()


def menu_list():
    while True:
        output = (f"{BLUE}|————————————————————————————————————————————|\n")
        output += (f"|{YELLOW} Select one of the following Options below:{BLUE} |\n")
        output += (f"{BLUE}|                                            |\n")
        output += (f"|{YELLOW} t - Translate a message to Morse Code.    {BLUE} |\n")
        output += (f"|{YELLOW} d - Decypher a Morse Code message.        {BLUE} |\n")
        output += (f"{BLUE}|                                            |\n")
        output += (f"|{YELLOW} e - Exit Program.                         {BLUE} |\n")
        output += (f"{BLUE}|————————————————————————————————————————————|\n")
        print(output)
        choice = input(f"{YELLOW}Enter Choice:")
        if choice == 't':
            phrase = input("Please enter a phrase which you would like to translate to morse code: ")
            print(f"Your phrase is /n {translate(phrase)}")
            menu_list()

        elif choice == 'd':
            message = input("Please enter the message you like to decypher. \n"
                            "Please note you message use the following characters with a space between \n"
                            "each letter. ─ • \n")
            print(f"Your de-cyphered message is: \n{decypher(message)}")
            menu_list()

        elif choice == 'e':
            # code to exit program
            print('Goodbye!!!')
            exit()

        else:
            print("Your choice has not been recognised, Please Try again")


BLUE = '\033[94m'
YELLOW = '\033[93m'
alphabet = {"a": "•─", "b": "─•••", "c": "─•─•", "d": "─••", "e": "•",
            "f": "••─•", "g": "──•", "h": "••••", "i": "••", "j": "•───",
            "k": "─•─", "l": "•─••", "m": "──", "n": "─•", "o": "───",
            "p": "•──•", "q": "──•─", "r": "•─•", "s": "•••", "t": "─",
            "u": "••─", "v": "•••─", "w": "•──", "x": "─••─", "y": "─•──",
            "z": "──••", '0': '−−−−−', '1': '·−−−−', '2': '··−−−', '3': '···−−',
            '4': '····−', '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··',
            '9': '−−−−·', ' ': '__'}

# potentially to be used later to add sound generation
convert_dict = {
    "A": [1, 2], "B": [2, 1, 1, 1], "C": [2, 1, 2, 1], "D": [2, 1, 1],
    "E": [1], "F": [1, 1, 2, 1], "G": [2, 2, 1], "H": [1, 1, 1, 1],
    "I": [1, 1], "J": [1, 2, 2, 2], "K": [2, 1, 2], "L": [1, 2, 1, 1],
    "M": [2, 2], "N": [2, 1], "O": [2, 2, 2], "P": [1, 2, 2, 1],
    "Q": [2, 2, 1, 2], "R": [1, 2, 1], "S": [1, 1, 1], "T": [2],
    "U": [1, 1, 2], "V": [1, 1, 1, 2], "W": [1, 2, 2], "X": [2, 1, 1, 2],
    "Y": [2, 1, 2, 2], "Z": [2, 2, 1, 1],
    "0": [2, 2, 2, 2, 2], "1": [1, 2, 2, 2, 2], "2": [1, 1, 2, 2, 2],
    "3": [1, 1, 1, 2, 2], "4": [1, 1, 1, 1, 2], "5": [1, 1, 1, 1, 1],
    "6": [2, 1, 1, 1, 1], "7": [2, 2, 1, 1, 1], "8": [2, 2, 2, 1, 1],
    "9": [2, 2, 2, 2, 1]
}

menu_list()

