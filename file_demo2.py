file = open("demo.txt",'w')
file.write("Did I ever tell you the definition of insanity?")
file.close()
file = open("demo.txt",'r')
print(file.read())
file.close()
file = open("demo.txt",'a')
file.write("\nInsanity is doing the exaxct same shit over and over again expecting shit to change")
file.close()
file = open("demo.txt",'r')
print(file.read())
file.close()