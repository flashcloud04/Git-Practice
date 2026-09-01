def greet(name):
    return f"Hello, {name}! Welcome to Aur-Sunao App."


def main():
    name = input("Enter your name please here: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
