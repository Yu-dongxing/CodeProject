import random

random_numbers = [random.randint(1, 5) for _ in range(5)]
max_numbers = [random.randint(10, 10) for _ in range(5)]

print(random_numbers+max_numbers)