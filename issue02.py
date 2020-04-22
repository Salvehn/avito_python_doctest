"""Morse Code Translator"""

import pytest


LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}

def encode(message: str) -> str:
    """
    Encodes string accordingly with Morse table
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Decodes Morse string to english
    """
    decoded_letters = [MORSE_TO_LETTER[letter] for letter in morse_message.split()]

    return "".join(decoded_letters)


@pytest.mark.parametrize('test_input,expected', [('.-', 'A'), ('... --- ...', 'SOS')])
def test_decode_success(test_input: str, expected: str) -> None:
    """
    Checking for symbols, that are represented in dictionary LETTER_TO_MORSE.
    :param test_input:
    :param expected:
    :return:
    """
    assert decode(test_input) == expected


def test_decode_exception() -> None:
    """
    Checking for symbols, not represented in dictionary LETTER_TO_MORSE.
    :return:
    """
    with pytest.raises(KeyError):
        decode('a')


def test_decode_empty() -> None:
    """
    Checking for empty string
    :return:
    """
    assert decode('') == ''


if __name__ == '__main__':
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
