def greet(name):
    return f"Hello, {name}!"

def inc(x):
    return x + 1


def main():
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()