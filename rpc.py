import random

choices = ["rock", "paper", "scissor"]

user_score = 0
comp_score = 0

print("=== Rock Paper Scissor (First to 3) ===")

while user_score < 3 and comp_score < 3:

    user = input("\nEnter rock / paper / scissor: ").lower()

    if user not in choices:
        print("Invalid input! Try again.")
        continue

    comp = random.choice(choices)
    print("Computer chose:", comp)

    # decide winner
    if user == comp:
        print("It's a draw!")
    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1

    print(f"Score → You: {user_score} | Computer: {comp_score}")

# final result
if user_score > comp_score:
    print("\n🎉 YOU WON THE MATCH!")
else:
    print("\n😢 COMPUTER WON THE MATCH!")
