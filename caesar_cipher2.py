def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = shift if mode == 'encrypt' else -shift
            shifted = (ord(char) - base + shift_amount) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

# --- Main Program ---
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed): {output}")
else:
    print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
