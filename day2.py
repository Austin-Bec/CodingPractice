num = int(input("Please enter a number: "))

#Check if number is positive or negative.
if num > 0:
    pos_neg = "positive"
elif num < 0:
    pos_neg = "negative"
else:
    pos_neg = "zero"

#Check if the number is even or odd.
if num % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

#Display result
if num == 0:
    print("The number is zero and neither even nor odd.")
else:
    print(f"The number is {pos_neg} and {even_odd}.")