from random import randint
from datetime import datetime
def magic8():
    outcomes = ["It is certain","It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good","Yes","Signs point to yes","Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predct now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no","Outlook not so good", "Very doubtful"]
    i = randint(0,len(outcomes)-1)
    print(outcomes[i])
    return outcomes[i]

def entry(string):
    f = open('journal.txt', 'a')
    date = str(datetime.now().strftime("%A")) + " " +str(datetime.now().strftime("%B")) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
    f.write(date + "\n")
    f.write(string + "\n")
def getGoogleInfo(string):
    query = ""
    if 'google search' in string:
        for i in range(string.index('google search')+ 18, len(string)):
            query+= string[i]
    elif 'google' in string:
        for i in range(string.index('google')+ 10, len(string)):
            query+= string[i]
    print(query)
    return query