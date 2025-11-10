import csv
from collections import defaultdict

Filename_read_1 = 'factory_A.csv'
Filename_read_2 = 'factory_B.csv'
Filename_write = 'summary.csv'

all_transaction = []
status = defaultdict(lambda: {'total_all': 0, 'count': 0})

def read_data(file_name):
    with open(file_name, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            all_transaction.append(row)

read_data(Filename_read_1)
read_data(Filename_read_2)

for item in all_transaction:
    factory = item['factory'].strip()
    amount = int(item['units'].strip())

    status[factory]['total_all'] += amount
    status[factory]['count'] += 1

summary_data = []
for factory, stats in status.items():
    total = int(stats['total_all'])
    count = stats['count']

    avg = total / count if count > 0 else 0

    summary_data.append({
        'factory': factory,
        'total_unit': total,
        'avg_unit': int(avg)
    })

fieldnames = ['factory', 'total_unit', 'avg_unit']
with open(Filename_write, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(summary_data)

print(f'Sudah di buat tablenya di {Filename_write}')