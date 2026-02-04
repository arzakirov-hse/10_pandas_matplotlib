import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# 1. Загрузка данных
with open("events.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["events"])

# 2. Анализ данных
df['event_type'] = df['signature'].apply(lambda x: x.split()[0])
event_counts = df['event_type'].value_counts()
print("Распределение событий по типам:")
print(event_counts)

# 3. Визуализация
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x='event_type',
    hue='event_type',     # теперь palette использован корректно
    dodge=False,          # объединяем столбцы в одну группу
    palette='Set2',
    legend=False          # отключаем легенду, чтобы не дублировалась
)
plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Тип события")
plt.ylabel("Количество")
plt.show()
