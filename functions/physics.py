from functions.InfoPack import InfoPack
def find_Num(string):
    isNum = False
    for i in range(0,len(string)):
        for n in range(0,10):
            if string[i] == str(n):
                isNum = True
            if isNum:
                return i
def pounds_grams(string):
    num=find_Num(string)
    num2 = ""
    for i in range(int(num),len(string)):
        for n in range(0,10):
            if string[i] == str(n):
                num2+= string[i]
    sum = int(num2) * 453.592
    print(str(sum) + " grams")
    return str(sum)

def grams_pounds(string):
    num=find_Num(string)
    num2 = ""
    for i in range(int(num),len(string)):
        for n in range(0,10):
            if string[i] == str(n):
                num2+= string[i]
    sum = int(num2) / 453.592
    print (str(sum) + " pounds")
    return str(sum)

def cal_thrust(velocity,mass,time):
    thrust = velocity* (mass/time)
    print(thrust)
    return thrust

def getThrustInfo(string):
    things = []
    vars = ['velocity', 'mass']
    currentString =''
    lastdex = 0
    for i in range(0,len(string)):
        currentString+= string[i]
        for var in vars:
            if var in currentString:
                things.append(var)
                currentString = ''
    for t in range(0,len(things)):
        if t <= len(things)-2:
            for i in range(string.index(things[t]), string.index(things[t+1])):
                if not string[i].isalpha() and not string[i] == " ":
                    things[t]+= string[i]
                lastdex= i
        else:
            for i in range(string.index(things[t]), len(string)):
                if not string[i].isalpha() and not string[i] == " ":
                    things[t]+= string[i]
    for var in vars:
        found = False
        for thing in things:
            if var in thing:
                found = True
        if not found:
            things.append(var)
    ThrustInfo = InfoPack(things)