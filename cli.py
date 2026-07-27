import sys
from ciphers import caesar, vigenere, playfair, affine, rail_fence, hill

def print_header():
    print("=" * 60)
    print("      CLASSICAL CIPHERS ALL-IN-ONE TOOLKIT       ")
    print("=" * 60)

def show_menu():
    print("\nSelect a Cipher:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Affine Cipher")
    print("4. Playfair Cipher")
    print("5. Rail Fence Cipher")
    print("6. Hill Cipher")
    print("0. Exit")

def get_mode():
    while True:
        mode = input("\nChoose Mode - (E)ncrypt or (D)ecrypt: ").strip().upper()
        if mode in ['E', 'D']:
            return mode
        print("[-] Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.")

def run_cli():
    print_header()
    
    while True:
        show_menu()
        choice = input("\nEnter choice (0-6): ").strip()

        if choice == '0':
            print("\nExiting Classical Ciphers Toolkit. Goodbye!")
            sys.exit(0)

        if choice not in [str(i) for i in range(1, 7)]:
            print("[-] Invalid option. Please select between 0 and 6.")
            continue

        mode = get_mode()
        text = input("Enter text: ").strip()

        # Caesar Cipher
        if choice == '1':
            shift = int(input("Enter shift value (e.g., 3): "))
            result = caesar.encrypt(text, shift) if mode == 'E' else caesar.decrypt(text, shift)
            
        # Vigenère Cipher
        elif choice == '2':
            key = input("Enter keyword: ").strip()
            result = vigenere.encrypt(text, key) if mode == 'E' else vigenere.decrypt(text, key)

        # Affine Cipher
        elif choice == '3':
            a = int(input("Enter key 'a' (must be coprime with 26): "))
            b = int(input("Enter key 'b': "))
            result = affine.encrypt(text, a, b) if mode == 'E' else affine.decrypt(text, a, b)

        # Playfair Cipher
        elif choice == '4':
            key = input("Enter keyword: ").strip()
            result = playfair.encrypt(text, key) if mode == 'E' else playfair.decrypt(text, key)

        # Rail Fence Cipher
        elif choice == '5':
            rails = int(input("Enter number of rails: "))
            result = rail_fence.encrypt(text, rails) if mode == 'E' else rail_fence.decrypt(text, rails)

        # Hill Cipher
        elif choice == '6':
            key = input("Enter key matrix or string: ").strip()
            result = hill.encrypt(text, key) if mode == 'E' else hill.decrypt(text, key)

        print("-" * 40)
        print(f"[+] Result ({'Encryption' if mode == 'E' else 'Decryption'}): {result}")
        print("-" * 40)
