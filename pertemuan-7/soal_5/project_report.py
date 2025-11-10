import csv
from collections import defaultdict

Filename_read = 'projects.csv'
Filename_write = 'report.txt'

department_budget_total = defaultdict(int)

with open(Filename_read, 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        department = row['department'].strip()
        budget = int(row['budget'].strip())

        department_budget_total[department] += budget

total_department = len(department_budget_total)

if department_budget_total:
    top_department, total_budget = max(department_budget_total.items())
else:
    top_department = 'Undefine'
    total_budget = 0

report_content = [
    f'PROJECT REPORT SUMMARY \n',
    f'======================= \n',
    f'Total department : {total_department} \n'
    f'Top Department : {top_department} ({total_budget}) \n'
]

with open(Filename_write, 'w', encoding='utf-8') as text:
    text.writelines(report_content)

print(f'Sudah di cetak di file {Filename_write}')