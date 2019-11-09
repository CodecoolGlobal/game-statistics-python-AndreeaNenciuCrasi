import reports
# Export functions

result1 = reports.count_games("game_stat.txt")
result2 = reports.decide("game_stat.txt", 2000)
result3 = reports.get_latest("game_stat.txt")
result4 = reports.count_by_genre("game_stat.txt", 'First-person shooter')
result5 = reports.get_line_number_by_title("game_stat.txt", 'Half-Life')
result6 = reports.sort_abc("game_stat.txt")
result7 = reports.get_genres("game_stat.txt")
result8 = reports.when_was_top_sold_fps("game_stat.txt")

result_list = [result1, result2, result3,
               result4, result5, result6, result7, result8]

file = open('export_statistics_report.txt', "w")
for result in result_list:
    file.writelines(str(result))
    file.write("\n")
