error = "Unconclusive, Try Again"
numbers = ["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten"]
def math(string):
    try:
        num1=""
        num2=""
        isFloat = False
        sign = ""
        if "+" in string:
            sign = "+"
        if "-" in string:
            sign = "-"
        if "*" in string:
            sign = "*"
        if "/" in string:
            sign = "/"
        for i in range (0,string.index(sign)):
            for n in range (0,10):
                if n<9:
                    if string[i] == str(n):
                        num1+= string[i]
                else:
                    if string[i]==".":
                        isFloat = True
                        num1+= string[i]
        for i in range (string.index(sign),len(string)):
            for n in range (0,10):
                if n<9:
                    if string[i] == str(n):
                        num2+= string[i]
                else:
                    if string[i]==".":
                        isFloat = True
                        num2+= string[i]
        if "+" in string:
            if isFloat:
                print(float(num1) + float(num2))
                return str(float(num1) + float(num2))
            else:
                print(int(num1) + int(num2))
                return str(int(num1) + int(num2))
        elif "-" in string:
            if isFloat:
                print(float(num1) - float(num2))
                return str(float(num1) - float(num2))
            else:
                print(int(num1) - int(num2))
                return str(int(num1) - int(num2))
        elif "*" in string:
            if isFloat:
                print(float(num1) * float(num2))
                return str(float(num1) * float(num2))
            else:
                print(int(num1) * int(num2))
                return str(int(num1) * int(num2))
        elif "/" in string:
            if isFloat:
                print(float(num1) / float(num2))
                return str(float(num1) / float(num2))
            else:
                print(int(num1) / int(num2))
                return str(int(num1) / int(num2))
    except:
        return error
def word_to_int(string):
    for i in range(0,10):
        if numbers[i] in string:
            return i + 1 