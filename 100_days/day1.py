# # #print("hello\t"+input("whats your name")+"!")
# #
# # new_var1= "welcome to the Band Name Generator"
# # print(new_var1)
# # new_var2=input("What's the name of the city your grew up in?")
# # print(new_var2)
# # new_var3=input("What's your pet's name")
# # print(new_var3)
# # print("your band name could be :" +new_var2+" " +new_var3)
#
#roller coaster ride control flow
print("welcome to roller coaster ride")
height = int(input("please enter your height"))
print(height)
bill = 0
if height >=120:
    print("please go ahead for ride")
    age = int(input("what's your age: \n"))
    if age <12:
        bill=5
        print("pay $5")
    elif 12<=age <=18:
        bill = 7
        print("pay $7")
    else:
         bill = 12
         print("pay $12")

    want_photos=input("do u want to take photos? type yes or no")
    if want_photos =='yes':
        #add $3 to their bill
        bill+=3
        print(f"please pay ${bill}")
else:
    print("you can't ride due to height policy")
#
#
#import math

# num1=int(input("please type 1 number: \n"))
# if num1%2==0:
#     print("num1 is even")
# else:
#     print("num1 is odd")
