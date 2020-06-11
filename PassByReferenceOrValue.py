class Number:
    def __init__(self, number):
        self.number = number


def change(a, b, c):
    a += 1
    b.number += 1
    c = Number(c.number + 1)

a = 1
b = Number(1)
c = Number(1)

change(a, b, c)

print(f'{a}/{b.number}/{c.number}')