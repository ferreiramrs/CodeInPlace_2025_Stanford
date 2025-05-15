from ai import call_gpt

def main():
    username = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print ("Creating your haiku")
    haiku = call_gpt (f"Please turn the {username} and the {topic} into a haiku")
    print(haiku)


if __name__ == "__main__":
    main()