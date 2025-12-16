import random

def main():
    print("🎮 Welcome to the Ultimate Number Guessing Game!")
    print("Choose a mode:")
    print("1️⃣  You guess the number")
    print("2️⃣  Computer guesses your number (Akinator style!)")

    choice = input("Enter 1 or 2: ").strip()

    # ---------------------------------------------
    # MODE 1: USER GUESSES COMPUTER'S NUMBER
    # ---------------------------------------------
    if choice == "1":
        print("\n🤖 I'm thinking of a number between 0 and 1000...")
        target = random.randint(0, 1000)
        attempts = 0

        while True:
            try:
                guess = int(input("👉 Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

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
        print("\n🤔 Think of a number between 0 and 1000 in your mind...")

        confirm = input(
            "Is your number within the range 0–1000? (yes/no): "
        ).strip().lower()

        # 🔐 Guard condition for >1000
        if confirm != "yes":
            print("❌ I can only guess numbers up to 1000.")
            print("Please restart the game and choose a valid number.")
            return   # exits main(), returns to launcher

        input("Ready? Press ENTER to continue 😎")

        low = 0
        high = 1000
        attempts = 0

        while low <= high:
            mid = (low + high) // 2
            attempts += 1

            response = input(
                f"🤖 Is your number {mid}? (yes / higher / lower): "
            ).strip().lower()

            if response == "yes":
                print(f"🎯 Yay! I guessed your number {mid} in {attempts} tries! 🎉")
                break
            elif response == "higher":
                low = mid + 1
            elif response == "lower":
                high = mid - 1
            else:
                print("❌ Invalid input, please type: yes / higher / lower")

        # Extra safety check (logical contradiction)
        if low > high:
            print("🤨 Something doesn't add up.")
            print("Are you sure your number was between 0 and 1000?")

    else:
        print("❌ Invalid choice. Please choose 1 or 2.")

# ------------------------------------------------
# ENTRY POINT
# ------------------------------------------------
if __name__ == "__main__":
    main()
