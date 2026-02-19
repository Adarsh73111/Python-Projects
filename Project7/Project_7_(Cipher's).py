# # Basic Cipher
# print(r"""
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\\
# """)
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # def encrypt(original_text, shift_amount):
# #     cipher_text = ""
# #     for letter in original_text:
# #         shifted_position = alphabet.index(letter) + shift_amount
# #         shifted_position = shifted_position % len(alphabet)
# #         cipher_text += alphabet[shifted_position]
# #     print(f"Here is the encoded result: {cipher_text}")
#
# # def decrypt(original_text, shift_amount):
# #     output_text = ""
# #     for letter in original_text:
# #         shifted_position = alphabet.index(letter) - shift_amount
# #         shifted_position = shifted_position % len(alphabet)
# #         output_text += alphabet[shifted_position]
# #     print(f"Here is the decoded result: {output_text}")
#
# def idol(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     actual_shift = shift_amount
#     if encode_or_decode == "decode":
#         actual_shift *= -1
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + actual_shift
#             shifted_position = shifted_position % len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result : {output_text}")
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     # encrypt(original_text=text, shift_amount=shift)
#     # decrypt(original_text=text, shift_amount=shift)
#     idol(original_text=text, shift_amount=shift, encode_or_decode=direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise. type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("GoodBye")


# #Cipher Encoding and Decoding. {Basic}. Work on combine Upper&Lower() Cases
# print(r"""
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\\
# """)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# def idol(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     actual_shift = shift_amount
#     if encode_or_decode == "decode":
#         actual_shift *= -1
#     for letter in original_text:
#         if letter.lower() not in alphabet:
#             output_text += letter
#         else:
#             # Determine the shifted character
#             is_upper = letter.isupper()
#             base_letter = letter.lower()
#             shifted_index = (alphabet.index(base_letter) + actual_shift) % len(alphabet)
#             shifted_char = alphabet[shifted_index]
#             # Preserve the original case
#             output_text += shifted_char.upper() if is_upper else shifted_char
#     print(f"Here is the {encode_or_decode}d result : {output_text}")
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n")
#     shift = int(input("Type the shift number:\n"))
#     idol(original_text=text, shift_amount=shift, encode_or_decode=direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise. type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("GoodBye")


# # Moderate but Secure
# import random
# print(r"""
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\\
# """)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# def idol(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     actual_shift = shift_amount
#     if encode_or_decode == "decode":
#         actual_shift *= -1
#     for letter in original_text:
#         if letter.lower() not in alphabet:
#             output_text += letter
#         else:
#             is_upper = letter.isupper()
#             base_letter = letter.lower()
#             shifted_index = (alphabet.index(base_letter) + actual_shift) % 26
#             shifted_char = alphabet[shifted_index]
#             output_text += shifted_char.upper() if is_upper else shifted_char
#     print(f"\nHere is the {encode_or_decode}d result: {output_text}\n")
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n")
#     if direction == "encode":
#         shift = random.randint(1, 25)
#         print(f"Random shift key used for encoding: {shift}")
#     else:
#         shift = int(input("Enter the shift key used during encoding:\n"))
#     idol(original_text=text, shift_amount=shift, encode_or_decode=direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye")


# # Moderate but Low Security
# import random
# import json
# import os
# print(r'''
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\
# ''')
# # Alphabet
# alphabet = [chr(i) for i in range(97, 123)]  # a-z
# key_file = "cipher_key.json"
# # Load or generate a cipher key
# if os.path.exists(key_file):
#     with open(key_file, "r") as f:
#         encrypt_dict = json.load(f)
#         print("Cipher key loaded from file.")
# else:
#     shuffled = alphabet.copy()
#     random.shuffle(shuffled)
#     encrypt_dict = dict(zip(alphabet, shuffled))
#     with open(key_file, "w") as f:
#         json.dump(encrypt_dict, f)
#     print("New cipher key generated and saved.")
# # Decryption dictionary
# decrypt_dict = {v: k for k, v in encrypt_dict.items()}
# # Function to encrypt
# def encrypt(text):
#     result = ""
#     for char in text:
#         if char.lower() in encrypt_dict:
#             new_char = encrypt_dict[char.lower()]
#             result += new_char.upper() if char.isupper() else new_char
#         else:
#             result += char
#     return result
# # Function to decrypt
# def decrypt(text):
#     result = ""
#     for char in text:
#         if char.lower() in decrypt_dict:
#             new_char = decrypt_dict[char.lower()]
#             result += new_char.upper() if char.isupper() else new_char
#         else:
#             result += char
#     return result
# # Run cipher loop
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
#     message = input("Enter your message:\n")
#     if direction == "encode":
#         print("Encrypted:", encrypt(message))
#     elif direction == "decode":
#         print("Decrypted:", decrypt(message))
#     else:
#         print("Invalid option!")
#     again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
#     if again != 'yes':
#         should_continue = False
#         print("Goodbye!")



# # Advance
# import random
# import json
# import os
# alphabet = [chr(i) for i in range(97, 123)]  # ['a', 'b', ..., 'z']
# # Save cipher key to a file
# def save_key(cipher_key, filename="cipher_key.json"):
#     with open(filename, "w") as file:
#         json.dump(cipher_key, file)
# # Load a cipher key from a file
# def load_key(filename="cipher_key.json"):
#     with open(filename, "r") as file:
#         return json.load(file)
# # Generate a new random cipher key
# def generate_cipher_key():
#     shuffled = alphabet[:]
#     random.shuffle(shuffled)
#     return dict(zip(alphabet, shuffled))
# # Encode message using the cipher key
# def encode_message(text, cipher_key):
#     result = ""
#     for char in text:
#         if char.lower() in cipher_key:
#             encoded = cipher_key[char.lower()]
#             result += encoded.upper() if char.isupper() else encoded
#         else:
#             result += char
#     return result
# # Decode message using the cipher key
# def decode_message(text, cipher_key):
#     reverse_key = {v: k for k, v in cipher_key.items()}
#     result = ""
#     for char in text:
#         if char.lower() in reverse_key:
#             decoded = reverse_key[char.lower()]
#             result += decoded.upper() if char.isupper() else decoded
#         else:
#             result += char
#     return result
# # Main program loop
# print(r"""
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\
# """)
# # Ask user whether to load or generate key
# choice = input("Do you want to (1) generate a new cipher or (2) load an existing one? ").strip()
# if choice == "1":
#     cipher = generate_cipher_key()
#     save_key(cipher)
#     print("A new cipher key has been generated and saved.")
# elif choice == "2":
#     if os.path.exists("cipher_key.json"):
#         cipher = load_key()
#         print("Cipher key loaded from file.")
#     else:
#         print("No existing key found. Generating a new one.")
#         cipher = generate_cipher_key()
#         save_key(cipher)
# else:
#     print("Invalid choice. Exiting.")
#     exit()
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n")
#     if direction == "encode":
#         print(f"Here is the encoded result : {encode_message(text, cipher)}")
#     elif direction == "decode":
#         print(f"Here is the decoded result : {decode_message(text, cipher)}")
#     else:
#         print("Invalid option. Please type 'encode' or 'decode'.")
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye!")



# # ADVANCE & Highly Secure
# import random
# import json
# import os
# import hashlib
# # Create the alphabet
# alphabet = [chr(i) for i in range(97, 123)]  # a-z
# # Save cipher key to a file
# def save_key(cipher_key, filename="cipher_key.json"):
#     with open(filename, "w") as file:
#         json.dump(cipher_key, file)
# # Load a cipher key from a file
# def load_key(filename="cipher_key.json"):
#     with open(filename, "r") as file:
#         return json.load(file)
# # Generate a new random cipher key
# def generate_cipher_key():
#     shuffled = alphabet[:]
#     random.shuffle(shuffled)
#     return dict(zip(alphabet, shuffled))
# # Create a hash ID for a given cipher key
# def get_key_id(cipher_key):
#     key_str = json.dumps(cipher_key, sort_keys=True)
#     return hashlib.sha256(key_str.encode()).hexdigest()[:8]
# # Encode message using the cipher key
# def encode_message(text, cipher_key):
#     result = ""
#     for char in text:
#         if char.lower() in cipher_key:
#             encoded = cipher_key[char.lower()]
#             result += encoded.upper() if char.isupper() else encoded
#         else:
#             result += char
#     return result
# # Decode message using the cipher key
# def decode_message(text, cipher_key):
#     reverse_key = {v: k for k, v in cipher_key.items()}
#     result = ""
#     for char in text:
#         if char.lower() in reverse_key:
#             decoded = reverse_key[char.lower()]
#             result += decoded.upper() if char.isupper() else decoded
#         else:
#             result += char
#     return result
# print(r"""
#   ___ ____   ___   _        ____ ___ ____  _   _ _____ ____
#  |_ _|  _ \ / _ \ | |      / ___|_ _|  _ \| | | | ____|  _ \
#   | || | | | | | || |     | |    | || |_) | |_| |  _| | |_) |
#   | || |_| | |_| || |___  | |___ | ||  __/|  _  | |___|  _ <
#  |___|____/ \___/ |_____|  \____|___|_|   |_| |_|_____|_| \_\
# """)
# # Ask user whether to generate or load key
# choice = input("Do you want to (1) generate a new cipher or (2) load an existing one? ").strip()
# if choice == "1":
#     cipher = generate_cipher_key()
#     save_key(cipher)
#     key_id = get_key_id(cipher)
#     print(f"A new cipher key has been generated and saved. Share this secret key ID with the receiver: {key_id}")
# elif choice == "2":
#     if os.path.exists("cipher_key.json"):
#         cipher = load_key()
#         key_id = get_key_id(cipher)
#         entered_key = input("Enter the secret key ID: ").strip()
#         if entered_key != key_id:
#             print("Wrong key ID. Exiting for safety.")
#             exit()
#         else:
#             print("Cipher key loaded successfully.")
#     else:
#         print("No existing key found. Generating a new one.")
#         cipher = generate_cipher_key()
#         save_key(cipher)
#         key_id = get_key_id(cipher)
#         print(f"New cipher generated. Share this secret key ID: {key_id}")
# else:
#     print("Invalid choice. Exiting.")
#     exit()
# # Cipher Loop
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n")
#     if direction == "encode":
#         print(f"Encrypted message: {encode_message(text, cipher)}")
#         print(f"Share this key ID with the receiver: {key_id}")
#     elif direction == "decode":
#         print(f"Decrypted message: {decode_message(text, cipher)}")
#     else:
#         print("Invalid option. Please type 'encode' or 'decode'.")
#     restart = input("Type 'yes' to go again. Otherwise type 'no':\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye!")

