#Problem Statement
#Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
#
#The first even number is 0:
#
#0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


print("\t📝 The first 20 even numbers are: ")
print("_." * 30 ,"\n")

for i in range(20):                #i * 2 h chay i kuch b ho,jesay 0*2, 1*2, 2*2, 3*2, 4*2, 5*2.....19*2
    print(i * 2 , end=" ")      #end=" " ka matlab hai:"Print ke baad nayi line mat do — bas ek space de do.
