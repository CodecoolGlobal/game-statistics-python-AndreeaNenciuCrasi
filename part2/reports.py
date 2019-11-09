
# Report functions
GAME_NAME = 0
MILLIONS_SOLD = 1
YEAR = 2
GENRE = 3
PUBLISHER = 4


def get_most_played(file_name):
    year_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        year_list.append(
            (float(split_list[MILLIONS_SOLD]), split_list[GAME_NAME]))
    final = sorted(year_list, key=lambda t: t[0], reverse=True)
    file.close()
    return final[0][1]


def sum_sold(file_name):
    sold_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        sold_list.append(float(split_list[MILLIONS_SOLD]))
    file.close()
    return sum(sold_list)


def get_selling_avg(file_name):
    sold_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        sold_list.append(float(split_list[MILLIONS_SOLD]))
    sold_sum = sum(sold_list)
    file = open(file_name, "r")
    count = len(file.readlines())
    file.close()
    return sold_sum/count


def count_longest_title(file_name):
    name_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        name_list.append(split_list[GAME_NAME])
    chr_max_name = len(max(name_list, key=len))
    file.close()
    return chr_max_name


def get_date_avg(file_name):
    year_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        year_list.append(float(split_list[YEAR]))
    year_sum = sum(year_list)
    file = open(file_name, "r")
    count = len(file.readlines())
    file.close()
    return round(year_sum/count)


def get_game(file_name, title):
    title_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        if title == split_list[GAME_NAME]:
            split_list[MILLIONS_SOLD] = float(split_list[MILLIONS_SOLD])
            split_list[YEAR] = int(split_list[YEAR])
            split_list[PUBLISHER] = split_list[PUBLISHER][:-1]
            file.close()
            return split_list


def count_grouped_by_genre(file_name):
    genre_list = []
    dic_genres = {}
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        genre_list.append(split_list[GENRE])
    sort_genre_list = sorted(genre_list)
    for genre in sort_genre_list:
        if genre not in dic_genres:
            dic_genres[genre] = sort_genre_list.count(genre)
    file.close()
    return dic_genres


def get_date_ordered(file_name):
    year_list = []
    final_sorted_list = []
    file = open(file_name, "r")
    for line in file.readlines():
        split_list = line.rsplit('\t')
        year_list.append((split_list[YEAR], split_list[GAME_NAME]))
    sort_year = sorted(
        (sorted(year_list, key=lambda t: t[1])), key=lambda t: t[0], reverse=True)
    for year in sort_year:
        final_sorted_list.append(year[1])
    file.close()
    return final_sorted_list


# print(get_most_played('game_stat.txt'))
# print(sum_sold('game_stat.txt'))
# print(get_selling_avg('game_stat.txt'))
# print(count_longest_title('game_stat.txt'))
# print(get_date_avg('game_stat.txt'))
# print(get_game('game_stat.txt', "Counter-Strike"))
# print(count_grouped_by_genre('game_stat.txt'))
# print(get_date_ordered('game_stat.txt'))
