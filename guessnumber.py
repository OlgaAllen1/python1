# print ("Hello world")
#
# name = "Olga"
# print (name)
# name = input ( "what is your name?")
# print (name)
# print ("Hi" + name)
print("Welcome to our game! \n Guess the number.")

secret_number = 19
user_number = int(input("Guess the number"))
if secret_number > user_number:
    print("Secret number is bigger")
if secret_number < user_number:
    print("Secret number is smaller")
if secret_number == user_number:
    print("You won!")