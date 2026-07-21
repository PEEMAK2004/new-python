'''inchar = input("Input one character:")
if inchar >= 'A' and inchar <= 'Z':
    print("You input Upper Case Letter", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You input Lower Case Letter", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input Number", inchar)
else:
    print("It's not a letter or number.", inchar)'''


'''inchar = input("Input two character:")
if inchar[0] >= 'A' and inchar[0] <= 'Z':
    print("You input Upper Case Letter", inchar[0])
if inchar[1] >= 'A' and inchar[1] <= 'Z':
    print("You input Upper Case Letter", inchar[1])
elif inchar[0] >= 'a' and inchar[0] <= 'z':
    print("You input Lower Case Letter", inchar[0])
elif inchar[1] >= 'a' and inchar[1] <= 'z':
    print("You input Lower Case Letter", inchar[1])
elif inchar[0] >= '0' and inchar[0] <= '9':
    print("You input Number", inchar[0])
elif inchar[1] >= '0' and inchar[1] <= '9':
    print("You input Number", inchar[1])
else:
    print("It's not a letter.", inchar)'''


inchar = input("Input two character:")
if inchar[0:2] >= 'A' and inchar[0:2] <= 'Z':
    print("You input Upper Case Letter", inchar[0:2])
elif inchar[0:2] >= 'a' and inchar[0:2] <= 'z':
    print("You input Lower Case Letter", inchar[0:2])
elif inchar[0:2] >= '0' and inchar[0:2] <= '9':
    print("You input Number", inchar[0:2])
else:
    print("It's not a letter.", inchar)
