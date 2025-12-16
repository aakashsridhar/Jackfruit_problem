"""
Hand Cricket (1-6) — Fair Play, Live Score, Run Rate, Target Display

Features in this updated version:
- User ALWAYS inputs first each ball (fair play).
- Detailed score updates after each ball (runs, balls, overs format like 4.2 overs).
- Live run rate displayed for the batting side after every ball (runs per over, 2 decimal places).
- During the second innings the game shows "Runs needed" for the chasing batsman and the current required run rate (if desired).
- Toss to decide who bats first. If user wins toss they choose bat/bowl; otherwise computer chooses.
- Two innings match: first innings sets a target, second innings chases and can finish early when target is passed.

How to use:

- Enter numbers 1-6 when prompted."""



import random
import sys

# ---------- Helpers ----------

def prompt_choice(prompt, options):
    options_map = {opt.lower(): opt for opt in options}
    while True:
        ans = input(prompt).strip().lower()
        if ans in options_map:
            return options_map[ans]
        # allow single-letter shortcuts
        if ans and ans[0] in options_map:
            return options_map[ans[0]]
        print(f"Please enter one of: {', '.join(options)}")


def get_user_number(role_desc="Enter a number"):
    while True:
        try:
            n = int(input(f"{role_desc} (1-6): ").strip())
            if 1 <= n <= 6:
                return n
            print("Number must be between 1 and 6.")
        except ValueError:
            print("Please enter an integer between 1 and 6.")


def format_overs(balls):
    # return a string like '4.2' for 26 balls (4 overs and 2 balls)
    overs = balls // 6
    rem = balls % 6
    return f"{overs}.{rem}"


def run_rate(runs, balls):
    # runs per over. If no balls yet, return 0.0
    if balls == 0:
        return 0.0
    return (runs * 6) / balls

# ---------- Innings ----------

def user_batting(target_runs=None):
    """User bats first or second. User inputs first; computer bowls after.
    Returns (runs, balls)
    If target_runs provided, it's the runs required to win (target = first_innings+1 normally).
    """
    print("\n--- You are BATTING ---")
    runs = 0
    balls = 0

    while True:
        balls += 1
        print(f"\nBall {balls} ({format_overs(balls)} overs):")
        # user inputs first
        bat = get_user_number("Your shot")
        # computer bowls after seeing user's input (fairness: random, but generated AFTER user enters)
        bowl = random.randint(1, 6)
        print(f"Computer bowls: {bowl}")

        if bat == bowl:
            print("\n❌ OUT! The bowler matched your shot.")
            print(f"You scored {runs} runs from {format_overs(balls)} overs.")
            rr = run_rate(runs, balls)
            print(f"Your run rate: {rr:.2f} runs per over.")
            return runs, balls
        else:
            runs += bat
            print(f"You scored {bat} this ball. Total = {runs} / {format_overs(balls)}")
            rr = run_rate(runs, balls)
            print(f"Current run rate: {rr:.2f} runs per over")

            if target_runs is not None:
                # target_runs is the runs required to WIN (e.g., first_innings + 1)
                runs_needed = target_runs - runs
                if runs_needed <= 0:
                    print(f"\n🔥 You have reached the target! You chased {target_runs} and win!")
                    return runs, balls
                else:
                    print(f"Runs needed to win: {runs_needed}")
                    # required run rate = runs_needed / (balls_remaining_in_overs) -> but no ball limit here
                    # we still show a simple required rate per over assuming infinite balls is meaningless
                    # so we only show runs needed and run rate so far.
        # continue


def computer_batting(target_runs=None):
    """Computer bats while user bowls. User always inputs first (as the bowler).
    Returns (runs, balls)
    """
    print("\n--- Computer is BATTING ---")
    runs = 0
    balls = 0

    while True:
        balls += 1
        print(f"\nBall {balls} ({format_overs(balls)} overs):")
        # user bowls (inputs first)
        bowl = get_user_number("Your bowling delivery")
        # computer chooses batting shot after seeing user's input
        bat = random.randint(1, 6)
        print(f"Computer plays: {bat}")

        if bat == bowl:
            print("\n🎉 OUT! You matched the computer's shot.")
            print(f"Computer scored {runs} runs from {format_overs(balls)} overs.")
            rr = run_rate(runs, balls)
            print(f"Computer run rate: {rr:.2f} runs per over.")
            return runs, balls
        else:
            runs += bat
            print(f"Computer scored {bat}. Total = {runs} / {format_overs(balls)}")
            rr = run_rate(runs, balls)
            print(f"Computer run rate: {rr:.2f} runs per over")

            if target_runs is not None:
                runs_needed = target_runs - runs
                if runs_needed <= 0:
                    print(f"\n💥 Computer has chased the target ({target_runs}) and wins!")
                    return runs, balls
                else:
                    print(f"Computer needs {runs_needed} more runs to win.")

# ---------- Toss and Match ----------

def coin_toss():
    print("\n--- Toss Time ---")
    call = prompt_choice("Call the toss — Heads or Tails? ", ["heads", "tails"]) 
    flip = random.choice(["heads", "tails"]) 
    print(f"Toss result: {flip.upper()}")
    if call == flip:
        print("You won the toss!")
        choice = prompt_choice("Choose to Bat or Bowl first: ", ["bat", "bowl"])
        user_bats_first = (choice == "bat")
    else:
        print("Computer won the toss.")
        comp_choice = random.choice(["bat", "bowl"]) 
        print(f"Computer chooses to {comp_choice} first.")
        user_bats_first = (comp_choice == "bowl")  # if comp bats, user bowls first
    return user_bats_first


def play_match():
    print("\nWelcome to Hand Cricket — Live Score & Run Rate Enabled!")
    print("Rules: batsman and bowler each pick 1-6. If numbers match, batsman is OUT. Otherwise batsman's number is added to score.")

    user_bats_first = coin_toss()

    if user_bats_first:
        # USER bats first
        first_runs, first_balls = user_batting()
        target_runs = first_runs + 1
        print(f"\nEnd of 1st innings. You scored {first_runs} in {format_overs(first_balls)} overs.")
        print(f"Target for Computer: {target_runs} runs to win.")

        # Computer chases; show runs needed after each ball inside function
        comp_runs, comp_balls = computer_batting(target_runs=target_runs)

        # result
        print("\n--- Match Result ---")
        if comp_runs >= target_runs:
            print(f"Computer wins by {comp_runs - target_runs + 1} runs (chased {target_runs}).")
        else:
            print(f"You win! Computer scored {comp_runs}, target was {target_runs}.")

    else:
        # Computer bats first
        comp_first_runs, comp_first_balls = computer_batting()
        target_runs = comp_first_runs + 1
        print(f"\nEnd of 1st innings. Computer scored {comp_first_runs} in {format_overs(comp_first_balls)} overs.")
        print(f"Target for You: {target_runs} runs to win.")

        user_runs, user_balls = user_batting(target_runs=target_runs)

        print("\n--- Match Result ---")
        if user_runs >= target_runs:
            print(f"You win! You chased {target_runs} with {user_runs}.")
        else:
            print(f"Computer wins! You scored {user_runs}, target was {target_runs}.")

# ---------- Main loop ----------

def main():
    while True:
        play_match()
        again = prompt_choice("\nPlay another match? (yes/no): ", ["yes", "no"]) 
        if again == "no":
            print("Thanks for playing — goodbye!")
            break

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Bye!")
        sys.exit(0)

