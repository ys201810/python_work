# coding=utf-8


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b


def main():
    r = add_num(10, 20)
    print(r)


if __name__ == '__main__':
    main()
