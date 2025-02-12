import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
symbols=['!', '@', '#', '$', '%', '^', '&', '*']

# password=" "
print("welcome to password generator")
letter_new=int(input("how many letters would you like in your password \n"))
nr_symbols= int(input("how many symbols would you like\n"))
nr_numbers = int(input("how many numbers would you like\n"))

# for char in range(1, letter_new + 1):
#     random_char=random.choice(letters)
#     #print(random_char)
#     password =password+random_char
# print(password)
#
# for char in range(1,nr_symbols + 1):
#     random_symbols=random.choice(symbols)
#     password =password+random_symbols
# print(password)
#
# for i in range(1,nr_numbers + 1):
#     new_numbers=random.choice(numbers)
#     password =password+str(new_numbers)
# print(password)
password = []
for char in range(0, letter_new):

    password.append(random.choice(letters))


for char in range(1,nr_symbols + 1):
    random_symbols=random.choice(symbols)
    password.append(random_symbols)


for i in range(0,nr_numbers):

    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
password_list=""
for i in password:
    password_list+=str(i)
print(password_list)