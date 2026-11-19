def greet_decorator(func):
    def wrapper():
        print("Welcome!")
        func()

    return wrapper


@greet_decorator
def greet():
    print("Hello, how are you?")


greet()