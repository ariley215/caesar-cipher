from corpus_loader import word_list, name_list
 
def encrypt(text, shift):
  encrypted_text = ""
  number_of_characters = 26
  base_char = "A"
  
  for char in text:
    base_code = ord(base_char)
    current_code = ord(char)
    char_position = current_code - base_code
    shifted_position = (char_position + shift) % number_of_characters
    shifted_char = base_code + shifted_position
    encrypted_text += chr(shifted_char)
    
  return encrypted_text
    
    
def decrypt(encoded, -shift):
  return encrypt(encoded, -shift)
 
  
  
if __name__ == "__main__":
plain_pin = "1234"
encrypted_pin = encrypt(plain_pin, 1)
print(encrypted_pin)