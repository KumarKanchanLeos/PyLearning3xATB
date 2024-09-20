# input_1 = input("Enter the first number: ")
# input_2 = input("Enter the second number: ")
# input_1= int(input_1)
# input_2 = int(input_2)
# print(input_1 + input_2)

pi = 3.14
print(type(pi))

i = 10
i2 = 12
print(type(i))
print(type(i2))
print(i2/i)
result = i2/i
print(type(result))

dir = r"c:\nomed\some dir"
print(type(dir))
print(dir)

#format of the string
first_name= "June"
last_name = "David"
print(first_name + " " +last_name)
print(f'your name is {first_name} {last_name}')

#printing the tanle of 5
num = 5
print(f"{num}*1 = {num*1}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")
for i in range(11):
    print(f"{num}*i = {num*i}")
    num = int(num)
    print(num)
    print("2*{},{}={}".format(num,num*2,i))

name = "kanu" #length starts from 1
print(len(name))
name = name.upper()
print(name)
name = 'radhika'
print(name.find('a'))
print(name[0])
name = "this is a big line"
print(len(name))
print(name[14])
print(name[-1])
print(id(name))
val = None
print(val)
print(type(None))

print(id(val))

shopping= ["milk","bread","Poha","butter"]
print(shopping[0])

print(len(shopping))
print(type(shopping))
my_list = [1,2,3,True,"Kanchan"]
print(my_list)
print("hello \"world\"")
print("hello \nworld")
print("hello \tworld")




