# numbers:list[int]=[95,96,97,98,99,100,101,102,103,104,105]
import random
from random import randint

numbers: list[int] = [num for num in range(95, 106)]
print(numbers)
numbers_even: list[int] = [num for num in range(10, 21, +2)]
print(numbers_even)
true_false: list[int] = [random.choice([True, False]) for i in range(5)]
print(true_false)
random_numbers: list[int] = [random.randint(1, 100) for num in range(10)]
print(random_numbers)
random_numbers_big: list[int] = [num for num in random_numbers if num > 50]
print(random_numbers_big)
random_numbers_2: list[int] = [random.randint(1, 99) for num in range(10)]
print(random_numbers_2)
random_numbers_ahadot: list[int] = [num % 10 for num in random_numbers_2]
print(random_numbers_ahadot)
