import random

inp=int(input("ENTER YOUR INPUT :"))
com=random.randint(0,2)
if(com==0):
    print("COMPUTER CHOICE IS ROCK")
elif(com==1):
    print("COMPUTER CHOICE IS PAPER")
else:
    print("COMPUTER CHOICE IS SICCSSOR")
if(inp==com):
    print("DRAW")
elif(inp==0 and com==1)or(inp==1 and com==2)or(inp==2 and com==0):
    print("COMPUTER WINS")
else:
    print("YOU WON")