import math

print("Think of a number.")

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

max_guesses = math.ceil(math.log(high - low + 1, 2))
print("I can find your number in at most", max_guesses, "guesses.")

guesses = 0

while low <= high:
    guess = (low + high) // 2
    guesses += 1

    print("\nMy guess is:", guess)
    hint = input("Enter H if too high, L if too low, or C if correct: ").upper()

    if hint == "C":
        print("I guessed your number in", guesses, "guesses!")
        break

    elif hint == "H":
        high = guess - 1

    elif hint == "L":
        low = guess + 1

    else:
        print("Invalid response. Please enter H, L, or C.")
        guesses -= 1
        continue

    if low > high:
        print("Your hints are inconsistent. You must have made a mistake.")
        break
