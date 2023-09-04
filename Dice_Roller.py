import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Rolling App!")
    
    while True:
        num_dice = int(input("How many dice do you want to roll? (Enter 1 or 2): "))
        
        if num_dice not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
            continue
        
        dice_results = roll_dice(num_dice)
        
        print(f"Result{'s' if num_dice > 1 else ''}: {', '.join(map(str, dice_results))}")
        
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for using the Dice Rolling App!")
            break

main()