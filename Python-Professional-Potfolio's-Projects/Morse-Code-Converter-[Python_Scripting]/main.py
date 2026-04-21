morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' '
}

def text_to_morse():
    is_running = True
    while is_running:
        user_input = input("Enter text to convert to Morse Code: ").upper()

        morse_output = ""
        for char in user_input:
            if char in morse_code_dict:
                if char == ' ':
                    morse_output += "   "
                else:
                    morse_output += morse_code_dict[char] + " "
            else:
                morse_output += char + " "

        print(f"Morse Code: {morse_output.strip()}")

        again = input("\nConvert another message? (yes/no): ").lower()
        if again != 'yes':
            is_running = False


if __name__ == "__main__":
    text_to_morse()