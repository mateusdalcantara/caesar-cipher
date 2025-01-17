from com.mateusdalcantara.resources.logo import logo
import random
"""
Caesar Cipher Encryption/Decryption Script

This script implements the Caesar cipher algorithm, which allows 
users to encrypt and decrypt messages by shifting the letters of the 
alphabet by a specified number of positions.

### Overview:
The script performs two operations: encryption and decryption. The user is 
prompted to choose an operation, input a message, and provide a shift value. 
Based on these inputs, the script applies the Caesar cipher to either encrypt 
or decrypt the message.

### Caesar Cipher:
The Caesar cipher works by shifting each letter in the input message 
by a given number of positions. For example:

- With a shift of 4:
    - 'a' becomes 'e', 'b' becomes 'f', 'c' becomes 'g', etc.
- For decryption, the shift is reversed (negative shift).

### Example:
**Encryption**:
- Input message: "boiled eggs"
- Shift: 4
- Encrypted message: "fsmpih ikkw"

**Decryption**:
- Input message: "fsmpih ikkw"
- Shift: 4
- Decrypted message: "boiled eggs"

The script handles non-alphabetic characters 
(e.g., spaces, punctuation) by leaving them unchanged.

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Display the Caesar cipher logo as ASCII art
print(logo)


def caesar(original_text, shift_amount, encode_or_decode):
    """
    Applies the Caesar cipher to encrypt or decrypt a given message.

    The Caesar cipher works by shifting each letter of the input text by a
    specified number of positions in the alphabet. For encryption, the shift is
    applied forward (i.e., letters are moved to the right), and for decryption,
    the shift is applied backward (i.e., letters are moved to the left).

    The function uses the following steps:
    1. It finds the position of each letter in the alphabet using the
    alphabet.index(letter) method.
    2. The shift amount is then added (or subtracted for decryption) to this position.
    3. The result is wrapped around using the modulo operator to ensure the
    position stays within the bounds of the alphabet.
    4. The letter is then replaced by the letter at the new shifted position.

    Non-alphabetic characters (such as spaces, punctuation, etc.) are not
    modified and are appended to the result as is.

    Parameters:
    - original_text (str): The text to be encrypted or decrypted.
    - shift_amount (int): The number of positions to shift each letter in the alphabet.
    - encode_or_decode (str): Determines whether to 'encode' (encrypt) or
    'decode' (decrypt) the message. Should be either "encode" or "decode".

    Returns:
    - str: The encrypted or decrypted text, depending on the operation chosen.

    Example:
    >>> caesar("boiled eggs", 4, "encode")
    "fsmpih ikkw"

    >>> caesar("fsmpih ikkw", 4, "decode")
    "boiled eggs"
    """

    output_text = ""

    # If the operation is 'decode', reverse the shift by making shift_amount negative
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Process each letter in the original text
    for letter in original_text:

        if letter not in alphabet: # Keep non-alphabet characters unchanged
            output_text += letter
        else:
            # Shift the letter's position in the alphabet and wrap around if necessary
            shifted_position = alphabet.index(letter) + shift_amount
            # move forward or backword on the alphabet in the case of overflow 0 - 25(a - z)
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    # Output the result of the encoding/decoding operation
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main loop to continuously interact with the user
while True:
    # Prompt the user to choose between encryption and decryption
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Prompt the user for the text to be encrypted or decrypted
    text = input("Type your message:\n").lower()

    # Prompt the user for the shift value (how many positions to shift)
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function with the user's inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to perform another operation
    resp = input("Type 'y' if you want to go again. Otherwise type 'n'")

    # Exit the loop if the user chooses 'n'
    if resp.lower() == "n":
        print("Goodbye")
        break
