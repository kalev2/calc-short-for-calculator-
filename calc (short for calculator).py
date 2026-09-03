choice = int (input("yoyoyo! wanna use my calc? (short for calculator). Pls choose a method  \n1. addition\n2. subtraction\n3. division\n4. multiplication    "))


if choice == 1:
    print("you chose addition.")
elif choice == 2 :
    print ("you chose subtraction.")
elif choice == 3 :
    print ("you chose division.")
else:   print ("you chose multiplication.")


number1 = float (input("choose a number "))
number2 = float (input("choose another number "))


if choice == 1:
    print(number1 + number2)
elif choice == 2:
    print (number1 - number2)
elif choice == 3:
    print (number1 / number2)
else:
 print (number1 * number2)
