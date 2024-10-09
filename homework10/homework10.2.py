# try-except is a way to catch and handle errors without letting the program crash
# As said earlier you should "catch" the errors because otherwise your code will simply crash
# and if you do catch them instead of letting it happen you will not have to restart the code from the beginning.
from operator import index

try:
    number: int = 88 // 0
    print(number)

except:
    print("number cannot be divided by zero")
while True:
    try:
        number: int = int(input("enter number from 1 to 100:"))
        if not 0 <= number <= 100:
            raise ValueError(f"{number} not in range")
        break
    except:
        print("out of range")
print(f"the number is {number}")

numbers: list[int] = []
stop: int = -999
while True:
    try:
        number: int = int(input(f"enter your number"))
        if number == stop:
            break
        if not 0 <= number <= 10 or number == int:
            raise ValueError(f"{number} not in range")
        numbers.append(number)
        numbers.count(number)
        for i in range(10):
            counts: int = numbers.count(i)
            if counts >= 1:
                print(f"{[i]}:{counts} ", end="")
        print()
    except:
        print(f"the number {number} is out of range or doesnt have a value!")
