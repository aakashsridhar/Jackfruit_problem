import random

print("🎮 Welcome to the Ultimate Number Guessing Game!")
print("Choose a mode:")
print("1️⃣  You guess the number")
print("2️⃣  Computer guesses your number (Akinator style!)")

choice = input("Enter 1 or 2: ")

# ---------------------------------------------
# MODE 1: USER GUESSES COMPUTER'S NUMBER
# ---------------------------------------------
if choice == "1":
    print("\n🤖 I'm thinking of a number between 0 and 1000...")
    target = random.randint(0, 1000)
    attempts = 0
    
    while True:
        guess = int(input("👉 Enter your guess: "))
        attempts += 1
        
        if guess < target:
            print("⬆️ Too low! Try a higher number.")
        elif guess > target:
            print("⬇️ Too high! Try a lower number.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries!")
            break

# ---------------------------------------------
# MODE 2: COMPUTER GUESSES USER'S NUMBER
# ---------------------------------------------
elif choice == "2":
    print("\n🤔 Think of a number between **0 and 1000** in your mind...")
    input("Ready? Press ENTER to continue 😎")

    low = 0
    high = 1000
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1

        response = input(f"🤖 Is your number {mid}? (yes / higher / lower): ").lower()

        if response == "yes":
            print(f"🎯 Yay! I guessed your number {mid} in {attempts} tries! 🎉")
            break
        elif response == "higher":
            low = mid + 1
        elif response == "lower":
            high = mid - 1
        else:
            print("❌ Invalid input, please type: yes / higher / lower")

else:
    print("❌ Invalid choice. Please run again and choose 1 or 2.")
