import reports
# Printing functions

result1 = reports.get_most_played('game_stat.txt')
result2 = reports.sum_sold('game_stat.txt')
result3 = reports.get_selling_avg('game_stat.txt')
result4 = reports.count_longest_title('game_stat.txt')
result5 = reports.get_date_avg('game_stat.txt')
result6 = reports.get_game('game_stat.txt', "Counter-Strike")
result7 = reports.count_grouped_by_genre('game_stat.txt')
result8 = reports.get_date_ordered('game_stat.txt')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
