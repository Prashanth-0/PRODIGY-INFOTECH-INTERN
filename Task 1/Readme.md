# Caesar Cipher Tool

This is a Python script that provides encryption and decryption using the Caesar Cipher algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage

### Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/Prashanth-0/PRODIGY-INFOTECH-INTERN.git


### Command Line Options
The script supports the following command line options:


- `-m,` `--mode`     Specifies the mode of operation.
            encrypt: Encrypts the message using the Caesar Cipher.
            decrypt: Decrypts the message using the Caesar Cipher.

- `-s,` `--shift`    Specifies the shift value (a number between 1 and 25).
            Example: -s 3 (Shift the characters by 3 positions).

- `message|        Specifies the message to be encrypted or decrypted.
            Enclose the message in quotes if it contains spaces or special characters.
