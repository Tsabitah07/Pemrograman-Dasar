Filename_read = 'sports_news.txt'
Filename_write = 'report.txt'
word_count = {'gol': 0, 'menang': 0}
total_lines = 0

with open(Filename_read, 'r', encoding='utf-8') as f:
    for line in f:
        total_lines += 1
        clean_ver = line.strip().lower()

        word_count['gol'] += clean_ver.count('gol')
        word_count['menang'] += clean_ver.count('menang')

report_content = [
    f'Total Lines : {total_lines} \n',
    f'Count of \"Gol\" : {word_count['gol']} \n',
    f'Count of \"Menang\" : {word_count['menang']} \n'
]

with open(Filename_write, 'w', encoding='utf-8') as file:
    file.writelines(report_content)

print(f'Sudah dicetak di {Filename_write}')