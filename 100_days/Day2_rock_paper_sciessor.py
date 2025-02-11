import random



rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """
scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

user_choice = int(input("please provide input 0 for rock,1 for paper,2 for scissors"))
print(user_choice)

new_list1=random.randint(0,2)
print(new_list1)

if user_choice ==0 and new_list1==2:
    print("user won")
elif user_choice<new_list1:
    print("you loose")
elif user_choice ==new_list1:
    print("it's draw")