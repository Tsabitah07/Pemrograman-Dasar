# Pastikan Anda sudah membuat file sales_A.csv dan sales_B.csv.
import csv
from collections import defaultdict

FILE_A = "sales_A.csv"
FILE_B = "sales_B.csv"
FILENAME_OUTPUT = "summary.csv"


def sales_merge():
    all_transactions = []

    # Fungsi untuk membaca dan menggabungkan data
    def read_csv_data(filename):
        try:
            with open(filename, 'r', newline='') as csvfile:
                # 1. Baca menggunakan csv.DictReader
                reader = csv.DictReader(csvfile, skipinitialspace=True)
                # 2. Gabungkan data
                for row in reader:
                    all_transactions.append(row)
        except FileNotFoundError:
            print(f"Error: File {filename} tidak ditemukan.")

    read_csv_data(FILE_A)
    read_csv_data(FILE_B)

    # 4. Hitung total dan rata-rata penjualan per cabang
    branch_stats = defaultdict(lambda: {'total_sales': 0, 'count': 0})

    for transaction in all_transactions:
        # 3. Gunakan kolom branch dan amount
        branch = transaction['branch'].strip()
        try:
            # Konversi amount ke integer
            amount = int(transaction['amount'].strip())
        except ValueError:
            continue  # Abaikan baris jika amount bukan angka

        branch_stats[branch]['total_sales'] += amount
        branch_stats[branch]['count'] += 1

    summary_data = []
    for branch, stats in branch_stats.items():
        total = stats['total_sales']
        count = stats['count']
        # Hitung rata-rata
        avg = total / count if count > 0 else 0

        summary_data.append({
            'branch': branch,
            'total_sales': total,
            'avg_sales': int(avg)  # Sesuai contoh output
        })

    # 5. Simpan hasil ke summary.csv
    fieldnames = ['branch', 'total_sales', 'avg_sales']
    with open(FILENAME_OUTPUT, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(summary_data)

    print(f"Summary penjualan disimpan di {FILENAME_OUTPUT}.")


if __name__ == "__main__":
    sales_merge()