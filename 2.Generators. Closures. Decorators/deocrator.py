def my_decorator(func):
    def private_decorator():
        print("Ми декоруємо метод зелений сфітофор")
        func()
        print("Червоне світло газу :)")
    return private_decorator

@my_decorator
def hello_message():
    print("Хочу в Африку")

hello_message()