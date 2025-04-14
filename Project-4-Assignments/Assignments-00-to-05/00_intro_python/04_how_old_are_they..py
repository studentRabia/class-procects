#Problem Statement
#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

#Anton is 21 years old.

#Beth is 6 years older than Anton.

#Chen is 20 years older than Beth.

#Drew is as old as Chen's age plus Anton's age.

#Ethan is the same age as Chen.







anton:int = 21
beth:int = anton + 6
chen:int = beth + 20
drew:int = chen + anton
ethan:int = chen


print("🧩 Welcome to the Age Riddle!")
print("==================================\n")
print("Anton is " + str(anton) + " years old")

#result will be same as above but with different formatting
print("📢  Anton is " + str(anton)," year old")
print("📢 Beth is " + str(beth)," year old")
print("📢 Chen is " + str(chen)," year old")
print("📢 Drew is " + str(drew)," year old")
print("📢 Ethan is " + str(ethan)," year old")

# error will be raised if we try to concatenate a string with an int directly
print(f"\nAnton is {anton}")
print(f"Beth is {chen}")
print(f"Drew is {drew}")
print(f"Ethan is  {ethan}")