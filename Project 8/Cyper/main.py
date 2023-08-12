import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ' ','0','1','2','3','4','5','6','7','8','9']


def encrypt(text, shift):
    newText = ""
    for char in text:
        if char not in alphabet:
            newText += char
        else:
            indexNumber = alphabet.index(char) + shift

            if (indexNumber < len(alphabet)):
                newText = newText + alphabet[indexNumber]
            else:
                indexNumber = indexNumber - len(alphabet)
                newText = newText + alphabet[indexNumber]
    print(f"Your decryted massage is: {newText}")
# zxyabc ecdfgh


def decrypt(text, shift):
    newText = ""
    for char in text:

        if char not in alphabet:
            newText += char
        else: 
            indexNumber = alphabet.index(char)
            if (indexNumber < shift):
                indexNumber = alphabet.index(char) - shift

                indexNumber = len(alphabet) + indexNumber
                newText = newText + alphabet[indexNumber]
            else:
                indexNumber = alphabet.index(char) - shift
                newText = newText + alphabet[indexNumber]

    print(f"Your encrypted massage is: {newText}")


status = False
print(art.logo)
while not status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    if (direction == "encode"):
        encrypt(shift=shift_input, text=text_input)
    elif (direction == "decode"):
        decrypt(shift=shift_input, text=text_input)
    else:
        print("Wrong input try again\n")
    again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if (again == "no"):
        status = True
