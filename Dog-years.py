# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    human_age = input("Enter an age in calendar years: ")
    human_age_num = int(human_age)
    dog_age = human_age_num * DOG_YEARS_MULTIPLIER
    print(f"That\'s {dog_age} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()