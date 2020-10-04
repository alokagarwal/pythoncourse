# try:
#     number  = int(input("enter a number "))
#     number += 1 
#     print(number)
# except TypeError:
#     print("enter a number not string")
# except ValueError:
#     print("please enter a number only")
# finally:
#     print("try except is finished")

x = -1
if x < 0:
    raise Exception("sorry, no numbers below zero")
