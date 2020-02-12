inp = input("input some text here please:\n").lower()

key = int(input("Input the key you want to use from 2 and 25:\n"))
def rot13(input,key):
    if key > 25:
        key = 25
    elif key < 2:
        key = 2
    finaltext = ""
    for letter in input:
        if letter.isalpha():
            num = ord(letter)
            if (num + key) > 122:
                x = (num + key) - 122
                finaltext += chr(x + ord("a") -1)
            else:
                finaltext += chr(num + key)
        else:
            finaltext += letter
    print(finaltext)


rot13(inp,key)