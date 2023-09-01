data = [1, 2, 3]


def x():
    global data
    data = data + []


x()
print(data)
