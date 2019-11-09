import reports
# Export functions
result1 = reports.get_most_played('game_stat.txt')
result2 = reports.sum_sold('game_stat.txt')
result3 = reports.get_selling_avg('game_stat.txt')
result4 = reports.count_longest_title('game_stat.txt')
result5 = reports.get_date_avg('game_stat.txt')
result6 = reports.get_game('game_stat.txt', "Counter-Strike")
result7 = reports.count_grouped_by_genre('game_stat.txt')
result8 = reports.get_date_ordered('game_stat.txt')

result_list = [result1, result2, result3,
               result4, result5, result6, result7, result8]

file = open('export_statistics_report2.txt', "w")
for result in result_list:
    file.writelines(str(result))
    file.write("\n")
