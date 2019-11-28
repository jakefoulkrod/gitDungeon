import random

answer = input("Enter a seed or press enter to skip: ")

try:
    seed = int(answer)
    print("Using seed of ", seed)
except:
    seed = random.randint(0, 10000000000)
    print("Generated randoms seed of ", seed)

random.seed(seed)

print(random.randint(0, 1000))
print(random.randint(0, 1000))
print(random.randint(0, 1000))
print(random.randint(0, 1000))
print(random.randint(0, 1000))
print(random.randint(0, 1000))
print(random.randint(0, 1000))
