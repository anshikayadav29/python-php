# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()




year =2000
if (year %400==0)and(year % 100 == 0):
    print("{0} is a leap year".format(year))
elif(year % 4 ==0) and (year % 100 !=0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is a leap year ".format(year))





