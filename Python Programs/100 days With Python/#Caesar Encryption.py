alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction,text,shift):
    decipher_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            decipher_text += alphabet[shifted_position]
        else:
            decipher_text += letter
    print(f"Here is the {direction}d result: {decipher_text}")

repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction,text,shift)
    repeat = input("Type 'yes' to continue:\n").lower()
