import random

secret = random.randint(1, 10)
success = False

for _ in range(3):
    guess = int(input())
    if guess == secret:
        print("Ви вгадали!")
        success = True
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")

if not success:
    print("Ви програли")