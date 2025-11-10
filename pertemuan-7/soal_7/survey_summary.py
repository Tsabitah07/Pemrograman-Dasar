import csv
from collections import defaultdict
from os import write

Filename_read_1 = 'survey_north.csv'
Filename_read_2 = 'survey_south.csv'
Filename_write_1 = 'report.txt'
Filename_write_2 = 'high_score.csv'

total = defaultdict(int)
total_2 = defaultdict(int)

all_data = []
def read_data(file_name):
    with open(file_name, 'r', newline='') as read:
        reader = csv.DictReader(read)

        for row in reader:
            all_data.append(row)

read_data(Filename_read_1)
read_data(Filename_read_2)

for item in all_data:
    region = item['region'].strip()
    score = int(item['score'].strip())

    total[region] += score

for item in all_data:
    respondent = item['respondent'].strip()
    score = int(item['score'].strip())

    total_2[respondent] += score

total_region = len(total)
total_respondent = len(total_2)

print(total)

avg = (total['North'] + total['South']) / total_respondent

if total_2:
    top_region, total_score = max(total.items())
else:
    top_department = 'Undefine'
    total_budget = 0

report_text = [
    f'CUSTOMER SATISFACTION REPORT \n',
    f'============================ \n',
    f'Total Region : {total_region} \n',
    f'Total Respondent : {total_respondent} \n',
    f'Average Score : {avg} \n',
    f'Top Region : {top_region} ({total_score // 3})'
]

with open(Filename_write_1, 'w', encoding='utf-8') as file:
    file.writelines(report_text)

print(all_data)

filtered_list = []

for item in all_data:
    if int(item['score']) > 80:
        filtered_list.append(item)

header_csv = ['region', 'respondent', 'score']

with open(Filename_write_2, 'w', newline='') as files:
    writer = csv.DictWriter(files, fieldnames=header_csv)

    writer.writeheader()
    writer.writerows(filtered_list)

