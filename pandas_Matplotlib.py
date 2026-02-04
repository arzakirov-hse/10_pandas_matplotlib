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

# 2. Анализ данных
# Чтобы посмотреть распределение по типам, можно выделить первую часть поля "signature"
df['event_type'] = df['signature'].apply(lambda x: x.split()[0])  # Берем первую часть (MALWARE-CNC, EXPLOIT, NETBIOS, INDICATOR-COMPROMISE)

# Посчитаем количество событий каждого типа
event_counts = df['event_type'].value_counts()
print("Распределение событий по типам:")
print(event_counts)

# 3. Визуализация
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='event_type', order=event_counts.index, palette='Set2')
plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Тип события")
plt.ylabel("Количество")
plt.show()