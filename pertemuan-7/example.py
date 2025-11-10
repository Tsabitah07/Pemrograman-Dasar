import csv

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # row adalah dict: {'name': 'Alice', 'age': '30'}
        print(row['name'], row['age'])

# menulis CSV
with open('out.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Budi', 'age': 25})
