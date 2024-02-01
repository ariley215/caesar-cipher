from caesar_cipher.corpus_loader import word_list, name_list
import re

input_strings = [
    "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]


def encrypt(text, shift):
    encrypted_text = ""
    number_of_characters = 26
    

    for char in text:
      if char.isalpha():
        base_char = 'A' if char.isupper() else 'a'
        base_code = ord(base_char)
        current_code = ord(char)
        char_position = current_code - base_code
        shifted_position = (char_position + shift) % number_of_characters
        shifted_char = base_code + shifted_position
        encrypted_text += chr(shifted_char)
      elif char.isspace():
        encrypted_text += char
      else: encrypted_text += char
    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

def count_words(text):
    input_strings = text.split()
    word_count = 0

    for strings in input_strings:
        word = re.sub(r"[^A-Za-z]+", "", strings)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count


for phrase in input_strings:
    word_count = count_words(phrase)
    percent = int(word_count / len(phrase.split()) * 100)
    print(percent, phrase)


def crack(cipher):
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  for shift in range(26):
    plain_text = ""
    for char in cipher:
      if char in letters:
        num = letters.find(char)
        new_num = (num - shift) % 26
        plain_text += letters[new_num]
      else:
        plain_text += char
        
      
    word_count = count_words(plain_text)
    if word_count > 0:
      return plain_text
  return ""
      
    
