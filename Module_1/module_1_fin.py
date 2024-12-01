#Дополнительное практическое задание по модулю: "Базовые структуры данных."

dict_ = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#print(sorted(list(students)))
sorted_ = sorted(list(students))
#print(sum(grades[0]) / len(grades[0]))
dict_.update({sorted_[0]: sum(grades[0]) / len(grades[0])})
dict_.update({sorted_[1]: sum(grades[1]) / len(grades[1])})
dict_.update({sorted_[2]: sum(grades[2]) / len(grades[2])})
dict_.update({sorted_[3]: sum(grades[3]) / len(grades[3])})
dict_.update({sorted_[4]: sum(grades[4]) / len(grades[4])})

print(dict_)
