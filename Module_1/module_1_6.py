# Словари и множества

a = 857
my_dict = {'Звёздочка': 859, 'Синий туман': 548, 'Ламборгини': a}
print(my_dict)
print(my_dict.get('Звёздочка'))
print(my_dict.get('Вулкан'))
my_dict.update({'Росинка': 229, 'Громовержец': 471})
print(my_dict.pop('Ламборгини'))
print(my_dict)

my_set = {a, 856, 'красный', 'синий', 'жёлтый', 'синий', 54, 12, 857, 54}
print(my_set)
my_set.add('зеленый')
my_set.add(99)
my_set.discard(857)
print(my_set)

a = [356, 678, 'Роза']