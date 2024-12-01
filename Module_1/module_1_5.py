# Неизменяемые и изменяемые объекты. Кортежи

immutable_var = ('gloves', 2, 'pants', 1, 'shirt', 'jeans')
print(immutable_var)
print(immutable_var[0].upper())
#print(immutable_var.append(84))
#print(immutable_var[0] = 'jacket')
# Объект кортеж неизменяемый и не поддерживает методы по изменению своего состава

mutable_list = ['table', 'sofa', 'bed', 640, False]
print(mutable_list)
print(mutable_list[0].upper())
mutable_list[2] = 125
mutable_list.append('chair')
mutable_list[3:5] = immutable_var
print(mutable_list)

#mutable_list[1:3] = 125

