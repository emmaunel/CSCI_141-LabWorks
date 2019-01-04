def decideSomething(long_str, short_str):
    for long_i in range(len(long_str)):
        if (short_str[0] == long_str[long_i]) and (len(long_str) >= len(short_str) + long_i):
            yes_or_no = True
            for short_i in range(len(short_str)):
                if short_str[short_i] != long_str[long_i + short_i]:
                    yes_or_no = False
            if yes_or_no == True:
                return True
    return False


print(decideSomething('resume', 'sum'))


def Lop(a):
    return a in ('a', 'e', 'i', 'o', 'u')


def Bar(a, b, c):
    for i in range(len(a)):
        if Lop(a[i]):
            b.append(a[i])
        else:
            c.append(a[i])


def Zep(a, b, c):
    x = ''
    y = 0
    z = 0
    for h in a:
        if Lop(h):
            x += c[z]
            z = (z + 1) % len(c)
        else:
            x += b[y]
            y = (y + 1) % len(b)
    return x


def Foo(a):
    b = []
    c = []
    Bar(a, b, c)
    return Zep(a, b, c)


print(Foo('peanut butter'))


def SecondLargest(l):
    large = 0
    sec = 0
    low = 0
    for index in range(0, len(l)):
        x = l[index]
        if x > large:
            low = sec
            sec = large
            large = x
        elif large > x > sec:
            low = sec
            sec = x
        elif x < low:
            low = x
    return sec


print(SecondLargest([1, -2, 0]))
print(SecondLargest([3, 1, 2]))
print(SecondLargest([1, 2, 3]))
print(SecondLargest([1, 2, 3, 4]))
