from caesar_cipher.corpus_loader import word_list, name_list
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
    return encrypt(encoded, -shift)


def count_words(text):
    input_strings = text.split()
    word_count = 0

    for string in input_strings:
        word = re.sub(r"[^A-Za-z]+", "", string)
        if word.lower() in word_list or word in name_list:
            print("english word: " + word)
            word_count += 1
        else:
            print("not an english word: " + word)

    return word_count


def calculate_word_validity_ratio(decrypted_text, word_list):
    words = decrypted_text.split()
    valid_words = sum(word.lower() in word_list for word in words)
    ratio = (valid_words / len(words)) * 100
    return min(ratio, 100.0)


def crack(encoded, english_words=word_list):
    for shift in range(number_of_characters):
        decrypted_text = decrypt(encoded, shift)
        validity_ratio = calculate_word_validity_ratio(decrypted_text, english_words)
        print(
            f"Shift: {shift} Text: {decrypted_text}, Validity Ratio: {validity_ratio}"
        )
        if validity_ratio > 0.8:
            return decrypted_text

    return ""
