list1 = input("Введите первый список: ").split()
list2 = input("Введите второй список: ").split()

set1 = set(list1)
set2 = set(list2)

add_sets = set1 & set2  # можно также: set1.intersection(set2)

print("Общие элементы:", ' '.join(sorted(add_sets, key=int)))
