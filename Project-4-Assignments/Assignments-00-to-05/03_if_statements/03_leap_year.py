#Problem Statement
#Write a program that reads a year from the user and tells whether a given year is a leap year or not.
#
#A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.
#
#In the Gregorian calendar, three criteria must be checked to identify leap years:
#
#The given year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is NOT a leap year; unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."


#2024 % 4 == 0 ✅
#2024 % 100 == 0 ❌ →To sidha "That's a leap year!" print

#1900 % 4 == 0 ✅
#1900 % 100 == 0 ✅
#1900 % 400 == 0 ❌ → So not a leap year

#2000 % 4 == 0 ✅
#2000 % 100 == 0 ✅
#2000 % 400 == 0 ✅ → So leap year

#Woh 4 se divide ho.
#→ agar nahi ho, to seedha -> "not a leap year"
#Lekin agar woh 100 se bhi divide ho jaye, to:
#Ab wo leap year nahi hai... ❌
#
#Sirf tab hoga agar wo 400 se bhi divide ho. ✅






print("\t📝 Leap Year Checker")
print("_." * 30 ,"\n")
print("📅 Leap Year Checker")

def main():
    year = int(input("📝 Enter a year: "))

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("\n✨🌟✨ That's a leap 📆 year! 🌟")
            else:
                print("\n📆 That's not a leap year.")
        else:
            print("\n✨🌟✨ That's a leap year! 🌟")
    else:
        print("\n📆 That's not a leap year.")



if __name__ == "__main__":
    main()
