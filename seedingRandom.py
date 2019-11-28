import random

answer = input("Enter a seed or press enter to skip: ")

try:
    seed = int(answer)
    print("Using seed of ", seed)
except:
    seed = random.randint(0, 10000000000)
    print("Generated randoms seed of ", seed)

random.seed(seed)

random.seed(9328362664)
cool = True
uncool = False
print(random.randint(0,1000))
print(random.randint(0,1000))
print("this is a cooler function than yours")
print("i mean come on, I'm a pretty cool guy")
print("but i suppose you're pretty cool too")
print(random.randint(0,1000))
today = "11/27/2019"
turkey = "i'm sorry for tomorrow"
