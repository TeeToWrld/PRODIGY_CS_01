def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(char) - base + shift) % 26
            encrypted_text += chr(base + shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            deshift = (ord(char) - base - shift) % 26
            encrypted_text += chr(base + deshift)
        else: 
            encrypted_text += char
    return encrypted_text

def main():
  while True:
       User_Input = input("Type 'Encrypt' for Encryption and 'Decrypt' for Decryption:   ").strip().lower()
       if User_Input == "encrypt":
        text = input('What text do you want to encrypt? ')
        while True:
          try:
           shift = int(input("Enter the Shift number: "))
           break
          except ValueError:
            print("Invalid input... Enter an integer")

        result = encrypt(text, shift)
        print("Encrypted Text: " ,result)

       elif User_Input == 'decrypt':
        text = input('What text do you want to decrypt? ')

        while True:
            try:
             shift = int(input("Enter the Shift number: "))
             break
            except ValueError:
                print("Invalid input... Enter an integer")

        result = decrypt(text, shift)
        print("Decrypted Text: ", result)
       elif User_Input == 'exit':
           print("Goodbye")
           break
   

       else:
          print('Your Response was Invalid .. Try again or Type exit to stop')
 
   

if __name__ == '__main__':
    main()
    

