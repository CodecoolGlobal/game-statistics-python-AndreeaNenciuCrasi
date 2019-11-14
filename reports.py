
# Report function

GAME_NAME = 0
MILLIONS_SOLD = 1
YEAR = 2
GENRE = 3


def bubbles(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubblesReverse(arr, key=None):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] < arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


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
    return latest[0]


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

            return count_line
        count_line += 1
    file.close()

    raise ValueError('Non-existing game')


def sort_abc(file_name):
    title_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        title_list.append(split_list[GAME_NAME])

    final_titles = bubbles(title_list)

    # while title_list:
    #     final_titles.append(min(title_list))
    #     title_list.remove(min(title_list))
    file.close()
    return final_titles


def get_genres(file_name):
    genre_list = []
    final_genres = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        genre_list.append(split_list[GENRE])

    list_to_s = list(set(genre_list))

    while list_to_s:
        final_genres.append(min(list_to_s))
        list_to_s.remove(min(list_to_s))
    file.close()
    return final_genres


def when_was_top_sold_fps(file_name):
    year_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')

        if split_list[GENRE] == 'First-person shooter':
            year_list.append(
                (float(split_list[MILLIONS_SOLD]), split_list[YEAR]))
    if len(year_list) == 0:
        raise ValueError

    final = bubblesReverse(year_list, 0)
    # print(final[0][1])
    file.close()
    return int(final[0][1])
