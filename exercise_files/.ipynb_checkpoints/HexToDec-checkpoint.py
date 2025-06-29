# Python code​​​​​​‌​‌‌‌​‌​​‌‌​‌​‌‌​​‌‌‌‌‌‌​ below

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    length=len(hexNum)

    # Validate each item exists as a hex number, if not exit
    # there should not be any spaces.
    if ' ' in hexNum:
        print('The string contains spaces', hexNum)
        return None
    else:
        for item in hexNum:
            if item not in hexNumbers:
                return None

    # Reverse the list so that the positon lines up with the exponent value, 
    # i.e first place is exponent 0, second placement is exponent 1.
    b = list(reversed(hexNum))

    # initialize variables
    position = 0
    total = 0

    # For loop to figure out the place of each item and do the math.
    for each in b:
        # do the math?
        summary = hexNumbers[each] * (16 ** position)
        #increment postion
        position = position + 1
        total = total + summary
    
    print(type(total))
    return(total)
    
    pass


hexToDec('AB')
