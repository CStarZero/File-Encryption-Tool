from cryptography.fernet import Fernet

def encrypt_file(file_path, key, output_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key, output_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data)
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)

# Prompt user for inputs
input_file = input("Enter the path of the input file: ")
key = input("Enter the encryption/decryption key: ")
output_file = input("Enter the path of the output file: ")

# Encrypt or decrypt based on user input
choice = input("Encrypt (E) or Decrypt (D) the file? ")
if choice.lower() == 'e':
    encrypt_file(input_file, key, output_file)
    print("File encrypted successfully.")
elif choice.lower() == 'd':
    decrypt_file(input_file, key, output_file)
    print("File decrypted successfully.")
else:
    print("Invalid choice.")
