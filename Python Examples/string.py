A="hello"
B="world"
C=A+" "+B
c=1
print("C=",C," c=",c)
print(C.upper())
D=C.split(" ",2)      # prints the value of C as uppercase but does not change it
print(D)              # this results in a list of two items at positions 0 and 1 
print(D[0])
print(D[1])
