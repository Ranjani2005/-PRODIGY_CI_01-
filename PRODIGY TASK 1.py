
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    
    return encrypted_text
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    
    return decrypted_text
if __name__ == "__main__":
    # Get user input
    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value: "))

    encrypted_message = encrypt(message, shift_value)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift_value)
    print(f"Decrypted Message: {decrypted_message}")
