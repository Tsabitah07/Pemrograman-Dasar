import csv
from collections import defaultdict

# Nama file input dan output
FILE_A = "store_A.csv"
FILE_B = "store_B.csv"
OUTPUT_CSV = "sales_over_10000.csv"
OUTPUT_REPORT = "report.txt"
FILTER_AMOUNT = 10000


def store_analysis():
    """
    Membaca, menggabungkan, memfilter, dan membuat laporan dari data transaksi CSV.
    """

    # Inisialisasi list untuk menyimpan seluruh data
    all_transactions = []

    # --- 1 & 2. Baca dan Gabungkan Data ---

    def read_csv_data(filename):
        """Membaca data dari satu file CSV dan menambahkannya ke all_transactions."""
        try:
            with open(filename, 'r', newline='') as csvfile:
                # 1. Baca menggunakan csv.DictReader
                reader = csv.DictReader(csvfile, skipinitialspace=True)
                for row in reader:
                    # Bersihkan spasi di sekitar nilai dan konversi amount
                    row['branch'] = row['branch'].strip()
                    row['customer'] = row['customer'].strip()
                    try:
                        row['amount'] = int(row['amount'].strip())
                        all_transactions.append(row)
                    except ValueError:
                        # Abaikan baris jika 'amount' tidak valid
                        print(f"Warning: Amount tidak valid di baris: {row}")
                        continue
        except FileNotFoundError:
            print(f"Error: File input {filename} tidak ditemukan.")
        except Exception as e:
            print(f"Error saat membaca {filename}: {e}")

    read_csv_data(FILE_A)  # Membaca file A
    read_csv_data(FILE_B)  # Membaca file B

    # Jika tidak ada transaksi, hentikan eksekusi
    if not all_transactions:
        print("Tidak ada data transaksi yang berhasil dibaca. Program dihentikan.")
        return

    # --- 3 & 4. Filter Transaksi dan Simpan ke sales_over_10000.csv ---

    # 3. Pilih hanya transaksi dengan amount lebih dari 10000
    filtered_transactions = [
        t for t in all_transactions if t['amount'] > FILTER_AMOUNT
    ]

    # 4. Simpan hasil filter
    fieldnames_csv_out = ['branch', 'customer', 'amount']
    try:
        with open(OUTPUT_CSV, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames_csv_out)
            writer.writeheader()
            writer.writerows(filtered_transactions)
        print(f"Output filter CSV disimpan di: {OUTPUT_CSV}")
    except Exception as e:
        print(f"Error saat menulis {OUTPUT_CSV}: {e}")

    # --- 5 & 6. Agregasi dan Simpan Laporan ke report.txt ---

    # 5. Hitung total dan rata-rata penjualan per cabang dari SELURUH data
    branch_stats = defaultdict(lambda: {'total_sales': 0, 'count': 0})

    total_sales_all = 0

    for transaction in all_transactions:
        branch = transaction['branch']
        amount = transaction['amount']

        # Agregasi per Cabang
        branch_stats[branch]['total_sales'] += amount
        branch_stats[branch]['count'] += 1

        # Total Keseluruhan
        total_sales_all += amount

    total_transactions_count = len(all_transactions)

    # Hitung nilai agregasi akhir
    total_branches = len(branch_stats)
    average_sales = total_sales_all / total_transactions_count if total_transactions_count > 0 else 0

    # Cari Cabang Tertinggi (Top Branch)
    top_branch = "N/A"
    top_sales = 0
    if branch_stats:
        # Cari cabang dengan total_sales maksimum
        top_branch_key = max(branch_stats.keys(), key=lambda b: branch_stats[b]['total_sales'])
        top_branch = f"{top_branch_key} ({branch_stats[top_branch_key]['total_sales']})"

    # Format rata-rata menjadi dua desimal
    formatted_avg_sales = f"{average_sales:.2f}"

    # 6. Simpan laporan ringkasan ke report.txt
    report_content = [
        "STORE PERFORMANCE REPORT\n",
        "==\n",
        f"Total branches: {total_branches}\n",
        f"Total sales: {total_sales_all}\n",
        f"Average sales: {formatted_avg_sales}\n",
        f"Top branch: {top_branch}\n"
    ]

    try:
        with open(OUTPUT_REPORT, "w") as file_out:
            file_out.writelines(report_content)
        print(f"Laporan ringkasan disimpan di: {OUTPUT_REPORT}")
    except Exception as e:
        print(f"Error saat menulis {OUTPUT_REPORT}: {e}")


if __name__ == "__main__":
    store_analysis()