# Gage Carlson

def encode(password):
    new_pass = ""
    for char in password:
        char = int(char)
        char += 3
        char = str(char)
        new_pass += char
    return new_pass

def encode(password):
    decodedPass = ""
    for num in password:
        decodedPass += str(int(num) - 3)
    return decodedPass
 
while True:

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("Please enter an option: ")
    if choice == "1":
        password = input("Please enter your password to encode: ")
        password = encode(password)
        print("Your password has been encoded and stored!")
    elif choice == "2":
        dec_password = decode(password)
        print(f"The encoded password is {password}, the original password is {dec_password}")
    elif choice == "3":
        break