'''0.Shortcut for comment out in python'''
# ctrl+/

'''1.Simple print command'''
# print("Hello world")
# print("JUET Guna")

'''2.Taking variables'''
# firstname="Tony"
# lastname="Stark" 
# age="51"

'''3.Print the variables'''
# is_genius = True
# print(firstname)
# print(lastname)
# print(age)
# print(is_genius)

'''4.taking input from user'''
# name = input("What's your name? ")
# print(name)
# print("Hello " + name)   '''CONCATENATION'''

'''Asking Tony for his Superhero name'''
# print("Hello Tony")
# name=input("What's your SuperHero name? ")
# print(name)

'''5.Type conversion'''
# old_age=input("What is your old age: ")
# new_age= int(old_age) + 2
# print(new_age)

# float() 
# number=18
# print(float(18))
# str()
# bool()

'''6.Print the algebra of two variables'''
# a=input("enter first number= ")
# b=input("enter second number= ")

# sum=int(a) + int(b)
# diff=int(a) - int(b)
# pro=int(a) * int(b)
# div=int(a) / int(b)

# print("sum= " + str(sum))
# print("diff= " + str(diff))
# print("pro= " + str(pro))
# print("div= " + str(div))

'''7.STRINGS'''

# name = "Dheeraj Verma"

# print(name.upper())
# print(name.lower())
# print(name.find('V'))   # ans is 8 bcoz position starts from 0
# print(name.replace("Dheeraj Verma" , "Arun Verma"))
# print(name.replace("Verma" , "Rajpoot"))
# print(name)

# print('Dheeraj' in name)
# print('D' in name)
# print('S' in name)

'''8.Arithmatic operators in Python'''

# print(5 +  2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

'''9.SHORTCUTS'''

# i = 5                  #OPERATOR PRECEDENCE LIKE BODMAS

# i = i + 3
# i += 3
# i -= 3
# i *= 3
# i /= 5      

# result = 2 + 3 * 5
# print(result)

'''10.COMPARISON OPERATORS'''

# print(3 > 2)      #True
# print(3 >= 2)     #True
# print(2 <= 0)     #False
# print(3 == 2)       #False

'''11.Logical operators'''

# print(3>2 or 5>6)    #True
# print(3 != 2)        #True
# print(not 2>3)       #True


'''12.If-Else statement in Python'''

# age=input("What's your age= ")
# print(age)

# if int(age) >= 18 :
#     print("You are adult.")               #here we used intentation
#     print("You can Vote.")    
# elif int(age)<18 and int(age)>3:
#     print("You are a child.")
#     print("Go to School.")   
# else:
#     print("You are a kid.")     

'''13.Making Calculator'''

# first=input("enter first number= ")
# second=input("enter second number= ")
# operator=input("enter operator (+,-,*,/,%)= ")
   #Hum pehle bhi variables me integral vale assign kar sakte the aisa na karne pur code time consuming ho jate hai
   #first=int(first)
   #second=int(second)

# if operator == "+":
#     print(int(first) + int(second))
# elif operator == "-":    
#     print(int(first) - int(second))
# elif operator == "*":
#     print(int(first) * int(second))
# elif operator == "/":
#     print(int(first) / int(second))
# elif operator == "%":
#     print(int(first) % int(second))
# else:
#     print("invalid syntax")

'''14.RANGE IN PYTHON'''
# a=range(5)
# print(a)

'''15.Loops in python'''
   #while loop

# i =1
# while i <= 10:
#     print(i)          #use intentation otherwise code will not run
#     i=i+1             #this line is to end the program otherwise 1  will be printed infinite times till it crashes the system


# i =1
# while i <= 5:
#      print(i * "*")          
#      i=i+1             #this line is to end the program otherwise 1  will be printed infinite times till it crashes the system

# i =5
# while i >= 0:
#     print(i * "*")
#     i=i-1 

    #for loop



