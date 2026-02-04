# Пример выполнения задания по теме 3:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Загрузка данных
with open("events.json", "r") as file:
    data = json.load(file)

# Преобразование в DataFrame
df = pd.DataFrame(data["events"])

# Визуализация
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="signature")
plt.title("Распределение типов событий безопасности")
plt.xticks(rotation=90)  # Поворот подписей оси X для лучшей читаемости
plt.show()
