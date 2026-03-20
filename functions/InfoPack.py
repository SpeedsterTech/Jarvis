class InfoPack:
    def __init__(self,things):
        self.properties={}
        for thing in things:
            num = ""
            word = ""
            for i in range(0,len(thing)):
                if thing[i].isalpha():
                    word += thing[i]
                else:
                    num+= thing[i]
            self.properties[word] = num
        print(self.properties)
