def greet(name):
    return f"Hello, {name}! Welcome to Aur-Sunao."


def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
