def sum(num1, num2):
    return num1 + num2

print(sum(4,5))

total = sum(10,5)
print(sum(10,total))
print(sum(10,sum(10,5)))


def sum(num3, num4):
    def another_func(n3,n4):
        return n3 + n4
    return another_func(num3, num4)

total = sum(10, 20)
print(total)