import main as mn
import sys
l = len(sys.argv[1])
file = open('answer.txt','w')
file.write("")
if l>0:
    file = open("answer.txt",'a')
    file.write(str(mn.getquery(False,sys.argv[1])[0])+ "\n")
file.close()