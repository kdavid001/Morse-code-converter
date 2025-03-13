# Copyright (c) 2025 Iyke Kisala
# All rights reserved.
#
# This code is the property of Iyke Kisala. Unauthorized copying,
# distribution, or modification of this code is strictly prohibited.
#
# Licensed under [Your License] (if applicable)


morse_code_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',  't': '-',
    'u': '..-',   'v': '...-', 'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
result = []
final = ""

word = input("Word to convert? ")
word_list = list(word)

for x in word_list:
    if x == " " :
        continue
    y = morse_code_dict[f"{x}"]
    result.append(y)

for a in result:
    final += f" {a}"

print(final)