import random

def main():
    dice_sides = input("How many sides does your dice have? ")
    x = int(dice_sides)
    roll = random.randint(1,x)
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()