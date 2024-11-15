

def main():
    text = "This Sentence Has Mixed CASE Letters!"
    upper_counter = len([c for c in text if c.isupper()])
    lower_counter = len([c for c in text if c.islower()])
    print(f"The number of uppercase letters is: {upper_counter}")
    print(f"The number of lowercase letters is: {lower_counter}")


if __name__ == "__main__":
    main()