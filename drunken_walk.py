# write a code to simulate drunken walk for the network given in missing sem.

#A goes to B and C
#B goes to D and E
#C goes to F and G
#D goes to H and A
#E goes to H and A
#F goes to A
#G goes to A
#H goes to A

import random

# creating variables for each position and assigining them zero initial value
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0


# setting initial location at A
location="A"

for i in range(1000000):#to repeat the following 1000000 times
    
    

    # if drunkard lands on  A, add 1 to A and randomly go to either B or C
    if location=="A":
        A=A+1
        
        if random.randint(0,1)==0:
            location="B"
        else:
            location="C"
    # if drunkard lands on B, add 1 to B and randomly go to either D or E
    elif location=="B":
        B=B+1
        if random.randint(0,1)==0:
            location="D"
        else:
            location="E"

    # if drunkard lands on C, add 1 to C and randomly go to either F or G
    elif location=="C":
        C=C+1
        if random.randint(0,1)==0:
            location="F"
        else:
            location="G"
    
    # if drunkard lands on D, add 1 to D and randomly go to either H or A
    elif location=="D":
        D=D+1
        if random.randint(0,1)==0:
            location="H"
        else:
            location="A" 

    # if drunkard lands on E, add 1 to E and randomly go to either H or A
    elif location=="E":
        E=E+1
        if random.randint(0,1)==0:
            location="H"
        else:
            location="A"
    
    # if drunkard lands on F, add 1 to F and go to A
    elif location=="F":
        F=F+1
        location="A"

    # if drunkard lands on G, add 1 to G and go to A
    elif location=="G":
        G=G+1
        location="A"   

    # if drunkard lands on H, add 1 to H and go to A
    elif location=="H":
        H=H+1
        location="A"


print(A, B, C, D, E, F, G, H)
