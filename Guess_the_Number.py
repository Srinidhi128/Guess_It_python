import random
import math
lower=int(input("Enter lower bound:"))
upper=int(input("Enter upper bound"))
x=random.randint(lower,upper)
print("You have",round(math.log(upper-lower+1,2)),"chances to guess the number")
count=0
while (count<math.log(upper-lower+1,2)):
    count+=1
    guess=int(input("Guess the Number:"))
    if x==guess:
        print("Congratulations you guessed it right")
        break
    elif x > guess:
        print("You guessed it low")
    elif x < guess:
        print("You guessed it high")
if count>math.log(upper-lower+1,2):
    print("You Lost!Better luck next time")
    print("The Number is",x)
    
