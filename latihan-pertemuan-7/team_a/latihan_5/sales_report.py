# Pastikan Anda sudah membuat file sales.csv dengan isi sesuai soal.
import csv
from collections import defaultdict

FILENAME_INPUT = "sales.csv"
FILENAME_OUTPUT = "report.txt"


def sales_report():
    branch_totals = defaultdict(int)

    try:
        # 1. Baca sales.csv
        with open(FILENAME_INPUT, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            for row in reader:
                # 2. Gunakan hanya branch dan amount
                branch = row['branch'].strip()
                try:
                    amount = int(row['amount'].strip())
                except ValueError:
                    continue

                    # Hitung total penjualan per cabang
                branch_totals[branch] += amount

    except FileNotFoundError:
        print(f"Error: File input {FILENAME_INPUT} tidak ditemukan.")
        return

    # 3. Hitung: Jumlah total cabang unik
    total_branches = len(branch_totals)

    # 3. Hitung: Cabang dengan total penjualan tertinggi
    if branch_totals:
        # Menggunakan max() pada items() untuk mencari pasangan (kunci, nilai) maksimum
        top_branch, top_sales = max(branch_totals.items(), key=lambda item: item[1])
    else:
        top_branch = "N/A"
        top_sales = 0

    # 4. Simpan hasil ke report.txt
    report_content = [
        "SALES REPORT SUMMARY\n",
        "====================\n",
        f"Total branches : {total_branches}\n",
        f"Top branch: {top_branch} ({top_sales})\n"
    ]

    with open(FILENAME_OUTPUT, "w") as file_out:
        file_out.writelines(report_content)

    print(f"Laporan disimpan di {FILENAME_OUTPUT}.")


if __name__ == "__main__":
    sales_report()