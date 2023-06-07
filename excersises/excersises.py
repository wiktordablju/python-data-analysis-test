# ZADANIE 15.1
# SZESCIANY
# Liczba podniesiona do trzeciej potegi jest szczescianem.
# Wygeneruj wykres dla szescianow pierwszych piecu liczb, a nastepnie przygotuj wykres dla szescianow pierwszych 5000liczb

# ZADANIE 15.2
# KOLOROWE SZESCIANY
# Zastosuj mape kolorow na wykresach szescianow

import matplotlib.pyplot as plt

# pierwsze piec liczb
# numbers = [1, 2, 3, 4, 5]
# 5000 liczb
numbers = range(1, 5001)
cubes = [number**3 for number in numbers]


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(numbers, cubes, c=cubes, cmap=plt.cm.Blues)

ax.set_title('Szesciany 5000 liczb')
ax.set_xlabel("Liczba")
ax.set_ylabel("Szescian liczby")

ax.tick_params(axis='both', which='major', labelsize=12)

plt.ylim(min(cubes), max(cubes))

plt.show()
