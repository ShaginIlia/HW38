import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Работа с numpy

na = np.array([1, 2, 3, 4, 5, 6, 7])
nb = np.array([11, 12, 13, 14, 15, 16, 17])
nc = np.concatenate((na, nb))
print(nc)  # объединил 2 массива в один

na2 = na.sum()
nb2 = nb.sum()
print(na2, nb2)  # посчитал сумму в каждом массиве

print(na2 + nb2)
print(na.max(), nb.min())  # можно узнать максимальные и минимальные значения массива
print(na.mean(), nb.mean())  # можно узнать среднее арифметическое

data = np.array([[23, 34], [45, 56], [78, 89]])  # создал матрицу
print(data)
num_rand = np.random.default_rng()  # numpy может создать случайную матрицу
print(num_rand.random((5, 2)))

# Работа с pandas

df = pd.read_csv('IRIS.csv')  # читаю файл ирисы
print(df)
df.info()  # узнаю информацию о файле
print(df.describe())  # узнаю статистические сведения о файле
print(df.sepal_length.value_counts())  # подсчитал количество значений в конкретном столбце

# Работа с matplotlib

plt.pie(df["species"].value_counts(), labels=['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], autopct='%1.1f%%')
plt.show()  # попытался на основе данных по ирисам сделать круговой график, вроде что-то получилось

plt.plot([2, 4, 5, 6, 8])
plt.show()  # сам нарисовал случайную кривую

plt.plot([0, 15, 40, 50, 80, 90], [0, 22, 34, 54, 76, 93])
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title('Мой график')
plt.show()  # нарисовал свой график и дополнил максимальными осями + добавил название
