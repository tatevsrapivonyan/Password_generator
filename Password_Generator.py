import random


def random_list():
    start = random.randint(33, 126)
    stop = random.randint(33, 126)

    while start > stop:
        start = random.randint(33, 126)
        stop = random.randint(33, 126)

    lst = [chr(random.randint(start, stop)) for i in range(random.randint(8, 15))]
    password = "".join(lst)
    return password


print(random_list())
