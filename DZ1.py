a = str(input('Введите строку:'))
def pal(a):
    if a[::1] == a[::-1]:
        return True
    return False

print(pal(a))