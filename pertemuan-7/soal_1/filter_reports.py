Filename_read = 'env_reports.txt'
Filename_write = 'filtered_reports.txt'
keyword = ['hujan', 'banjir']

filtered_lines = []

with open(Filename_read, 'r', encoding='utf-8') as f:
    for line in f:
        clean_ver = line.strip().lower()

        for key in keyword:
            if key in clean_ver:
                filtered_lines.append(line)

with open(Filename_write, 'w', encoding="utf-8") as file:
    file.writelines(filtered_lines)

print(f'Sudah dicetak di {Filename_write}')