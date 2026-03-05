from datetime import datetime


def my_decorator(func):
    def private_decorator():
        print("-------")
        func()
        print("-------")
    return private_decorator

@my_decorator
def hello_message():
    now = datetime.now()
    print("Хочу в Африку")

hello_message()