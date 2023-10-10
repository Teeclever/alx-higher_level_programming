#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

print()

my_u = MyInt(6)
my_v = MyInt(6)
print(f"Comparing {my_u} and {my_v}")
print(my_u == my_v)
print(my_u != my_v)
