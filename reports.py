
# Report function

GAME_NAME = 0
MILLIONS_SOLD = 1
YEAR = 2
GENRE = 3


def count_games(file_name):
    file = open(file_name, "r")
    count = len(file.readlines())
    file.close()
    return count


def decide(file_name, year):
    year_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        x = line.rsplit('\t')
        year_list.append(x[YEAR])
    file.close()
    if str(year) in year_list:
        return True
    else:
        return False


def get_latest(file_name):
    year_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        year_list.append((split_list[GAME_NAME], split_list[YEAR]))
    latest = max(year_list, key=lambda t: t[1])
    file.close()
    return latest


def count_by_genre(file_name, genre):
    count_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        count_list.append(split_list[GENRE])
    genre_number = count_list.count(genre)
    file.close()
    return genre_number


def get_line_number_by_title(file_name, title):
    title_list = []
    count_line = 1
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        if title == split_list[GAME_NAME]:
            try:
                return count_line
            except ValueError:
                print("Non-existing game")
        count_line += 1


def sort_abc(file_name):
    title_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        title_list.append(split_list[GAME_NAME])
    sorted_titles = []
    while title_list:
        sorted_titles.append(min(title_list))
        title_list.remove(min(title_list))
    return sorted_titles


def get_genres(file_name):
    genre_list = []
    sorted_genres = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        genre_list.append(split_list[GENRE])

    list_to_sort = list(set(genre_list))

    while list_to_sort:
        sorted_genres.append(min(list_to_sort))
        list_to_sort.remove(min(list_to_sort))
    return sorted_genres


def when_was_top_sold_fps(file_name):
    year_list = []
    sorted_genres = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        try:
            if split_list[GENRE] == 'First-person shooter':
                year_list.append(
                    (float(split_list[MILLIONS_SOLD]), split_list[YEAR]))
        except ValueError:
            print('No First-person shooter game.')
    final = sorted(year_list, key=lambda t: t[0], reverse=True)
    return final[0][1]


# print(count_games('game_stat.txt'))
# print(decide('game_stat.txt', 2000))
# print(get_latest('game_stat.txt'))
# print(count_by_genre('game_stat.txt', 'First-person shooter'))
# print(get_line_number_by_title('game_stat.txt', 'Half-Life'))
# print(sort_abc('game_stat.txt'))
# print(get_genres('game_stat.txt'))
# print(when_was_top_sold_fps('game_stat.txt'))
