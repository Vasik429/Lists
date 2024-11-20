immutable_var = ('Turtle', 'Lion', 'Cat')
print(type(immutable_var))
# immutable_var.append ('Dog')
# print(immutable_var)
# immutable_var[1] = ('Tiger')
# tuple - неизменяемый список

mutable_list = [123, 'Turtle', True]
print(type(mutable_list))
mutable_list[0] = 345
mutable_list.append ('Dog')
print(mutable_list)