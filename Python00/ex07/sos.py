#!/usr/bin/env python3

import sys

NESTED_MORSE = {
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
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}


def encode_morse(text):

    text = text.upper()
    morse_list = []
    for ch in text:
        if ch not in NESTED_MORSE:
            raise AssertionError("the arguement are bad")
        morse_list.append(NESTED_MORSE[ch])
    return " ".join(morse_list)


def main():

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the argument are bad")
        text = sys.argv[1]
        result = encode_morse(text)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
