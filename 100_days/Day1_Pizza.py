print("Welcome to the Pizza Hut")
size=input("What size of Pizza you want?  S,M,L \n")

pep=input("Do you want peperronie on your Pizza?? Y  or N")

cheeze =input("Do u want extra cheeze on your Pizza? Y or N")
#how much they need to pay based on size
#how much to add to bill to add peperoni on the pizza
#how much to add to bill to add cheeze to pizza
bill =0
if size == 'S':
    bill+=15
    print("please pay $15")
elif size =='M':
    bill+=20
    print("please pay $20")
elif size == 'L':
    bill+=25
    print("please pay $25")
else:
    print("its invalid input")

if pep == "Y":
    if size =='S':
     bill+=2
     print(f"total amount to pay is :${bill}")
    else:
        bill+=3
        print(f"please pay total: {bill}")

if cheeze =='Y':
        bill+=1
        print(f"Total amount with cheeze is:{bill}")
else:
        print(f"total amount is {bill}")






