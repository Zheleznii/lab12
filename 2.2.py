dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
values_set = set(dct.values())
union_set = keys_set.union(values_set) # можно через keys_set | values_set но я не знаю как тебе нужно так что сам выбери !!!!!!!!!

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:", union_set)