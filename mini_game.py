import random

secret = random.randint(1,100)
attempts = 0

print("🎯 Guess the number between 1 and 100!")

while True:
    
    gusse = int(input("Enter your guess: "))
    attempts += 1

    if gusse < secret:
        print("Too low")
    elif gusse > secret:
        print("Too high")
    else:
        print(f"Correct! 🎉 You guessed it in {attempts} tries.")
        break
