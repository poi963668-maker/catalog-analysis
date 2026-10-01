import math
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака."""
    if not movies:
        return 0.0
        
    total_rating = 0.0
    for movie in movies:
        total_rating += movie["rating"]
        
    return round(total_rating / len(movies), 1)


# Проверяем работу первой функции (выводим результат на экран)
print("Средний рейтинг фильмов:", average_rating(movies))


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж: (самый старый фильм, самый новый фильм, средний возраст)."""
    if not movies:
        return 0, 0, 0
        
    ages = []
    for movie in movies:
        # Считаем возраст фильма
        age = current_year - movie["year"]
        ages.append(age)
        
    # Находим самый старый и самый новый фильм в годах
    oldest = max(ages)
    newest = min(ages)
    
    # Считаем средний возраст и округляем ВВЕРХ до целого числа
    average_age = math.ceil(sum(ages) / len(movies))
    
    return oldest, newest, average_age


# Проверяем работу второй функции (выводим результат на экран)
print("Статистика возраста фильмов:", catalog_age_stats(movies))


def duration_in_hours(minutes):
    """Переводит минуты в формат строки 'Xч Yм'."""
    # Находим количество полных часов
    hours = minutes // 60
    # Находим оставшиеся минуты
    remaining_minutes = minutes % 60
    
    # Формируем красивую строку
    return f"{hours}ч {remaining_minutes}м"


# Проверяем работу третьей функции (передаём для примера 135 минут)
print("Пример перевода времени (135 минут):", duration_in_hours(135))


def rating_tier(rating):
    """Возвращает категорию фильма по его оценке."""
    # Используем тернарный оператор для первой категории
    if rating >= 9:
        return "шедевр"
    
    # Для остальных категорий используем стандартные if/elif/else
    if rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    """Возвращает метку времени для фильма через конструкцию match/case."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Проверяем работу функций Этапа 2 (выводим тестовые примеры на экран)
print("Категория оценки (рейтинг 8.6):", rating_tier(8.6))
print("Метка времени (год 2014):", decade_label(2014))
print("Метка времени (год 2023):", decade_label(2023))


# ==========================================
# ЭТАП 3. ЦИКЛЫ
# ==========================================

print("\n--- Фильмы, которые НЕ относятся к жанру comedy ---")
# 1. Используем for и continue для фильтрации жанров
for movie in movies:
    if "comedy" in movie.get("genres", []):
        continue
    print(f"- {movie['title']}")

print("\n--- Поиск первого фильма с рейтингом выше 9.0 ---")
# 2. Используем while, break и ветку else цикла
index = 0
while index < len(movies):
    movie = movies[index]
    if movie["rating"] > 9.0:
        print(f"Найден шедевр: {movie['title']} (Рейтинг: {movie['rating']})")
        break
    index += 1
else:
    print("Шедевров не найдено")

# 3. Напишем функцию подсчета длинных фильмов
def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

print("\n--- Количество длинных фильмов ---")
# Проверяем работу функции (ищем фильмы длиннее 120 минут)
print(f"Фильмов длиннее 120 минут: {count_long_movies(movies, 120)}")


# ==========================================
# ЭТАП 4. СТРОКИ
# ==========================================

def normalize_title(title):
    """Приводит каждое слово в строке к заглавной букве вручную."""
    words = title.split()
    normalized_words = []
    for word in words:
        if word:  # Проверяем, что слово не пустое
            # Делаем первую букву заглавной, а остальные оставляем как есть
            new_word = word[0].upper() + word[1:]
            normalized_words.append(new_word)
    return " ".join(normalized_words)


def make_slug(title):
    """Превращает название в слаг для ссылки (в нижнем регистре и через дефисы)."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Возвращает единую красивую строку с описанием фильма."""
    # Получаем нормализованное название фильма
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    
    # Переводим длительность, вызывая нашу функцию из Этапа 1
    duration = duration_in_hours(movie["duration_min"])
    
    # Сортируем жанры по алфавиту и склеиваем через запятую
    genres_list = sorted(movie.get("genres", []))
    genres_str = ", ".join(genres_list)
    
    # Собираем всё в итоговую f-строку по шаблону Практикума
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres_str}'


print("\n--- Проверка Этапа 4 (Строки) ---")
# Проверяем первые две функции на примере строки "silent hours"
test_title = "silent hours"
norm_title = normalize_title(test_title)
print("Нормализованное название:", norm_title)
print("Слаг для ссылки:", make_slug(test_title))

# Проверяем строку отчёта на примере фильма из списка под индексом 7
# (В прекоде это "The Quiet Algorithm" или аналогичный фильм)
if len(movies) > 7:
    print("Строка отчета для фильма:")
    print(format_report_line(movies[7]))


# ==========================================
# ЭТАП 5. СПИСКИ
# ==========================================

def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    # Сортируем копию списка фильмов по ключу "rating" в обратном порядке (reverse=True)
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    
    # Собираем только названия фильмов
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) топ-фильмов по рейтингу."""
    # Сортируем фильмы по убыванию рейтинга
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    
    # Берём первые n фильмов с помощью среза [:n]
    top_movies = sorted_movies[:n]
    
    # Формируем список кортежей (название, рейтинг)
    result = []
    for movie in top_movies:
        result.append((movie["title"], movie["rating"]))
    return result


print("\n--- Проверка Этапа 5 (Списки) ---")
# Проверяем сортировку названий (выведем первые 3 названия для аккуратности)
all_sorted_titles = titles_sorted_by_rating(movies)
print("Топ-3 названий по рейтингу:", all_sorted_titles[:3])

# Проверяем функцию Топ-N фильмов по рейтингу (ищем 3 лучших фильма)
print("Топ-3 фильма (структура кортежей):")
print(top_n_by_rating(movies, 3))


# ==========================================
# ЭТАП 6. СЛОВАРИ
# ==========================================

def count_by_genre(movies):
    """Считает количество фильмов в каждом жанре вручную через метод .get()."""
    genre_counts = {}
    for movie in movies:
        for genre in movie.get("genres", []):
            # Если жанра еще нет в словаре, .get вернет 0, и мы прибавим 1
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    """Строит словарь, где ключ — актер, а значение — список его фильмов."""
    filmography = {}
    for movie in movies:
        title = movie["title"]
        for actor in movie.get("actors", []):
            # Если актера еще нет в словаре, создаем для него пустой список
            if actor not in filmography:
                filmography[actor] = []
            # Добавляем название фильма в список актера
            filmography[actor].append(title)
    return filmography


print("\n--- Проверка Этапа 6 (Словари) ---")
# 1. Проверяем подсчет по жанрам
print("Подсчет фильмов по жанрам:")
print(count_by_genre(movies))

# 2. Построение словаря лучших фильмов через генератор словарей (Dict Comprehension)
avg_rating_value = average_rating(movies)  # Берем средний рейтинг из Этапа 1
best_movies_dict = {
    movie["title"]: movie["rating"] 
    for movie in movies 
    if movie["rating"] > avg_rating_value
}
print(f"\nФильмы с рейтингом выше среднего ({avg_rating_value}):")
print(best_movies_dict)


# ==========================================
# ЭТАП 6. СЛОВАРИ
# ==========================================

def count_by_genre(movies):
    """Считает количество фильмов в каждом жанре вручную через метод .get()."""
    genre_counts = {}
    for movie in movies:
        for genre in movie.get("genres", []):
            # Если жанра еще нет в словаре, .get вернет 0, и мы прибавим 1
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    """Строит словарь, где ключ — актер, а значение — список его фильмов."""
    filmography = {}
    for movie in movies:
        title = movie["title"]
        for actor in movie.get("actors", []):
            # Если актера еще нет в словаре, создаем для него пустой список
            if actor not in filmography:
                filmography[actor] = []
            # Добавляем название фильма в список актера
            filmography[actor].append(title)
    return filmography


print("\n--- Проверка Этапа 6 (Словари) ---")
# 1. Проверяем подсчет по жанрам
print("Подсчет фильмов по жанрам:")
print(count_by_genre(movies))

# 2. Построение словаря лучших фильмов через генератор словарей (Dict Comprehension)
avg_rating_value = average_rating(movies)  # Берем средний рейтинг из Этапа 1
best_movies_dict = {
    movie["title"]: movie["rating"] 
    for movie in movies 
    if movie["rating"] > avg_rating_value
}
print(f"\nФильмы с рейтингом выше среднего ({avg_rating_value}):")
print(best_movies_dict)


# ==========================================
# ЭТАП 7. МНОЖЕСТВА
# ==========================================

def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    genres_set = set()
    for movie in movies:
        # Объединяем текущие жанры с общим множеством через оператор |
        genres_set = genres_set | set(movie.get("genres", []))
    return genres_set


def common_actors(movie1, movie2):
    """Возвращает множество актеров, снявшихся в обоих фильмах."""
    actors1 = set(movie1.get("actors", []))
    actors2 = set(movie2.get("actors", []))
    # Находим пересечение с помощью оператора &
    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, которые есть в списке movies_a, но нет в movies_b."""
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie.get("genres", []))
        
    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie.get("genres", []))
        
    # Находим разность множеств с помощью оператора -
    return genres_a - genres_b


print("\n--- Проверка Этапа 7 (Множества) ---")
# 1. Проверяем общих актеров для фильма 0 и фильма 3
if len(movies) > 3:
    print("Общие актеры для фильма 0 и 3:", common_actors(movies[0], movies[3]))

# 2. Проверяем разность жанров по примеру из Практикума
if len(movies) > 6:
    print("Уникальные жанры для срезов фильмов:", genres_only_in_one(movies[5:6], movies[:5]))


# ==========================================
# ЭТАП 8. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ
# ==========================================

def iter_high_rated(movies, min_rating=8.0):
    """Функция-генератор, которая лениво отдает фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


print("\n--- Проверка Этапа 8 (Вывод лучших фильмов через yield) ---")
# Демонстрируем работу генератора циклом for с вызовом format_report_line
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

print("\n--- Суммарная длительность фильмов с рейтингом выше 7 ---")
# Подсчет общей длительности через генераторное выражение внутри sum()
total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
print(f"Общая длительность: {total_duration} минут")


# ==========================================
# ЭТАП 9. ИТОГОВЫЙ ОТЧЕТ
# ==========================================

def build_report(movies):
    """Объединяет результаты всех этапов в единый консольный отчет."""
    print("ОТЧЕТ ПО КАТАЛОГУ")
    
    # 1. Общая статистика (Этап 1)
    avg_rating = average_rating(movies)
    # Нам нужен только третий элемент кортежа — средний возраст
    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()
    
    # 2. Топ-3 фильма (Этап 5 и Этап 4)
    print("Топ-3 фильма:")
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    for movie in sorted_movies[:3]:
        print(f"  {format_report_line(movie)}")
    print()
    
    # 3. Фильмов по жанрам (Этап 6)
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    # Сортируем жанры по убыванию количества фильмов, а при равенстве — по алфавиту
    sorted_genres = sorted(genre_counts.items(), key=lambda x: (-x[1], x[0]))
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()
    
    # 4. Все уникальные жанры каталога по алфавиту (Этап 7)
    genres_set = all_genres(movies)
    sorted_unique_genres = sorted(list(genres_set))
    genres_line = ", ".join(sorted_unique_genres)
    print(f"Все жанры каталога: {genres_line}")


# ==========================================
# ГЛАВНЫЙ ЗАПУСК ПРОГРАММЫ
# ==========================================
if __name__ == "__main__":
    build_report(movies)
