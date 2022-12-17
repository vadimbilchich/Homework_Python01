# Задача 2:
# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно выяснить, является ли предикатом (утверждением) выражение:
# "Не(x или y или z) = не x и не y и не z"
    
for x in[False, True]:
    for y in[False, True]:
        for z in[False, True]:
            if(not x or y or z) != (not x or y or z):
                print('Выражение:¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) - False')
                break
else:
    print('Выражение:¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) - True')