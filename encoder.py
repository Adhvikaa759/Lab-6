def encode(password):
    encoded_pass = ""
    for digit in password:
        #loop for shifting the digit by 3
        encoded_digit = (int(digit)+ 3) % 10
        encoded_pass += str(encoded_digit)
    return encoded_pass


def decode(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        decoded_digit = (int(digit)-3) % 10
        decoded_pass += str(decoded_digit)
    return decoded_pass

def main():
    while True:
        print("Menu:")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            password = input("Enter an 8-digit password to encode: ")
            encoded_pass = encode(password)
            print(f"Encoded password: {encoded_pass}")
        elif choice == "2":
            encoded_pass=input("Enter the encoded password to decode: ")
            decoded_pass = decode(encoded_pass)
            print(f"Decoded password: {decoded_pass}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()