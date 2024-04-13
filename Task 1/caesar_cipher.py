import argparse

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord('A' if char.isupper() else 'a') + (ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26
            result += chr(shifted)
        else:
            result += char

    return result if mode == "encrypt" else result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher encryption and decryption tool.")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], required=True, help="Mode of operation: encrypt or decrypt")
    parser.add_argument("-s", "--shift", type=int, required=True, help="Shift value (a number between 1 and 25)")
    parser.add_argument("message", help="Message to be encrypted or decrypted")

    args = parser.parse_args()

    if args.shift < 1 or args.shift > 25:
        print("Shift value must be between 1 and 25.")
        return

    if args.mode == "encrypt":
        encrypted_message = caesar_cipher(args.message, args.shift, "encrypt")
        print("Encrypted message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher(args.message, -args.shift, "decrypt")
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
