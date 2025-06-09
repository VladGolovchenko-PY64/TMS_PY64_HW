import json
import csv


with open('city.list.json', encoding='utf-8') as file:
    data = json.load(file)

# 1. Определить количество городов в файле

total_cities = len(data)
print(f"Всего городов: {total_cities}")

# 2. Создать словарь, где ключ — это код страны, а значение — количество
# городов.

country_count = {}
for city in data:
    country = city["country"]
    country_count[country] = country_count.get(country, 0) + 1

print("Словарь: код страны - количество городов:")
for country, count in country_count.items():
    print(f"{country}: {count}")

# 3. Подсчитать количество городов в северном полушарии и в южном

north = sum(1 for city in data if city["coord"]["lat"] > 0)
south = total_cities - north
print(f"В северном полушарии: {north}")
print(f"В южном полушарии: {south}")

# 4. Перевести в CSV файл данные по городам (координаты представить в виде
# строки значений через запятую).

with open('cities.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'country', 'coord'])
    for city in data:
        coord = f'{city["coord"]["lat"]},{city["coord"]["lon"]}'
        writer.writerow([city["id"], city["name"], city["country"], coord])


# 5. Создать другой JSON файл, в который сохранить только города одной
# выбранной страны.

target_country = 'RU'
filter = [city for city in data if city["country"] == target_country]

with open(f'{target_country}_cities.json', 'w', encoding='utf-8') as file:
    json.dump(filter, file, ensure_ascii=False, indent=2)


