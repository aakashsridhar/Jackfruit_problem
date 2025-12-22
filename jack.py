



   


def main():
    while True:
        print("\n🎮 GAME LAUNCHER")
        print("1. Number Guessing Game")
        print("2. Tic Tac Toe")
        print("3. Odd or Even (Hand Cricket)")
        print("4. Rock–Paper–Scissors")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("\nLaunching Number Guessing Game...\n")
            import number_guessing_game
            number_guessing_game.main()
            

        elif choice == "2":
            print("\nLaunching Tic Tac Toe...\n")
            import tictactoe_final
            tictactoe_final.main()

        elif choice == "3":
            print("\nLaunching Odd or Even...\n")
            import odd_or_even_game
            odd_or_even_game.main()

        elif choice == "4":
            print("\nLaunching Rock–Paper–Scissors...\n")
            import rpc
        elif choice == "5":
            print("🚪 Exiting launcher. Play again soon!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
