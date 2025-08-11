# Задание 9. Класс «Музыкальный плейлист»
# Цель: много методов для управления коллекцией и сортировки.
# Описание:
# Создай класс Playlist.
# Требования:
# 1. Атрибуты: название плейлиста, список треков (название, исполнитель, длительность в
# секундах).
# 2. Методы:
# o add_track(name, artist, duration) — добавить трек.
# o remove_track(name) — удалить трек.
# o total_duration() — общая длительность всех треков.
# o find_by_artist(artist) — найти все треки исполнителя.
# o longest_track() — найти самый длинный трек.
# o shortest_track() — найти самый короткий трек.
# o shuffle() — перемешать треки в случайном порядке.
# o sort_by_duration(reverse=False) — сортировать треки по длительности.

import random

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, name, artist, duration):
        self.tracks.append({"name": name, "artist": artist, "duration": duration})

    def remove_track(self, name):
        self.tracks = [t for t in self.tracks if t["name"] != name]

    def total_duration(self):
        return sum(t["duration"] for t in self.tracks)

    def find_by_artist(self, artist):
        return [t for t in self.tracks if t["artist"].lower() == artist.lower()]

    def longest_track(self):
        return max(self.tracks, key=lambda t: t["duration"], default=None)

    def shortest_track(self):
        return min(self.tracks, key=lambda t: t["duration"], default=None)

    def shuffle(self):
        random.shuffle(self.tracks)

    def sort_by_duration(self, reverse=False):
        self.tracks.sort(key=lambda t: t["duration"], reverse=reverse)

playlist = Playlist("Мой плейлист")

playlist.add_track("Song1", "Artist1", 100)
playlist.add_track("Song2", "Artist2", 200)
playlist.add_track("Song3", "Artist1", 300)

print("Общая длительность:", playlist.total_duration())
print("Треки Artist1:", playlist.find_by_artist("Artist1"))
print("Самый длинный:", playlist.longest_track())
print("Самый короткий:", playlist.shortest_track())

playlist.shuffle()
print("После перемешивания:", playlist.tracks)

playlist.sort_by_duration(reverse=True)
print("Сортировка по убыванию:", playlist.tracks)
