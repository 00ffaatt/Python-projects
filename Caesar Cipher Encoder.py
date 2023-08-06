# Encodes Caesar Cipher to input text


# Encoder will convert all alphabetical letters and leave other characters alone
# Negative steps are also allowed as inputs
def CC_encoder(input:str, steps: int):
    new_word = ''
    
    for char in input.lower():
        if char.isalpha():
            newdex = 0
            if ord(char) + steps > 122:
                newdex = ord(char) + steps - 26
            elif ord(char) + steps < 97:
                newdex = ord(char) + steps + 26
            else:
                newdex = ord(char) + steps
            new_word += chr(newdex)
        else:
            new_word += char
            
    
    return new_word


# Using the function
print(CC_encoder('hello 293847239847239world aaaa!', -1))
    