
class MyShittyClass:
    x = 1

    def __add__(self, other):
        temp = self.x + other.x
        new_shitty = MyShittyClass()
        new_shitty.x = temp
        return new_shitty

    def __str__(self):
        return 'num:' + str(self.x)


s1 = MyShittyClass()
s1.x = 2

s2 = MyShittyClass()
s2.x = 5

ans = s1 + s2

print('new:', ans)