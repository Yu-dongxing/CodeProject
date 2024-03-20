import random

random_numbers = [random.randint(1, 5) for _ in range(6)]
max_numbers = [random.randint(10, 10) for _ in range(4)]
max01_numbers = [random.randint(5, 8) for _ in range(1)]
max02_numbers = [random.randint(10, 10) for _ in range(2)]
re=random_numbers+max_numbers+max01_numbers+max02_numbers
print(re)
for number in re:  
    print(number)