my_dict = {'Cucumbers': 20, 'Mandarins': 30, 'Tomatoes': 70}
print(my_dict)
print(my_dict['Cucumbers'])
my_dict ['apples'] = 2
print(my_dict['apples'])
print(my_dict)
my_dict.update ({'mushrooms': 7,
               'Turtle': 1})
print(my_dict)
print(my_dict.get('Mandarins'))
my_dict.pop ('Mandarins')
print(my_dict)
print(my_dict.get('Mandarins'))
print(my_dict)

my_set = {1,2,3,7,2,3,7,1,'Turtle', 0.5}
print(my_set)
my_set.update({18, (0.5, 0.7, 0,12)})
print(type(my_set))
# my_set.remove('egg') - none
my_set.discard('Turtle')
print(my_set)



