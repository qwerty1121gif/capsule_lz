from decorators import logged

@logged
def func1():
    print("123123")

if __name__ == "__main__":
    print("Скрипт работает")  # Проверка запуска файла
    func1()