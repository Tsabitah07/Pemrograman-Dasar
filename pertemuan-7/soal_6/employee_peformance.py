import csv
from collections import defaultdict

Filename_read = 'performance.csv'
Filename_write = 'summary.csv'

performance_total = defaultdict(list)

with open(Filename_read, 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        division = row['division'].strip()
        score = int(row['score'].strip())

        performance_total[division].append(score)

data = []
for division, scores in performance_total.items():
    max_score = max(scores)
    min_score = min(scores)

    data.append({
        'division': division,
        'max': max_score,
        'min': min_score
    })

field_name = ['division', 'max', 'min']

with open(Filename_write, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_name)

    writer.writeheader()
    writer.writerows(data)

print(f'Sudah di cetak {Filename_write}')