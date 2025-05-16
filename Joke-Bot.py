PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def main():
    # 1. The chat asks the user "What do you want?"
    user_input = input(PROMPT)
    # 2. Chat replies with a single joke if "joke" is inserted. If anything else is typed down, the chat says SORRY:
    if (user_input == "Joke"):
        print(JOKE)
    else:
        print(SORRY)
    
if __name__ == "__main__":
    main()