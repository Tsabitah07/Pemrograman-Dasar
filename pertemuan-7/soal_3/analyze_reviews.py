Filename_read = 'product_reviews.txt'
Filename_write = 'report.txt'
word_counts = {'puas': 0, 'rekomendasi': 0}
total_review = 0

with open(Filename_read, 'r', encoding='utf-8') as f:
    for line in f:
        clean_ver = line.strip().lower()
        total_review += 1

        word_counts['puas'] += clean_ver.count('puas')
        word_counts['rekomendasi'] += clean_ver.count('rekomendasi')

report_content = [
    f'Total Review : {total_review} \n',
    f'Filtered Review (puas / rekomendasi) : {word_counts['puas'] + word_counts['rekomendasi']} \n',
    f'Count of \"puas\" : {word_counts['puas']} \n',
    f'Count of \"rekomendasi\" : {word_counts['rekomendasi']}'
]

with open(Filename_write, 'w', encoding='utf-8') as file:
    file.writelines(report_content)

print(f'Sudah di cetak di file {Filename_write}')