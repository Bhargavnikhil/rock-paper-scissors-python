import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("=" * 40)
print("      🎮 Rock Paper Scissors 🎮")
print("=" * 40)

try:
    user_choice = int(input(
        "\nChoose an option:\n"
        "1. ROCK 🪨\n"
        "2. PAPER 📄\n"
        "3. SCISSORS ✂️\n\n"
        "Enter your choice (1-3): "
    ))
except ValueError:
    sys.exit("❌ Invalid input! Please enter a number.")

if user_choice not in [1, 2, 3]:
    sys.exit("❌ Invalid choice! Please select a number between 1 and 3.")

computer_choice = random.randint(1, 3)

print("\n------------------------------")
print(f"You chose      : {RPS(user_choice).name}")
print(f"Computer chose : {RPS(computer_choice).name}")
print("------------------------------")

if user_choice == computer_choice:
    print("\n🤝 It's a Tie!")
elif (
    (user_choice == RPS.ROCK.value and computer_choice == RPS.SCISSORS.value)
    or (user_choice == RPS.PAPER.value and computer_choice == RPS.ROCK.value)
    or (user_choice == RPS.SCISSORS.value and computer_choice == RPS.PAPER.value)
):
    print("\n🎉 Congratulations! You Win!")
else:
    print("\n💻 Computer Wins!")

print("\nThanks for playing! ❤️")