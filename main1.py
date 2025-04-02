from decorators import logged

@logged
def example_function():
    print("Функция example_function работает")

@logged
def another_function():
    print("Функция another_function тоже работает")

if __name__ == "__main1__":
    example_function()
    another_function()