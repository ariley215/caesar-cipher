from caesar_cipher.corpus_loader import word_list, name_list
from nltk.corpus import words
import re

number_of_characters = 26


def encrypt(text, shift):
    encrypted_text = []

    for char in text:
        if char.isalpha():
            base_char = "A" if char.isupper() else "a"
            base_code = ord(base_char)
            current_code = ord(char)
            char_position = current_code - base_code
            shifted_position = (char_position + shift) % number_of_characters
            shifted_char = base_code + shifted_position
            encrypted_text.append(chr(shifted_char))
        elif char.isspace():
            encrypted_text.append(char)
        else:
            encrypted_text.append(char)

    return "".join(encrypted_text)


def decrypt(encoded, shift):
    return encrypt(encoded, shift * -1)


def count_words(text):
    input_strings = text.split()
    word_count = 0

    for string in input_strings:
        print(string)
        word = re.sub(r"[^A-Za-z]+", "", string)
        if word.lower() in word_list or word in name_list:
            # print("english word: " + word)
            word_count += 1
        else:
            # print("not an english word: " + word)
            pass
    return word_count


def load_words():
    english_words = set(word_list)
    return english_words


def calculate_word_validity_ratio(input_strings, word_count):
    ratio = int((word_count/ len(input_strings)) * 100)
    return min(ratio, 100.0)


def crack(encoded):
    print("encoded: ", encoded)
    for shift in range(number_of_characters):
        word_count = 0
        decrypted_text = decrypt(encoded, shift)
        input_strings = decrypted_text.split()
        for string in input_strings:
            word = re.sub(r"[^a-zA-Z]+", "", string)
            print('word', word)
            if word in word_list:
                word_count += 1
                print('word count', word_count)
            else:
                pass
        validity_ratio = calculate_word_validity_ratio(input_strings, word_count)
        print("input strings, word count", input_strings, word_count)
        print(
            f"Shift: {shift} Text: {decrypted_text}, Validity Ratio: {validity_ratio}"
        )
        if validity_ratio > 50:
            return decrypted_text

    return ""


if __name__ == "__main__":
    # test_string = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    english_words = load_words()
    # print(english_words)
