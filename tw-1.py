def get_name():
    name = input('Write you name: ')
    return name


def greet(name):
    print(f'Hello {name}')


def main():
    name = get_name()
    greet(name)


main()
