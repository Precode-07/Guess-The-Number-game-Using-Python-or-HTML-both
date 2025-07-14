import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def vending_display(current_guess=None):
    """ASCII vending-machine feel with spinning slots"""
    frames = [
        "[▒▒▒] 🎯 ",
        "[▓▒▒] 🎯 ",
        "[▒▓▒] 🎯 ",
        "[▒▒▓] 🎯 ",
    ]
    for _ in range(4):
        clear_console()
        frame = random.choice(frames)
        if current_guess is not None:
            frame = frame.replace("🎯", f"{current_guess:>3}")
        print(frame)
        time.sleep(0.1)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❗ Please enter a valid integer.")

def play_game():
    clear_console()
    print("🎮 Welcome to VendoGuess!")
    max_n = get_int("Enter max number (≥1): ")
    target = random.randint(1, max_n)
    guess = get_int(f"Guess a number between 1 and {max_n}: ")

    vending_display(guess)

    if guess == target:
        print(f"\n🎉 Bingo! You guessed **exactly** right: {target}.")
        print("🌟 You have sharp prediction skills—you're a guess wizard!")
    else:
        # show target with "reveal" animation
        for i in range(min(guess, target), target + (1 if target > guess else -1), 1 if target > guess else -1):
            vending_display(i)
        print(f"\n❌ You picked {guess}, but it was {target}.")
        diff = abs(target - guess)
        accuracy = (1 - diff / max_n) * 100
        if diff <= 1:
            print(f"👏 Wow, you're *almost there*! Off by just {diff}.")
        else:
            print(f"📏 Your accuracy: {accuracy:.1f}% ({diff} away). Nice try!")

if __name__ == "__main__":
    play_game()
