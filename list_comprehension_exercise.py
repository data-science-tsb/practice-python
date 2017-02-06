my_list = [1, 2, 3, 4, 222, 4]

my_magic_list = [x**x for x in range(100)]
print('list:', my_magic_list)

my_two_dimensional_list = [[x,y] for y in range(5,0,-1) for x in range(5)]
print('two-dimensional-array:', my_two_dimensional_list)

lis = [[x + str(y) for x in ('a', 'b', 'c', 'd', 'e')] for y in range(5)]
print(lis)
# a, b, c
# 1, 2, 3
# [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]]