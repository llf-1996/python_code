def customer():
    while True:
        n = yield
        print(f'customer: {n}')


def product(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print(f"product: {n}")
        r = c.send(n)
        print(f'customer return {r}')
    c.close()


if __name__ == '__main__':
    c = customer()
    product(c)
